import requests
from flask import Flask, request, make_response, render_template, redirect, url_for, jsonify
from flask_cors import CORS
import json
import logging

app = Flask(__name__)
CORS(app)

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

canView = True
canPlay = True

myCode = ""

@app.route("/nowPlaying")
def generateNowPlaying():
    loadOptions()
    if not canView:
        sendDict = {
            "song": "Service Currently Disabled",
            "artist": " ",
            "albumArt": "https://via.placeholder.com/300.png"
        }
        return jsonify(sendDict)
    try:
        sendDict = {
            "song": "n/a",
            "artist": "n/a",
            "albumArt": "n/a"
        }
        r = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers={"Authorization": myCode})
        respJson = r.json()["item"]
        sendDict["song"] = respJson["name"]
        sendDict["artist"] = respJson["artists"][0]["name"]
        sendDict["albumArt"] = respJson["album"]["images"][1]["url"]
        return jsonify(sendDict)
    except:
        sendDict = {
            "song": "Service Currently Disabled",
            "artist": " ",
            "albumArt": "https://via.placeholder.com/300.png"
        }
        return jsonify(sendDict)

@app.route("/playSong")
def setSong():
    loadOptions()
    if not canPlay or not canView:
        return jsonify({"status": "500"})
    try:
        songTitle = request.args.get("title")
        requestParams = {
            "q": songTitle,
            "type": "track"
        }
        r = requests.get("https://api.spotify.com/v1/search", headers={"Authorization": myCode}, params=requestParams)
        respJson = r.json()
        trackURI = respJson["tracks"]["items"][0]["uri"]
        songDict = {
            "uris": [trackURI]
        }
        playSong = requests.put("https://api.spotify.com/v1/me/player/play",headers={"Authorization": myCode}, json=songDict)
        print(playSong.text)
        return jsonify({"status": "200"})
    except:
        return jsonify({"status": "500"})

@app.route("/authenticateUser")
def authenticate():
    try:
        global myCode
        print(request.args)
        authCode = request.args.get("code")
        parameters = {"grant_type": "authorization_code", "code": authCode, "redirect_uri": "URLHERE/authenticateUser",
                      "client_id": "", "client_secret": ""}
        r = requests.post("https://accounts.spotify.com/api/token", data=parameters)
        print(r.text)
        accessCode = r.json()["access_token"]
        with open("control.json", "r") as read_file:
            data = json.load(read_file)
        data["auth"] = accessCode
        with open("control.json", "w") as write_file:
            json.dump(data, write_file)
        loadOptions()
        return jsonify({"status": "200"})
    except:
        return jsonify({"status": "500"})

def loadOptions():
    global canPlay
    global canView
    global myCode
    with open("control.json", "r") as read_file:
        data = json.load(read_file)
    canPlay = data["canPlay"]
    canView = data["canView"]
    myCode = str("Bearer " + data["auth"])

loadOptions()

if __name__ == "__main__":  # starts the whole program
    print("started")
    app.run(host='0.0.0.0', port=5001)