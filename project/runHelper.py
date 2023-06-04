import os
import subprocess
import spotipy.util as util
from dotenv import load_dotenv

def authorize_with_spotify():
    # only need to run this once
    # returns: token
    os.environ['SPOTIPY_CLIENT_ID'] = os.getenv("SPOTIPY_CLIENT_ID")
    os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv("SPOTIPY_CLIENT_SECRET")
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

    scopes = 'user-library-read user-library-modify playlist-modify-private playlist-read-private playlist-modify-public playlist-read-collaborative user-read-currently-playing'
    token = util.prompt_for_user_token(os.getenv("USERNAME"), scopes)

    return token

def notify(msg, icon='face-surprise'):
    cmd = ['notify-send', '-i', icon, msg]
    subprocess.call(cmd)


load_dotenv("../tokens.env")
USER = os.getenv("USER")
TOKEN = authorize_with_spotify()
PLAYLIST = os.getenv("CURRENT_PLAYLIST")



"""
TODO
- no terminal popup when pressed
- display a list of playlists once an hour
- use keyboard shortcut to run activator
"""