# Spotify-Python-Programs-Using-Spotipy

This repository contains two Python 3 scripts.

"cursor_position.py" is a script that allows a user to see the exact coordinates of their mouse cursor until they press 'ctrl' + 'c' to exit the script.

"spotify.py" is a script that interacts with the Spotify API and provides a simple console-based interface for controlling Spotify playback and performing basic actions. Here is a description of the code:

Imports: The code begins by importing necessary libraries such as json for JSON manipulation, spotipy for interfacing with the Spotify API, selenium for web automation, time for time-related functions, webbrowser for opening URLs in the default web browser, pyautogui for simulating keyboard and mouse actions, and pynput for handling keyboard input.

Spotify API Credentials: It defines the username, clientID, clientSecret, and redirect_uri required for authentication with the Spotify API.

Authentication: The script uses the spotipy.SpotifyOAuth class to obtain an access token for the authenticated user.

Console Interaction: It enters a while loop to create a basic console interface where the user can interact with their Spotify account. It prints the user's display name obtained from the Spotify API.

Menu Options: The code presents the following menu options to the user:

0: Exit the console
1: Search for a Song
2: Previous Track
3: Next Track
4: Play/Pause Song
5: Volume Down
6: Volume Up

User Input: The script prompts the user to enter their choice (0-6) and processes the input accordingly.

Song Search (Option 1): If the user chooses to search for a song, the script takes a song name as input, searches for it using the Spotify API, and opens the song's URL in the default web browser. It also simulates a mouse action to control playback if the screen is maximized so the user need not touch their own mouse.

Playback Control (Options 2-4): Options 2 to 4 correspond to controlling playback with options for previous track, next track, and play/pause.

Exit (Option 0): If the user chooses to exit, the script prints a goodbye message and breaks out of the loop.

Error Handling: It provides a message for invalid user input.

This script effectively acts as a basic Spotify controller, allowing the user to search for and play songs, control playback, and exit the console. It uses a combination of the Spotify API and simulated user interactions to achieve these actions.
