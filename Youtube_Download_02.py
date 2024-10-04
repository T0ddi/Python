from pytube import YouTube
link = "https://www.youtube.com/watch?v=Z2607_P40iY" # the video URL goes here
youtube = YouTube(link)
# To download the highest resolution video
stream = youtube.streams.get_highest_resolution()
# To download as mp4 specifically despite the resolution
stream = youtube.streams.get_by_itag(22)
stream.download()
print("Download completed.")