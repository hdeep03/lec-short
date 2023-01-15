# Lecture Shortener

An AI @ MIT Labs project which sought to use advances in transcription, image processing, and natural language processing to shorten long lectures.
The project uses OpenAI's whisper to do transcription, pytesseract for image processing, and SBERT for extractive summarization to find the most important parts of the lecture. Lastly, the implementation is dependent on ffmpeg for video processing. 

The pipeline we have built is designed for speed, and we have tried to optimize all steps of the processing. Currently, the pipeline is able to create a shortened video in less than 20% of the length of the initial video (Ex. if the initial video was 15 minutes long, the lecture shortening process would take less than 3 minutes to run). If you would like to try it out for yourself, please check out our website at: http://www.lecshort.com. 

If you are trying to run this locally, make sure you install all the dependencies with ```pip install -r requirements.txt``` and run ```gunicorn --bind=0.0.0.0:80 --timeout 3600 -w 4 app:app```

Reach out to hdeep [at] mit.edu with any questions or to request any improvements.
