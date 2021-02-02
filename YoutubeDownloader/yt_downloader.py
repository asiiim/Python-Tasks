# Importing the essential libraries that we wanted during this programming.
from pytube import YouTube
import os

# File Destination
DESTINATION = os.getcwd() + '\\Videos'

# Ask user to simply input link.
link = input('Paste the link here: ')

# Generate object - YouTube object
try:
    youtube_obj = YouTube(link)

    # Summary of the video from the youtube object
    print('\nSummary')
    print(f'Title: {youtube_obj.title}')
    print(f'Duration: {youtube_obj.length}')

    # Get the streams filtered with mp4
    youtube_obj.streams.get_by_itag(18).download(DESTINATION)

except:
    raise ConnectionError('Try Again.')