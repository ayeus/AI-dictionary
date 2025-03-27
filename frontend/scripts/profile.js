async function showProfile() {
    const progressResponse = await fetch('/progress');
    const data = await progressResponse.json();
    const bookmarksResponse = await fetch('/bookmarks');
    const bookmarks = await bookmarksResponse.json();
    const content = document.getElementById('content');
    content.innerHTML = `
        <h3>Profile</h3>
        <p>Total Words Learned: ${data.words.length}</p>
        <p>Scores: ${data.scores.join(', ') || 'None'}</p>
        <p>Bookmarks: ${bookmarks.join(', ') || 'None'}</p>
        <button onclick="exportProgress()">Export Progress</button>
    `;
}

function exportProgress() {
    window.location.href = '/export_progress';
}