**Note:**
This a fork of the original project as it's no longer maintained.

## Usage
- Make sure Python3 is installed properly, do `pip install -r requirements.txt` and then you can use `download.sh` to launch the program
- Create $HOME/1fichier-dl.conf config file or windows directory instead of $HOME

Example config file:
```
[aria2]
host = HOST
port = PORT_NUMBER
token = YOUR_TOKEN
```

Change according to your configuration

## Fork Features
- paulo27ms fixed looping bug when proxy works but download fails
- Add aria2 integration from oureveryday
- Add token authentication
- Use config file instead of hardcoded values

# 1fichier-dl
<p align="center">
  <b>1Fichier Download Manager.</b>
</p>

<p align="center">
  <img src="https://github.com/sobkas/1fichier-dl/blob/main/preview.png?raw=true"></img>
</p>

## Features
⭐ Manage your downloads

⭐ Bypass time limits

## Credits
* All icons, including the app icon, were provided by [Feather](https://feathericons.com/).
* Proxies provided by [Proxyscan](https://www.proxyscan.io/).
* paulo27ms for proxy stuff
* oureveryday for aria2 stuff
