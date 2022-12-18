 #Import webbrowser module in the program 
import random
def getRandomSearch:
  // A list of all characters that can be chosen.
  const characters = 'abcdefghijklmnopqrstuvwxyz';
  
  // Gets a random character from the characters string.
  const randomCharacter = characters.charAt(Math.floor(Math.random() * characters.length));
  let randomSearch = '';

  // Places the wildcard character at the beginning, or both beginning and end, randomly.
  switch (Math.round(Math.random())) {
    case 0:
      randomSearch = randomCharacter + '%';
      break;
    case 1:
      randomSearch = '%' + randomCharacter + '%';
      break;
  

  return randomSearch;

const randomOffset = Math.floor(Math.random() * 10000);

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='e4200ab456fe497d94bd17721aea83b2',client_secret='7e7da44c308642a9a3296e12ae7a966e'))

import webbrowser  
emotion=input("how are you ")
emotion.lower()
if(emotion=="neutral"):
    url= 'https://open.spotify.com/playlist/7EClwmhqu7mg4JvUI9z5DT?si=e880baf124f8446d'
    GET https://api.spotify.com/v1/url
    type=track
    q=getRandomSearch()
    offset=randomOffset  
    webbrowser.open_new_tab(url)
elif(emotion=="joy"):
    url= 'https://open.spotify.com/playlist/79E7FTe1BxDLTioXfDPGch?si=1c9ba013a7fa4e91'  
    webbrowser.open_new_tab(url)
elif(emotion=="sadness"):
    url= 'https://open.spotify.com/playlist/4YOfhHpjPB0tq29NPpDY3F?si=1d69d3f04c19499e'  
    webbrowser.open_new_tab(url)
elif(emotion=="fear"):
    url= 'https://open.spotify.com/playlist/2KANDdP7pkyXR1fatEXkA6?si=59b3a06294c2425e'  
    webbrowser.open_new_tab(url)
elif(emotion=="surprise"):
    url= 'https://open.spotify.com/playlist/4o5SxWNsTNLOi9ahHeJF8A?si=592b39fff6344df5'  
    webbrowser.open_new_tab(url)
elif(emotion=="anger"):
    url= 'https://open.spotify.com/playlist/4VcB1Z6mYDWf9QQHbn2LPe?si=02b2eae8d90e4aea'  
    webbrowser.open_new_tab(url)
elif(emotion=="shame"):
    url= 'https://open.spotify.com/playlist/2QbD03tA7gJm6aySITfn1U?si=943484ace16f4fd0'  
    webbrowser.open_new_tab(url)
elif(emotion=="disgust"):
    url= 'https://open.spotify.com/playlist/1DSLdUwgNnNroGrxnUxVv4?si=a713ac238d9945d2'  
    webbrowser.open_new_tab(url)
else:
    print("dont you have any emotion?")


