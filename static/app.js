document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', handleFormSubmit);
});

function handleFormSubmit(event) {
    event.preventDefault();
    const playlistData = getPlaylistFormData();
    print(playlistData);
    postPlaylistData(playlistData).then(handleResponse).catch(handleError);
}

function getPlaylistFormData() {
    const playlistName = document.querySelector('#playlist-name').value;
    const playlistPrompt = document.querySelector('#playlist-prompt').value;
    const playlistCount = document.querySelector('#count').value;
    return {
        playlist_name: playlistName,
        playlist_prompt: playlistPrompt,
        count: playlistCount,
    };
}

function postPlaylistData(data) {
    return fetch('/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
}

function handleResponse(response) {
    if (!response.ok) {
        return response.json().then((json) => Promise.reject(json));
    }
    return response.json().then((data) => {
        displaySuccessMessage(data);
    });
}

function handleError(error) {
    displayErrorMessage(error);
}

function displaySuccessMessage(data) {
    console.log('Success:', data);
}

function displayErrorMessage(error) {
    console.error('Error:', error);
}
