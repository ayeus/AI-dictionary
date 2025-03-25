async function showRecap() {
    const response = await fetch('/progress');
    const data = await response.json();
    document.getElementById('content').innerHTML = `
        <h3>Weekly Recap</h3>
        <p>Words Learned: ${data.words.join(', ')}</p>
    `;
}