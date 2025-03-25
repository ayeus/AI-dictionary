async function showProfile() {
    const response = await fetch('/progress');
    const data = await response.json();
    document.getElementById('content').innerHTML = `
        <h3>Profile</h3>
        <p>Total Words Learned: ${data.words.length}</p>
        <p>Scores: ${data.scores.join(', ')}</p>
    `;
}