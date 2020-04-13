function nowPlaying() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let songInfo = JSON.parse(this.response);
            document.getElementById("songTitle").innerText = songInfo["song"];
            document.getElementById("artist").innerText = "By: ".concat(songInfo["artist"]);
            document.getElementById("albumArt").src = songInfo["albumArt"];
        }
    };
    xhttp.open("GET", "https://spotify.domhupp.space/api/nowPlaying", true);
    xhttp.send();
}

function pickSong() {
    trackName = document.getElementById("trackTitle");
    var sendSong = new XMLHttpRequest();
    sendSong.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let songInfo = JSON.parse(this.response);
            closeModal()
        }
    };
    sendSong.open("GET", "https://spotify.domhupp.space/api/playSong?title=".concat(trackName.value), true);
    sendSong.send();
}