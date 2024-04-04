import openai
import json
import os


class PlayListGenerator:

    SAMPLE_RESPONSE_JSON = """
    [ 
        {"song": "Everybody Hurts", "artist": "R.E.M."},
        {"song": "Nothing Compares 2 U", "artist": "Sinead O'Connor"},
        {"song": "Tears in Heaven", "artist": "Eric Clapton"},
        {"song": "Hurt", "artist": "Johnny Cash"},
        {"song": "Yesterday", "artist": "The Beatles"}
    ]
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_playlist(self, prompt, count=8):
        messages = [
            {
                "role": "system",
                "content": """
                You are a helpful playlist generating assistant. 
                You should generate a list of songs and their artists according to a text prompt.
                Your should return a JSON array, where each element follows this format: {"song": <song_title>, "artist": <artist_name>}""",
            },
            {
                "role": "user",
                "content": "Generate a playlist of 5 songs based on this prompt: super super sad songs. Future playlist name will be: sad songs and you don't need to handle with the playlist name",
            },
            {"role": "assistant", "content": PlayListGenerator.SAMPLE_RESPONSE_JSON},
            {
                "role": "user",
                "content": f"Generate a playlist of {count} songs based on this prompt: {prompt}.",
            },
        ]

        response = openai.chat.completions.create(
            messages=messages, model="gpt-4", max_tokens=400
        )

        playlist = json.loads(response.choices[0].message.content)
        return playlist
