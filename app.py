from flask import Flask, jsonify, request, render_template
from utilities.playlist_generator import PlayListGenerator
from utilities.spotify_manager import SpotifyManager
from utilities.settings import load_env
import logging


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# load the environment variables
load_env(".env")

# flask setup
app = Flask(
    __name__, template_folder="templates", static_url_path="", static_folder="static"
)

playlist_generator = PlayListGenerator()
spotify_manager = SpotifyManager()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create_playlist():
    content = request.json
    playlist_name = content.get("playlist_name")
    playlist_prompt = content.get("playlist_prompt")
    count = content.get("count")
    print(f"count here: {count}")

    if not playlist_prompt:
        return (
            jsonify({"error": "The prompt to describe the playlist is required."}),
            400,
        )

    try:
        # Generate playlist and add songs to Spotify
        playlist = playlist_generator.generate_playlist(playlist_prompt, count)
        spotify_manager.add_songs_to_spotify(playlist_name, playlist)
        return jsonify({"message": "Playlist created successfully"}), 200
    except Exception as e:
        log.exception("An error occurred while creating the playlist.")
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
