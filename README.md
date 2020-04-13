
# SpotifyControl
Allows for public crowdsourcing of music to play on Spotify
This project utilizes the following resources to be possible:

 - Official Spotify Developer API
 - Python (Flask)
 - HTML/CSS/JS

## Usage
### Setup
Please create a spotify developer account and application. The instructions to do so can be found on [the spotify developer quickstart page](https://developer.spotify.com/documentation/web-api/quick-start/).

From there, decide on a URL for your application. You must pick a callback URL to use, which needs to be entered both within your app on the spotify dashboard and within the redirect_uri key of the parameters within the authenticate function. Follow the steps on the Spotify oAuth page to generate an API authentication link.

### Backend Resources

Within the main.py file, the parameters within the authenticate function must be filled in. 
The **grant type** can remain the same as provided, however, your **redirect_uri** must match both the URL of that endpoint, the URL provided in the spotify dashboard, and the URL provided in the API authentication link. Without this, Spotify will return an error such as "wrong format" or "invalid API key". 
The **client_id** and **client_secret** must be copied and pasted from the spotify dashboard into their respective locations.
Once this is all configured, run your main.py using something such as gunicorn.

### Frontend Resources

These can be hosted statically, as long as the URLs within the apiAcess.js file are pointed at the correct URL for the backend Flask server.

