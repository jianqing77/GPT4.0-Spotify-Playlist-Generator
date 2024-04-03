from playlist_generator import PlayListGenerator
from spotify_manager import SpotifyManager
from settings import load_env
import argparse
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Simple command line utility")
    parser.add_argument("-p", type=str, help="The prompt to describe the playlist.")
    parser.add_argument(
        "-n", type=int, default=12, help="The number of songs to be added."
    )
    parser.add_argument(
        "-envfile",
        type=str,
        default=".env",
        required=False,
        help='A dotenv file with your environment variables: "SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "OPENAI_API_KEY"',
    )

    args = parser.parse_args()
    load_env(args.envfile)

    playlist_generator = PlayListGenerator()
    spotify_manager = SpotifyManager()

    playlist_prompt = args.p
    count = args.n

    playlist = playlist_generator.generate_playlist(playlist_prompt, count)
    spotify_manager.add_songs_to_spotify(playlist_prompt, playlist)


if __name__ == "__main__":
    main()
