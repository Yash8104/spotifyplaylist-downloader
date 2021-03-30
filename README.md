# Spotifyplaylist-downloader
Just a basic python script to download songs from spotify playlist links

### What is required?
- Python version 3.7.0
- All the modules in requirements.txt
- [Choco](https://chocolatey.org/install) and [ffmpeg](https://chocolatey.org/packages/ffmpeg)

## How to install the modules:
- Open cmd in the directory of the code
- Then run this code
```
pip install -r requirements.txt
```

## How to install choco:
- First open cmd in administrative shell
- Then install powershell
```
powershell.exe
```
- Then run this code 
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
- Chocolatey is installed.

## How to install FFmpeg

- Run this
```
choco install ffmpeg
```

- Done

#### Note:
You can run this in an virtual env (recommened)


## The Installation process is finished

Running the code is pretty straight forward.You just have to run the spotify.py script.
**The songs are saved in c:/SONGS FROM SPOTIFY/**

_For further queries feel free to contact me ;)_
