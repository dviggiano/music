from flask import Flask, request, render_template

from src import Recommender

app = Flask(__name__)
recommender = Recommender()


@app.route('/add', methods=['POST'])
def add_song():
    song = request.get_json()
    # TODO recommender.add(song)
    return f"{song['title']} added to library!"


@app.route('/listen', methods=['POST'])
def listen_to_song():
    session = request.get_json()
    # TODO record listening session in user data
    return f"{session['user']} listened to {session['song']} from {session['start']} to {session['end']}!"


@app.route('/recommend', methods=['GET'])
def recommend():
    params = request.get_json()
    # TODO recommender.recommend(params)
    return f"This route will provide a set of recommendations for {params['user']}."


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
