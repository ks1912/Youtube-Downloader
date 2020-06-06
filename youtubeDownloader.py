from pytube import *

url = "https://www.youtube.com/watch?v=1Qe-sie4xFw"
path_save = "C:\\Users\\User\\Desktop"
# Creating youtube object with URL ...

obj = YouTube(url)
# stem = obj.streams.all()
# for s in stem:
#   print(s)

# strm_first_video = obj.streams.first()
# print(strm_first_video)

# strm_highest_resolution = obj.streams.get_highest_resolution()
# print(strm_highest_resolution)

# strm_get_resolution = obj.streams.get_by_resolution('360p')
# print(strm_get_resolution)

strm_audio = obj.streams.get_audio_only()
# print(strm_audio)

# strm_size = strm_highest_resolution.filesize_approx
# print(strm_size)

# strm_title = strm_highest_resolution.title
# print(strm_title)

# strm_des = obj.description
# print(strm_des)

# DOWNLOAD FUNCTION
# strm_highest_resolution.download(path_save)
strm_audio.download(path_save)
print('Downloading Completed please close and restart to again download a new video')






