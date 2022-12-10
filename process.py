'''
Downloads and processes the video
'''
from pytube import YouTube
import whisper
import pandas as pd
import time
import numpy as np
from summarizer.sbert import SBertSummarizer
from secrets import token_hex
import sys
import os
import cv2
import pytesseract
import tesserocr
from PIL import Image

gpu = False 
whisper_model = whisper.load_model("tiny.en") 
embedding_model = SBertSummarizer('all-mpnet-base-v2')
api = tesserocr.PyTessBaseAPI()
n_samples = 3


def downloadVideo(yLink):
    yt = YouTube(yLink)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_360p_files = mp4_files.get_by_resolution("360p") #Download low-res for faster image processing
    rand = token_hex(16)
    mp4_360p_files.download(output_path=f'data/', filename=f"{rand}.mp4")
    path = f"data/{rand}.mp4"
    print(f'Downloaded Video to {path}')
    return rand, path

def transcribeVideo(path):
    result = whisper_model.transcribe(path, fp16=gpu)
    transcript = result['segments']
    start_vals = np.array([transcript[x]['start'] for x in range(len(transcript))])
    end_vals = np.array([transcript[x]['end'] for x in range(len(transcript))])
    segment_length = end_vals - start_vals
    text_segment = [transcript[x]['text'] for x in range(len(transcript))]
    return {'starts':start_vals, 'ends':end_vals, 'lengths':segment_length, 'text':text_segment}

def summarize_text(text, ratio):  #Summarizer using S-BERT model
  return embedding_model(text, ratio)


def video_processing(path, start_vals, end_vals, ap):
    tstart = time.time()
    name = f"{path}frame.jpg"

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
        
    if not cap.isOpened():
        raise IOError("Video not working")

    avg_words = np.zeros_like(start_vals)

    for i in range(len(start_vals)):
        #if ap[i]:
        #    continue
        t = 1000*np.linspace(start_vals[i], end_vals[i], n_samples+2)
        t = t[1:-1]
        t = t.astype(np.int32)
        res = 0
        for timee in t:
            cap.set(cv2.CAP_PROP_POS_MSEC, timee)
            ret, frame = cap.read()
            if not ret:
                continue
            imgH, imgW,_ = frame.shape
                
            y = int(imgH*0.05)
            h = int(imgH*0.90)

            x = int(imgW*0.05)
            w = int(imgW*0.90)

            frame1 = frame[y:y+h, x:x+w]
            cv2.imwrite(name, frame1)

            pil_image = Image.open(name)
            api.SetImage(pil_image)
            text = api.GetUTF8Text()
            res+=len(text.split())
        avg_words[i] = res/n_samples

    return avg_words/max(avg_words)


def generateAudioPreservationMask(text_segment, ratio): #Generates a mask for which text segments should be preserved
  complete_transcript = " ".join(text_segment)
  summary = summarize_text(complete_transcript, ratio)
  preserve = [False]*len(text_segment)
  for snippet in summary.lower().split('.'):
    for x in range(len(text_segment)):
      if snippet.strip() in text_segment[x].lower():
        preserve[x] = True
        break
  return preserve

