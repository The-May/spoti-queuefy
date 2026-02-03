<img width="200" height="200" alt="SQ" src="https://github.com/user-attachments/assets/dd0a5a9d-a8ff-48b9-a42d-df90f9be4ff7" />

# Spoti-Queuefy

This app exists because some people are too impatient, too drunk, or just think their song is more important than everyone else’s. Instead of letting them skip the line and ruin the current track, this interface forces songs to be added to the queue in order. Everyone gets a turn, and the music keeps playing without chaos.

In short: add your songs, be patient, enjoy the music. Your ego can wait.

---
## Disclaimer:

This project should not be used with open ports on WAN and just be used for private parties!
**Use only in your private LAN.**
This project is not hardened at all, hat no pentests at all and I dont intend to harden it further.
I was tired of disruptive guests and no good/real solution seemed to exist for this.

## Features

- Simple web interface to **search Spotify** and **add songs to the queue**
<img width="928" height="258" alt="image" src="https://github.com/user-attachments/assets/a3ff9113-b9cf-42a2-a19b-c396b41a611c" />

- Shows **Now Playing** and the **next 5 queued songs**  
<img width="628" height="483" alt="image" src="https://github.com/user-attachments/assets/9e4b791e-b97a-43ed-aaa3-d8c62e0b6855" />

- Prevents skipping or interrupting the current song  
- Works on **tablets, desktops, and LAN devices**  
- Configurable **IP whitelist** to limit access  

---

## Prereq
- Constant Internet Access to the Spotify API
- Spotify Premium (Free does not allow dev account/api access iirc)
- create dev app in https://developer.spotify.com/dashboard (in case Spotify does not allow -> reach out to them and not to me) -> See also: https://community.spotify.com/t5/Spotify-for-Developers/Unable-to-create-app/m-p/7300324#M19538
- create client ID + secret, App name + description: queuefy (or something else what makes it easy to identify for what it is used for), redirect URL http://127.0.0.1:8888/callback and API Uses: Web API -> Save

<img width="658" height="543" alt="image" src="https://github.com/user-attachments/assets/14a7b93c-697a-4f16-8345-675804778e6b" />


## Setup locally

1. Clone the repository:


```
git clone https://github.com/The-May/spoti-queuefy.git
cd spoti-queuefy
```

2. Create a virtual environment:

```
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux / macOS
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Copy example.env to .env and edit with your Spotify credentials:

```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://127.0.0.1:5000/callback
ALLOWED_IPS=all
HOST=0.0.0.0
PORT=5000
DEBUG=False
```
5. Run the app:
    
```
python app.py
```




## Setup with HA 
- currently not available/ready

## Setup with docker(compose)
- currently not available/ready
