# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# chrome_options = Options()
# chrome_services = Service(ChromeDriverManager().install())
# chrome_options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(service = chrome_services,options = chrome_options)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# element = driver.find_element(By.NAME,"q")
# element.clear()
# element.send_keys("pycon")
# element.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

# Practicing pytube
from pytube import YouTube
from pytube import Playlist

#creating object
# yt = YouTube("https://www.youtube.com/watch?v=-AGcvRsUK3I")
# print(yt.title)
# print(yt.thumbnail_url)

#streams
# streams = yt.streams
#filtering progressive and adaptive streams
# print(streams.filter(progressive= True))
# print(streams.filter(adaptive= True))

#To query the streams that contain only the audio track:
# print(streams.filter(only_audio=True))
# to filter only mp4 format files
# print(streams.filter(file_extension=True))

#downloading the file
# stream = yt.streams.get_by_itag(22)
# stream.download()

# Subtitle/Caption Tracks
# yt = YouTube("https://www.youtube.com/watch?v=lW2pXu97Yvo")
# caption=yt.captions.get_by_language_code('en')

#INITIALIZING PLAYLIST URL
p = Playlist("https://www.youtube.com/playlist?list=PLpG69FdeMzXbvI-Kju0UegpFdn_mZtjeg")

for video in p.videos:
    video.streams.first().download()
    print("Done")

    from pytube import YouTube
    from pytube import Playlist
    from pytube import Channel
    from pytube import Search

    # p = Playlist('https://www.youtube.com/playlist?list=PLZoTAELRMXVO3gDYhbHFyFDesgLDoO5T-')
    # print(f'Downloading: {p.title}')
    # for i in p.video_urls:
    #     print(i)

    # c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    # # print(f'Downloading videos by: {c.channel_name}')
    # for url in c.video_urls[:3]:
    #     print(url)

    try:
        s = Search("Neymar Jr")
        print(s.results)
    except:
        print("there is error")

import requests

API_KEY = "AIzaSyBVX1wuuYSpwBDEzBuXO-N0WPWzudpKyIY"
VIDEO_ID = "VIDEO_ID"

# Construct the API request URL
url = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&part=snippet,statistics&id={VIDEO_ID}"

# Make the API request
response = requests.get(url)
data = response.json()

# Extract video information
if "items" in data and len(data["items"]) > 0:
    video_info = data["items"][0]
    snippet = video_info["snippet"]
    statistics = video_info["statistics"]

    title = snippet["title"]
    description = snippet["description"]
    views = statistics["viewCount"]
    likes = statistics["likeCount"]

    print("Title:", title)
    print("Description:", description)
    print("Views:", views)
    print("Likes:", likes)
else:
    print("Video not found or API error")
import requests

API_KEY = "AIzaSyBVX1wuuYSpwBDEzBuXO-N0WPWzudpKyIY"
VIDEO_ID = "VIDEO_ID"

# Construct the API request URL
url = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&part=snippet,statistics&id={VIDEO_ID}"

# Make the API request
response = requests.get(url)
data = response.json()

# Extract video information
if "items" in data and len(data["items"]) > 0:
    video_info = data["items"][0]
    snippet = video_info["snippet"]
    statistics = video_info["statistics"]

    title = snippet["title"]
    description = snippet["description"]
    views = statistics["viewCount"]
    likes = statistics["likeCount"]

    print("Title:", title)
    print("Description:", description)
    print("Views:", views)
    print("Likes:", likes)
else:
    print("Video not found or API error")





