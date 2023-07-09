import os
import requests

URL = 'http://localhost:5000/add'


def add():
    """
    Adds several songs at a time. Depends on the API running
    and a `songs` directory being populated with MP3 files.
    """
    songs = os.path.join(os.getcwd(), 'songs')

    for filename in os.listdir(songs):
        path = os.path.join(songs, filename)

        if filename.endswith('.mp3'):
            with open(path, 'rb') as f:
                files = {'file': f}
                response = requests.post(URL, files=files)

            if response.status_code != 200:
                print(f'Failed to upload song (response status {response.status_code}).')


if __name__ == '__main__':
    add()
