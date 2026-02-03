import os
import sys
from flask import Flask, request, redirect, url_for, abort, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Spotipy / App configuration from environment variables
required_vars = ["ALLOWED_IPS", "HOST", "PORT", "DEBUG"]
config = {}

#Precheck for required environment variables: issue error and exit if any vars missing and/or empty
for var in required_vars:
    value = os.environ.get(var)
    if not value:  # None or empty string
        print(f"Missing or empty required environment variable: {var}")
        print("Please set all required variables in your .env file or environment. Please read the docs for more info.")
        sys.exit(1)
    config[var] = value

# Assign properly
ALLOWED_IPS = config["ALLOWED_IPS"]
HOST = config["HOST"]
PORT = int(config["PORT"])
DEBUG = config["DEBUG"].lower() == "true"


app = Flask(__name__)

# Spotify setup
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-read-playback-state user-modify-playback-state",
#        cache_path=".spotify_cache"  # defaults to .cache
    )
)


@app.before_request
def limit_remote_addr():
    # Allow all if set to "all"
    if ALLOWED_IPS.strip().lower() == "all":
        return

    # Split the string into a list of IPs and strip spaces
    allowed = [ip.strip() for ip in ALLOWED_IPS.split(",")]

    # If the client's IP is not in the list, block
    if request.remote_addr not in allowed:
        abort(403)  # Forbidden


@app.route("/")
def index():
    playback = sp.current_playback()
    queue_data = sp.queue()

    current = None
    if playback and playback.get("item"):
        item = playback["item"]
        current = {
            "name": item["name"],
            "artist": ", ".join(a["name"] for a in item["artists"]),
            "cover": item["album"]["images"][0]["url"]
        }

    queue = []
    for t in queue_data.get("queue", [])[:5]:
        queue.append({
            "name": t["name"],
            "artist": ", ".join(a["name"] for a in t["artists"]),
            "cover": t["album"]["images"][0]["url"]
        })

    return render_template(
        "index.html",
        current=current,
        queue=queue
    )


@app.route("/search")
def search():
    q = request.args.get("q")
    results = []

    if q:
        data = sp.search(q, limit=10, type="track")
        for t in data["tracks"]["items"]:
            results.append({
                "name": t["name"],
                "artist": ", ".join(a["name"] for a in t["artists"]),
                "cover": t["album"]["images"][0]["url"],
                "uri": t["uri"]
            })

    return render_template("search.html", results=results)


@app.route("/add", methods=["POST"])
def add():
    uri = request.form["uri"]
    sp.add_to_queue(uri)
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)