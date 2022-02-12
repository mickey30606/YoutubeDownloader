from pytube import YouTube, Playlist
from moviepy.editor import *
#from pydub import AudioSegment

def Cut(originfile, start, end, targetfile):
    originfile = "./music/"+originfile
    targetfile = "./music/"+targetfile
    song = AudioSegment.from_mp3(originfile)
    song[start:end].export(targetfile)

def GetYoutubePlayList(url, filename):
    pl = Playlist(url)
    print(pl)
    print('start')
    pl.download_all(filename)
    print('end')

def GetYoutubeVideo(url, filename):
    print('start')
    YouTube(url).streams.get_highest_resolution().download(filename=filename)
    print('end')

def VideoToMusic(filename, targetname):
    video = VideoFileClip(filename)
    video.audio.write_audiofile(targetname)
    video.close()

if __name__ == "__main__":
    filename = "tmp.mp4"
    targetname = "tmp.mp3"
    url = "https://www.youtube.com/watch?v=_HxkMKb_EQs"
    GetYoutubeVideo(url, filename)
    print("get video success")
