from __future__ import unicode_literals
from youtube_dl import YoutubeDL


def download_songs_lmao(url,playlist_name):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'C:/SONGS FROM SPOTIFY/{playlist_name}/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])