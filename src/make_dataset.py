"""
Youtube Video Batch Downloader

@author Harsh Deep
"""

import readline
import subprocess
import argparse
from multiprocessing import Pool
import time

MAX_THREADS = 4

def yt_downloader(url):
    """
    Downloads a single youtube video
    @param url: the url of the video
    @param output_loc: the directory and output format of the video
    """
    subprocess.run(["yt-dlp", "-o", "data/raw/%(id)s.%(ext)s", "-f", "mp4", url])


if __name__ == '__main__':

    start = time.time()
    parser = argparse.ArgumentParser(description='Batch Downloader for Youtube Videos')
    parser.add_argument("file", help = "Input file with list of YT urls")
    path = parser.parse_args()
    
    with open(path.file, 'r') as f:
        urls = f.readlines()
        print(f'{len(urls)} videos to download')
        workers = min(len(urls), MAX_THREADS)
        with Pool(workers) as p:
            print(f'Downloading with {workers} workers...')
            p.map(yt_downloader, urls)
    print(f'Task completed in {time.time()-start:.2f} seconds')
            