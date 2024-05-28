from pytube import YouTube

link = str(input('enter url: '))
yt = YouTube(link)
print("video downloding....")
video = yt.streams.get_highest_resolution()
video.download()
print('video downloaded!')