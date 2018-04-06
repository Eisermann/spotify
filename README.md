# Spotify Web API Tutorial

## Installation

### Create virtualenv spotify
```
virtualenv spotify -p python3
```
### Install requirements (having active virtualenv)
```
pip install -r requirements.txt
```

### Add credentials
In main directory create file credentials.py with two string constants: CLIENT_ID and CLIENT_SECRET. They should contain your client id and client secret obtained from https://developer.spotify.com/my-applications/

## Run app
### If you have not activated virtualenv, make it now :)
```
cd <project_dir>
source spotify/bin/active
```
### Run application
```
./main.py
```
