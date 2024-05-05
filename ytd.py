from pytube import YouTube
from moviepy.editor import *
import os

AUDIO_SAVE_DIRECTORY = "D:\\Audio"
VIDEO_SAVE_DIRECTORY = "E:\\Videos"

os.makedirs(os.path.dirname(VIDEO_SAVE_DIRECTORY), exist_ok=True)
os.makedirs(os.path.dirname(AUDIO_SAVE_DIRECTORY), exist_ok=True)

def download_video(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()
    for i in os.listdir(VIDEO_SAVE_DIRECTORY):
        if str(VIDEO_SAVE_DIRECTORY+'\\'+str(video.title)+".mp4")==i:return 0
        else:pass
    try:video.download(VIDEO_SAVE_DIRECTORY)
    except:return 0
    
def download_audio(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()
    for i in os.listdir(AUDIO_SAVE_DIRECTORY):
        if str(AUDIO_SAVE_DIRECTORY+'\\'+str(video.title)+".mp3")==i:return 0
        else:pass
    try:
        loc = video.download(AUDIO_SAVE_DIRECTORY)
        video = VideoFileClip(loc)
        video.audio.write_audiofile(str(loc).replace(".mp4",".mp3"))
        video.close()
        os.remove(str(loc).replace(".mp3",".mp4"))
    except:return 0

while True:
    
    link=input("Link : ")

    if "vid" in link:
        link = link.split(" ")[1]
        download_video(link)
    else:download_audio(link)

