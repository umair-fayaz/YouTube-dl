from pytube import YouTube
import os
import sys

link = input("Enter the video link: ")
print("Loading video...")
if not os.path.exists('Downloaded_Videos'):
    os.makedirs('Downloaded_Videos')

def show_progress_bar(stream, chunk: bytes, bytes_remaining: int):
  current = ((stream.filesize - bytes_remaining)/stream.filesize)
  percent = ('{0:.1f}').format(current*100)
  progress = int(50*current)
  status = '█' * progress + '-' * (50 - progress)
  sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
  sys.stdout.flush()

try:
    folder = "Downloaded_Videos"
    directory = os.getcwd()
    SAVE_PATH = os.path.join(directory, folder)

    yt = YouTube(link)
    print('Title :',yt.title)

    print('Available Formats: ')
    for stream in yt.streams.all():
        print(stream)

    itag =  input("\nEnter the itag number to select a format: ")
    stream = yt.streams.get_by_itag(itag)

    print("\nDownloading --> "+yt.title+' to '+SAVE_PATH)

    yt.register_on_progress_callback(show_progress_bar)
    stream.download(SAVE_PATH)
    print('Download Finished!')
    input('Press Return to Exit')


except Exception as e:
    print("Error :",e)
    input('Press Return to Exit')
