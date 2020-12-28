import pytube

url = input('Enter youtube url:')
# url = 'https://www.youtube.com/watch?v=UM6YDJ2aalU&t=217s'  # Example

itag = 22  # Stream: itag="22" type=video/mp4 res=720p
video = pytube.YouTube(url)
print('Information about streams:')
for v in video.streams:
    print(v)

try:
    stream = video.streams.get_by_itag(itag)  # if you need another quality then change value of itag
# Video doesnt have itag=22
except:
    itag = input("Choose itag. For example 299")
    stream = video.streams.get_by_itag(int(itag))

file_name = video.title  # if dont want write or skip file name

# file_name = input("You can skip. Filename:")
# if file_name == '':
#     file_name = video.title

print('Downloading...')
stream.download(filename=file_name)
print('Done.')