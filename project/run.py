import sys
import subprocess
import spotipy
import runHelper

api = spotipy.Spotify(auth=runHelper.TOKEN)

try:
    current_song = api.currently_playing()

except subprocess.CalledProcessError:
    runHelper.notify("Couldn't find any songs playing", icon='error')
    sys.exit(1)

try:
    url = current_song["item"]["uri"]
    url_list = [url]
    api.playlist_remove_all_occurrences_of_items(runHelper.PLAYLIST, url_list)
    api.playlist_add_items(runHelper.PLAYLIST, url_list, position=None)

except subprocess.CalledProcessError:
    runHelper.notify("Couldn't add song to playlist", icon='error')
    sys.exit(1)