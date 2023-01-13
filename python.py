from pytube import YouTube

link = "https://youtube.com/shorts/9tOrqWNDvIA?feature=share"

youtube_1 = YouTube(link)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter: "))
videos[strm].download()
print("Successfully")