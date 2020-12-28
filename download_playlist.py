import pytube

url = input('Playlist url:')
itag = 22
playlist = pytube.Playlist(url)

for video in playlist:
    v = pytube.YouTube(video)
    file_name = video.title()
    try:
        stream = v.streams.get_by_itag(itag)
        print(f"Downloading {file_name} ...")
        stream.download(filename=file_name)
    except:
        print(f"Something wrong with {file_name}.\n The url: {v}")
print("Done")
