import urllib
import re
from bs4 import BeautifulSoup

def url_Save(song_name):
    if(not(song_name and song_name.strip())): 
        return 
    query = urllib.parse.quote(song_name)
    #for i in range(0,len(song_name)):
    #    url = url  + song_name[i]
    #    if i != len(song_name)-1:
    #       url = url + "+"

    url_youtube = "https://www.youtube.com/results?search_query="+query
    scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url_youtube)
    path = urllib.parse.quote(path)
    url_youtube = urllib.parse.urlunsplit((scheme, netloc, path, query, fragment))
    html = urllib.request.urlopen(url_youtube)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_link = "https://www.youtube.com/watch?v=" + str(video_ids[0])

    return video_link
