#!/usr/bin/env python

import requests

from credentials import CLIENT_ID, CLIENT_SECRET

AUTH_URL = 'https://accounts.spotify.com/api/token'
API_URL = 'https://api.spotify.com/v1/'

GET_ALBUM_URL = API_URL + 'albums/{id}'

# Send POST request to receive access_token from Spotify
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# Response is in JSON format, so we use .json() method to parse it to dict
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

# We have to create custom headers with authorization
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Get album information
album_response = requests.get(
    GET_ALBUM_URL.format(id='2LQ52yDk9Ey7qBrq4XSo8W'),
    headers=headers,
)

# Parse JSON data to dict
album_response_data = album_response.json()

# Get all artists names
artists = [artist['name'] for artist in album_response_data['artists']]

# Get tracks information (CD number, track number and title)
tracks = [
    'CD {cd_id}: {track_id} - {title}'.format(
        cd_id=track['disc_number'],
        track_id=track['track_number'],
        title=track['name'],
    ) for track in album_response_data['tracks']['items']
]

# Print 'em all!
print('Album name: ', album_response_data['name'])
print('Artists: ', artists)
print('Tracks: ', tracks)
