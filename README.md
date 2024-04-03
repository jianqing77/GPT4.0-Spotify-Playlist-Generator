# GPT4.0-Spotify-Playlist-Generator

Welcome to the GPT4.0-Spotify-Playlist-Generator, where your words shape the soundtrack of your life! 🎵✨

This innovative project harnesses the power of OpenAI's GPT-4 to interpret your musical desires and the Spotify API to create a playlist that resonates with your mood, activity, or any theme you express in plain text. Get ready to elevate your music experience with playlists that are personalized just for you, and seamlessly integrated into your Spotify account.

## Features

-   **Personalized Playlists**: Generate custom playlists based on your input descriptions.
-   **GPT-4 Integration**: Utilize the latest in AI language models to understand and interpret your requests.
-   **Spotify API Connection**: Create and sync playlists directly to your Spotify account.
-   **User-Friendly Interface**: Simple and intuitive design for ease of use.

## Getting Started

To get started with the GPT4.0-Spotify-Playlist-Generator, follow these steps:

### Prerequisites

Ensure you have the following prerequisites installed and set up:

-   Python 3.6 or higher
-   pip (Python package installer)
-   Virtualenv (optional but recommended for package management)
-   A Spotify Developer account and a registered application

### Installation

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/yourusername/GPT4.0-Spotify-Playlist-Generator.git
    cd GPT4.0-Spotify-Playlist-Generator
    ```

2. Set up a virtual environment (optional):

    ```shell
    python -m venv env
    source env/bin/activate  # For Unix or MacOS
    env\Scripts\activate  # For Windows
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory with your Spotify credentials and OpenAI API key:

    ```plaintext
    SPOTIFY_CLIENT_ID='your_spotify_client_id'
    SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
    OPENAI_API_KEY='your_openai_api_key'
    ```

### Usage

To use the Playlist Generator, run the main script (ensure your virtual environment is activated if you're using one):

```shell
python app.py
```
