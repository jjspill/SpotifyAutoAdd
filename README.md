# SpotifyAutoAdd
Script that adds current song to chosen playlist

# To create a new python local environment run:
    python3 -m venv env

# To activate:
    source env/bin/activate

# Then:
    pip install -r requirements.txt

# To deactivate the local environment:
    deactivate

## Configuration

Before running the application, you need to configure the application with your Spotify credentials and other settings. 

### Steps:

1. Create a new file in the root directory of the project and name it `tokens.env`.
2. Open the `tokens.env` file in a text editor.
3. Add the following lines to the file, replacing `<...>` with your actual values (without the `<` and `>` brackets):

```
dotenv
SPOTIPY_CLIENT_ID=<Your Spotify Client ID>
SPOTIPY_CLIENT_SECRET=<Your Spotify Client Secret>
USER=<Your user name>
USERNAME=<Your Spotify username>
CURRENT_PLAYLIST=<Your Spotify playlist ID>
```

4. Save and close the tokens.env file.
