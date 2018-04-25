# Spotify Web API Tutorial

## Installation
```
cd <project_dir>
```
### Create virtualenv spotify
```
virtualenv spotify -p python3
source spotify/bin/active
```
### Install requirements (having active virtualenv)
```
pip install -r requirements.txt
```

### Add credentials
In main directory create file credentials.py with two string constants: CLIENT_ID and CLIENT_SECRET. They should contain your client id and client secret obtained from https://developer.spotify.com/my-applications/

## Run app
### Activate virtualenv
```
cd <project_dir>
source spotify/bin/active
```
### Run application
```
./main.py
```
