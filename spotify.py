import json
import spotipy
from selenium import webdriver 
import time
import webbrowser
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key

username = 'kevinwong973'
clientID = 'b53d4283df5c4b4687b9fc971ea9ac11'
clientSecret = 'a9ef299f57dc4f30a088c8e1b2b473dc'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))

while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    print("2 - Previous Track")
    print("3 - Next Track")
    print("4 - Play/Pause Song")
    print("5 - Volume Down")
    print("6 - Volume Up")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        pyautogui.moveTo(599, 676, 3)
        time.sleep(2)
        pyautogui.press("prevtrack")
        time.sleep(1)
        pyautogui.leftClick()
        print("Now playing " + search_song)

        #pyautogui.press("playpause")
        print('Song has opened in your browser.')
    elif user_input == 2:
        pyautogui.press("prevtrack")
    elif user_input == 3:
        pyautogui.press("nexttrack")
    elif user_input == 4:
        pyautogui.press("playpause")

    elif user_input == 0:
        #pyautogui.hotkey('ctrl', 'w')
        #pyautogui.keyDown('ctrl')
        #pyautogui.keyDown('w')
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")