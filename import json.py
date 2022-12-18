import json

import spotipy
import webbrowser

#curl -X "GET" "https://api.spotify.com/v1/playlists/" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "
  
SPOTIPY_USERNAME = '31mitlf4wlvrchodybnocrejvfba'
SPOTIPY_CLIENT_ID = 'e4200ab456fe497d94bd17721aea83b2'
SPOTIPY_CLIENT_SECRET = '7e7da44c308642a9a3296e12ae7a966e'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
oauth_object = spotipy.SpotifyOAuth(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed
print(json.dumps(user_name, sort_keys=True, indent=4))
  
while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0,"playlist")
        songs_dict = results['playlists']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        player=RandomPlayer(random_song_schema='word')
        player.authenticate()
        player.playRandomSong(numSongs=10)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("hii")
        #GET "https://api.spotify.com/v1/playlists/1XPc8HtISFFdyjdj2LJ37z"
        