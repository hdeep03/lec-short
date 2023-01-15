# Video_Shortener

An AI @ MIT Labs project which sought to use advances in transcription, image processing, and natural language processing to shorten long lectures.
The project uses OpenAI's whisper to do transcription, pytesseract for image processing, and SBERT for extractive summarization to find the most important parts of the lecture. 
The resulting pipeline can be run quickly in less than 20% of the length of the initial video. The website is hosted at http://www.lecshort.com. 

The command to run the server is ```gunicorn --bind=0.0.0.0:80 --timeout 3600 -w 4 app:app```

Reach out to hdeep [at] mit.edu with any questions or to request any improvements.
