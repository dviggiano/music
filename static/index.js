async function reset() {
    const userSelector = document.getElementById('user');
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

document.getElementById('add').addEventListener('submit', () => {

});

document.getElementById('listen').addEventListener('submit', () => {

});

document.getElementById('recommend').addEventListener('submit', () => {

});