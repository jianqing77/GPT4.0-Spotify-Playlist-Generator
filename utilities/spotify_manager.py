import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class SpotifyManager:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri="http://localhost:9999",
                scope="playlist-modify-private",
            )
        )
        self.current_user = None
        self._initialize_user()

    def _initialize_user(self):
        try:
            self.current_user = self.sp.current_user()
        except spotipy.SpotifyException as e:
            print(f"An error occurred while retrieving the current Spotify user: {e}")

    def perform_user_action(self):
        if self.current_user is None:
            raise Exception(
                "Current user must be set before performing any user actions."
            )

    def add_songs_to_spotify(self, playlist_name, playlist):
        # Ensure that the user is initialized before adding songs
        self.perform_user_action()
        track_uris = []
        for item in playlist:
            artist, song = item["artist"], item["song"]

            advanced_query = f"artist:({artist} track:({song}))"
            basic_query = f"{song} {artist}"

            for query in [advanced_query, basic_query]:
                log.debug(f"Searching for query: {query}")
                search_results = self.sp.search(q=query, limit=10, type="track")
                # If no items or the top track is not popular enough, skip to the next query
                if (
                    not search_results["tracks"]["items"]
                    or search_results["tracks"]["items"][0]["popularity"] < 20
                ):
                    continue
                else:
                    # Found a good enough track, add its URI to the list and break out of the loop
                    good_guess = search_results["tracks"]["items"][0]
                    print(f"Found: {good_guess['name']} [{good_guess['id']}]")
                    track_uris.append(good_guess["id"])
                    break

        created_playlist = self.sp.user_playlist_create(
            self.current_user["id"],
            public=False,
            name=f"{playlist_name}",
        )

        self.sp.user_playlist_add_tracks(
            self.current_user["id"], created_playlist["id"], track_uris
        )

        print("\n")
        print(f"Created playlist: {created_playlist['name']}")
        print(created_playlist["external_urls"]["spotify"])