def process(yLink, cratio, dt):
    tstart = time.time()
    rand, input_file = downloadVideo(yLink)
    print(f'Download done in {time.time()-tstart:.2f}')
    tstart = time.time()

    ret_dict = transcribeVideo(input_file)
    preserved = generateAudioPreservationMask(ret_dict['text'], cratio)
    print(f'Audio Processing done in {time.time()-tstart:.2f}')
    tstart = time.time()

    norm_vscores = video_processing(input_file,ret_dict['starts'], ret_dict['ends'], preserved)

    print(f'Video Processing done in {time.time()-tstart:.2f}')
    tstart = time.time()

    val = int(np.sqrt(len(norm_vscores)))+1
    indicies = np.argpartition(norm_vscores, -val)[-val:].astype(int)

    for idx in indicies:
        preserved[idx] = True

    
    
    importantSet = ["important", "vital", "critical", "essential", "urgent", "valuable", "useful", "necessary", "relevant", "fundamental"]
    uselessSet = ["not important", "irrelevant", "useless", "on a tangent"]
    
    for x in range(len(ret_dict['text'])):
        for y in importantSet:
            if y in ret_dict['text'][x]:
                preserved[x] = True
        for y in uselessSet:
            if y in ret_dict['text'][x]:
                preserved[x] = False
    
    audio_df = pd.DataFrame({'Text':ret_dict['text'], 'Start':ret_dict['starts'], 'End':ret_dict['ends'], 'Preserve':preserved})
    saved_clip_meta = audio_df.where(audio_df['Preserve']).dropna()
    print(preserved)

    final_starts, final_ends, final_pres = [], [], []

    tups = (ret_dict['starts'], ret_dict['ends'], preserved)
    i = 0
    while i < len(tups[0]):
        start = tups[0][i]
        ptype = tups[2][i]
        while i<len(tups[0])-1 and tups[2][i]==tups[2][i+1]:
                i+=1
        end = tups[1][i]
        final_starts.append(start)
        final_ends.append(end)
        final_pres.append(ptype)
        i+=1


    startList = final_starts
    endList = final_ends
    preserved = final_pres

    longString = ""

    gamma = dt

    for i in range(0, len(startList)):

        if preserved[i]:
        
                if (i == len(startList) - 1):
                    longString += "[0:v]trim=" + str(startList[i]) + ":,setpts=PTS-STARTPTS[v" + str(i + 1) + "]; "

                else:
                    longString += "[0:v]trim=" + str(startList[i]) + ":" + str(endList[i]) + ",setpts=PTS-STARTPTS[v" + str(i + 1) + "]; "

            

        else:

            if (i == len(startList) - 1):

                    longString += "[0:v]trim=" + str(startList[i]) + f":,setpts={float(1/gamma)}*(PTS-STARTPTS)[v" + str(i + 1) + "]; "
            
            else:

                longString += "[0:v]trim=" + str(startList[i]) + ":" + str(endList[i]) + F",setpts={float(1/gamma)}*(PTS-STARTPTS)[v" + str(i + 1) + "]; "

    
    for i in range(0, len(startList)):

        if preserved[i]:
        
            if (i == len(startList) - 1):
                longString += "[0:a]atrim=" + str(startList[i]) + ":,asetpts=PTS-STARTPTS[a" + str(i + 1) + "]; "

            else:
                longString += "[0:a]atrim=" + str(startList[i]) + ":" + str(endList[i]) + ",asetpts=PTS-STARTPTS[a" + str(i + 1) + "]; "

        

        else:

            if (i == len(startList) - 1):

                longString += "[0:a]atrim=" + str(startList[i]) + f":,asetpts=PTS-STARTPTS,atempo={gamma}[a" + str(i + 1) + "]; "
            
            else:

                longString += "[0:a]atrim=" + str(startList[i]) + ":" + str(endList[i]) + f",asetpts=PTS-STARTPTS,atempo={gamma}[a" + str(i + 1) + "]; "


        

    for i in range(1, len(startList) + 1):

        longString += "[v" + str(i) + "]" + "[a" + str(i) + "]"

    longString += "concat=n=" + str(len(startList)) + ":v=1:a=1"

    #print(f"ffmpeg -i '{input_file}' -filter_complex '{longString}' -c:v libx264 -preset medium -profile:v baseline 'output/{rand}.mp4' -hide_banner -loglevel error")

    os.system(f"ffmpeg -i '{input_file}' -filter_complex '{longString}' -c:v libx264 -preset medium -profile:v baseline 'output/{rand}.mp4' -hide_banner -loglevel error")
    print(f'Export done in {time.time()-tstart:.2f}')

    return f'output/{rand}.mp4'


if __name__=="__main__":
    process(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
