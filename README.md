# SpotifyAutoAdd
Script that adds current song to chosen playlist

## Configuration

Before running the application, you need to configure the application with your Spotify credentials and other settings. 

### Steps:

1. Create a new file in the root directory and name it `tokens.env`.
2. Open the `tokens.env` file in a text editor.
3. Add the following lines to the file, replacing `<...>` with your actual values (without the `<` and `>` brackets):

```
SPOTIPY_CLIENT_ID=<Your Spotify Client ID>
SPOTIPY_CLIENT_SECRET=<Your Spotify Client Secret>
USER=<Your user ID>
USERNAME=<Your Spotify username>
CURRENT_PLAYLIST=<Your Spotify playlist ID>
```

4. Save and close the tokens.env file.

### To create a new python local environment run:
    python3 -m venv env

### To activate:
    source env/bin/activate

### Then:
    pip install -r requirements.txt

### To deactivate the local environment:
    deactivate

### Running the Application with Apple Script

This guide assumes that you're using macOS. If you're using a different operating system, these instructions may not apply. 

In macOS, you can use Apple Script to automate running this application. This allows you to easily run the application without needing to manually open a Terminal and enter commands.

Here are the steps to create an Apple Script that runs this application:

1. Open the "Script Editor" application. You can do this by opening Spotlight Search (pressing `Command` + `Space`) and typing "Script Editor".

2. Once the Script Editor is open, click on "New Document".

3. Copy and paste the following script into the new document:

   ```
   applescript
   tell application "Terminal"
       launch
       do script "<path to script>"
       delay 5
   end tell

   tell application "Terminal" to close (get window 1)
   ```

Replace <path to script> with the absolute path to the run.py file in the project directory. For example, if the project is in your home directory, the path might be /Users/YourUserName/YourProjectFolder/run.py.

After pasting the script and replacing <path to script>, go to the "File" menu and click on "Save". Give your script a name and save it.

You've now created an Apple Script to run the application. To run the application, simply double-click the saved script file. You can also pin scripts to the menu bar for easy access.

