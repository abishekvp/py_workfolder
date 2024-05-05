import os
from telegram import Update, MessageEntity
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from pytube import YouTube
from moviepy.editor import *
import os
TOKEN = '5148319110:AAGe4XFc8akli8Hbr2r3LF0QZPyc-WZ3Pto'

AUDIO_SAVE_DIRECTORY = "Audio"
VIDEO_SAVE_DIRECTORY = "Video"

os.makedirs(VIDEO_SAVE_DIRECTORY, exist_ok=True)
os.makedirs(AUDIO_SAVE_DIRECTORY, exist_ok=True)

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


def MakeReply(mesg):
    if "Hi" in mesg:
        return "Hello"
    elif "Hello" in mesg:
        return "Hi"
    else:
        return "I am a bot, I don't understand that"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_mesg = "Hi"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_mesg)

async def HandleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mesg = update.message.text
    print(mesg)
    if "youtube.com" in mesg or "youtu.be" in mesg:
        download_audio(mesg)
        mesg = 'Audio Donwloaded'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mesg)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=MakeReply(mesg))
        

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, HandleMessage))
    application.run_polling()

if __name__ == '__main__':
    main()