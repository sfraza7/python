from pytube import YouTube
from  sys import argv

link =argv[1]
yt =YouTube(link)

print("title:",yt.title)

print("view: ",yt.views)

#yd = yt.streams.get_highest_resolution()
yd = yt.streams.get_audio_only()

#yd.download()
download_path = r'C:\Users\farha\Videos\ytdownloads'

try:
    yd.download(download_path)
except Exception as e:
    print(f"An error occurred: {e}")


#yd.download('C:\Users\farha\Videos\New folder')
            