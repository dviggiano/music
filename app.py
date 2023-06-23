from flask import Flask, request, jsonify, render_template

from src import Recommender

app = Flask(__name__)
recommender = Recommender()


@app.route('/songs', methods=['GET'])
def songs():
    # TODO return uploaded songs
    return {}


@app.route('/reset', methods=['PATCH'])
def reset():
    # TODO reset user users
    return


@app.route('/add', methods=['POST'])
def add_song():
    song = request.files['file']
    response = recommender.add(song)
    return jsonify(response)


@app.route('/listen', methods=['POST'])
def listen_to_song():
    session = request.get_json()
    # TODO record listening session in user users
    return f"{session['user']} listened to {session['song']} from {session['start']} to {session['end']}!"


@app.route('/recommend', methods=['GET'])
def recommend():
    params = request.get_json()
    # TODO songs = recommender.recommend(params)
    # response = { 'songs': songs }
    # return jsonify(response)
    return f"This route will provide a set of recommendations for {params['user']}."


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
