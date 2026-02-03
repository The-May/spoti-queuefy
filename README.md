# Spoti-Queuefy

This app exists because some people are too impatient, too drunk, or just think their song is more important than everyone else’s. Instead of letting them skip the line and ruin the current track, this interface forces songs to be added to the queue in order. Everyone gets a turn, and the music keeps playing without chaos.

In short: add your songs, be patient, enjoy the music. Your ego can wait.

---

## Features

- Simple web interface to **search Spotify** and **add songs to the queue**  
- Shows **Now Playing** and the **next 5 queued songs**  
- Prevents skipping or interrupting the current song  
- Works on **tablets, desktops, and LAN devices**  
- Configurable **IP whitelist** to limit access  

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/The-May/spoti-queuefy.git
cd spoti-queuefy

    Create a virtual environment:

python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux / macOS

    Install dependencies:

pip install -r requirements.txt

    Copy example.env to .env and edit with your Spotify credentials:

SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://127.0.0.1:5000/callback
ALLOWED_IPS=all
HOST=0.0.0.0
PORT=5000
DEBUG=False

    Run the app:

python app.py
