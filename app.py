import csv
from flask import Flask, request, jsonify, render_template

from src import Engine, SONG_LIST_FILENAME

app = Flask(__name__)
engine = Engine()


@app.route('/songs', methods=['GET'])
def get_songs():
    songs = []

    with open(SONG_LIST_FILENAME, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(row)

    return jsonify({'songs': songs})


@app.route('/reset', methods=['PATCH'])
def reset():
    # TODO reset user users
    return


@app.route('/add', methods=['POST'])
def add_song():
    song = request.files['file']
    response = engine.add(song)
    return jsonify(response)


@app.route('/listen', methods=['POST'])
def listen_to_song():
    session = request.get_json()
    # TODO record listening session in user users
    return f"{session['user']} listened to {session['song']} from {session['start']} to {session['end']}!"


@app.route('/recommend', methods=['GET'])
def recommend():
    params = request.get_json()
    # TODO songs = engine.recommend(params)
    # response = { 'songs': songs }
    # return jsonify(response)
    return f"This route will provide a set of recommendations for {params['user']}."


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
