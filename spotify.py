import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from time import sleep
from pprint import pprint
import search_youtube
import download_songs


playlistname = str(input("Enter the folder/playlists name :"))


url1 = str(input("Enter the playlist url: "))
session = HTMLSession()

response = session.get(url1)

response.html.render(sleep=3)

soup = bs(response.html.html, "html.parser")

songs = soup.find_all('div',class_="da0bc4060bb1bdb4abb8e402916af32e-scss standalone-ellipsis-one-line _8a9c5cc886805907de5073b8ebc3acd8-scss")

artists = soup.find_all('span',class_="_966e29b71d2654743538480947a479b3-scss standalone-ellipsis-one-line f3fc214b257ae2f1d43d4c594a94497f-scss")
songs_names_list = []
artists_names_list = []
for i in range(0,len(songs)):
    temp = songs[i]
    temp_artist = artists[i]
    songnames_txt = temp.get_text()
    artistnames_txt = temp_artist.get_text()
    songs_names_list.append(songnames_txt)
    artists_names_list.append(artistnames_txt)
print("Found all the songs!")

song_names1 = open('songnames.txt','w',encoding='utf-8')

for i in range(0,len(songs_names_list)):
    print(f"{songs_names_list[i]} by {artists_names_list[i]}")

    try:
        song_names1.write(f"{songs_names_list[i]} by {artists_names_list[i]}\n")
    except:
        continue

song_names1.close()

songs_list_url = []
songs_list_name = []
song_namess = open('songnames.txt','r',encoding='utf-8')
print("Starting to search the urls!")
for i in song_namess:
    songs_list_url.append(search_youtube.url_Save(i))
    songs_list_name.append(i)

song_namess.close()

for i in songs_list_url:
    download_songs.download_songs_lmao(i,playlistname)






## old
#url1 = "https://open.spotify.com/playlist/4kF5AkUNeKUZ0lqMlYGUQ8?si=520b3812da994b85"
#html_text = requests.get(url1)
#soup = bs(html_text.content,'html.parser')
#lol1 = soup.find_all('div')
#lol = lol1[0].find_all('span',class_='track-name')
##lol = soup.find_all('span',class_='track-name')