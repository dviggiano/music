const userSelector = document.getElementById('user');

let songs = false;

function addSong(song) {
    const number = document.getElementById('number');

    if (!songs) {
        songs = true;
        number.min = 1;
        const form = document.getElementById('listen');
        form.style.display = 'block';
        const message = document.getElementById('empty');
        message.style.display = 'none';
    }

    const option = document.createElement('option');
    option.text = `${song.name} (${song.length}s)`;
    option.value = JSON.stringify(song);
    const songSelector = document.getElementById('song');
    songSelector.add(option);
    number.max = Number(number.max) + 1;
}

async function reset() {
    const user = userSelector.value;
    const confirmed = confirm(`Are you sure you want to reset listening history for ${user}?`);

    if (confirmed) {
        const response = await fetch('/reset', {
            method: 'PATCH',
            body: JSON.stringify({ user }),
        });

        alert(
            response.status === 200 ?
            `Reset listening history for ${user}.` :
            `Could not reset listening history for ${user} (response status ${response.status}).`
        );
    }
}

fetch('/songs', { method: 'GET' })
    .then(response => {
        const data = response.json();

        if (data['songs']) {
            data['songs'].forEach(addSong);
        }
    });

document.getElementById('add').addEventListener('submit', async event => {
    event.preventDefault();
    const input = document.getElementById('file-input');
    const file = input.files[0];

    if (file) {
        const data = new FormData();
        data.append('file', file);
        const response = await fetch('/add', {
            method: 'POST',
            body: data,
        });

        if (response.status === 200) {
            const song = response.json();
            addSong(song);
        } else {
            alert(`Failed to upload song (response status ${response.status}).`)
        }
    }
});

document.getElementById('listen').addEventListener('submit', event => {
    event.preventDefault();
});

document.getElementById('recommend').addEventListener('submit', event => {
    event.preventDefault();
});
