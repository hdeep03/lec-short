"""
Build Dataset

@author Harsh Deep
"""

import readline
import json
import os
import subprocess
import argparse
from multiprocessing import Pool
import time
import whisper

MAX_THREADS = 4

def yt_downloader(url):
    """
    Downloads a single youtube video
    @param url: the url of the video
    @param output_loc: the directory and output format of the video
    """
    subprocess.run(["yt-dlp", "-o", "data/raw/%(id)s.%(ext)s", "-f", "mp4", url])

def audioTranscribe(file, target_file):
    '''
    Transcribes the audio from a file
    '''
    if ".DS" in file:
        return 0;
    #print('Loading whisper model ...')
    model = whisper.load_model("base")
    #print('Model Loaded')
    result = model.transcribe(file)
    with open(f"{target_file}.json", "w") as outfile:
        outfile.write(json.dumps(result['segments']))


if __name__ == '__main__':
    start = time.time()
    parser = argparse.ArgumentParser(description='Batch Downloader for Youtube Videos')
    parser.add_argument("file", help = "Input file with list of YT urls")
    path = parser.parse_args()
    '''
    with open(path.file, 'r') as f:
        urls = f.readlines()
        print(f'{len(urls)} videos to download')
        workers = min(len(urls), MAX_THREADS)
        with Pool(workers) as p:
            print(f'Downloading with {workers} workers...')
            p.map(yt_downloader, urls)
        print(f'Download completed in {time.time()-start:.2f} seconds')
    '''
    print('Beginning Audio Transcription ...')
    for f in os.listdir("data/raw/"):
        audioTranscribe('data/raw/{}.mp4'.format(f[:-4]), 'data/processed/{}'.format(f[:-4])) 
    