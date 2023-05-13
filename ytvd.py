import requests
from pyquery import PyQuery as pq
from pytube import YouTube

# Ask user for the YouTube video URL
url = 'https://youtu.be/v-hL3sks2qI'

# Create a YouTube object and get the video title


# Send a GET request to the video URL and get the HTML content
response = requests.get(url)
html = response.content

# Use PyQuery to parse the HTML and extract the stream data
doc = pq(html)
print(doc)
print("\n\n\n\n")
stream_data = doc('script:contains("streamingData")').text()
print(stream_data)
# stream_data = stream_data.split('ytInitialPlayerResponse = ')[1]
# stream_data = stream_data.split(';\n')[0]

# Get the first stream (usually the highest quality) with the video and audio together
stream_urls = eval(stream_data)['streamingData']['adaptiveFormats']
stream = None
for s in stream_urls:
    if 'audio' in s['mimeType']:
        continue
    stream = s
    break

# Download the video
if stream:
    yt_stream = yt.streams.get_by_itag(stream['itag'])
    yt_stream.download(filename=title)
    print(f"Video '{title}' downloaded successfully!")
else:
    print("No suitable video stream found.")



# import requests
# from pyquery import PyQuery as pq
# from pytube import YouTube

# # Ask user for the YouTube video URL
# url = 'https://youtu.be/v-hL3sks2qI'

# # Send a GET request to the video URL and get the HTML content
# response = requests.get(url)
# html = response.content

# # Use PyQuery to parse the HTML and extract the video title
# doc = pq(html)
# title = doc('title').text()

# # Create a YouTube object
# yt = YouTube(url)

# # Get the first stream (usually the highest quality) with the video and audio together
# stream_urls = yt.streams.filter(progressive=True, file_extension='mp4').all()
# stream = stream_urls[-1] # get the last one (highest resolution)

# # Download the video
# stream.download(filename=title)
# print(f"Video '{title}' downloaded successfully!")
