document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', handleFormSubmit);
    const cancelButton = document.querySelector('#cancel-btn');
    cancelButton.addEventListener('click', clearFormInputs);
});

function handleFormSubmit(event) {
    event.preventDefault();
    displayLoadingMessage(); // Display loading message
    const playlistData = getPlaylistFormData();
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

function clearFormInputs() {
    document.querySelector('#playlist-name').value = '';
    document.querySelector('#playlist-prompt').value = '';
    document.querySelector('#count').value = '';

    const messageContainer = document.querySelector('#message-container');
    messageContainer.textContent = '';
    messageContainer.className = 'hidden';
}

function displaySuccessMessage(data) {
    const messageContainer = document.querySelector('#message-container');
    messageContainer.textContent = 'Success: ' + data.message; // Assuming 'message' is a key in your response
    messageContainer.className =
        'block p-4 mb-4 text-lg text-center font-medium text-green-500'; // Show with success styling
    setTimeout(() => (messageContainer.className = 'hidden'), 5000); // Hide the message after 5 seconds
}

function displayErrorMessage(error) {
    const messageContainer = document.querySelector('#message-container');
    messageContainer.textContent = 'Error: ' + error.message; // Assuming 'message' is a key in your error object
    messageContainer.className =
        'block p-4 mb-4 text-sm text-center font-medium text-red-500'; // Show with error styling
    setTimeout(() => (messageContainer.className = 'hidden'), 5000); // Hide the message after 5 seconds
}

function displayLoadingMessage() {
    const messageContainer = document.querySelector('#message-container');
    messageContainer.textContent = 'Loading...';
    messageContainer.className =
        'block p-4 mb-4 text-sm text-center font-medium text-blue-500';
}
