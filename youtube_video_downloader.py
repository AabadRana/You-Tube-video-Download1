from pytube import YouTube

link="https://www.youtube.com/watch?v=EJzOeoAapTk&t=302s"
youtube_2=YouTube(link)
#print(youtube_2.title)
#print(youtube_2.thumbnail_url)

videos=youtube_2.streams.all()

#videos=youtube_2.streams.filter(only_video=True)
vid=list(enumerate(videos))
for i in vid:
    print(i)
strm=int(input("enter: "))
videos[strm].download()
print("successfully")
