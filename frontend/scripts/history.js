async function showHistory() {
    const response = await fetch('/history');
    const history = await response.json();
    const content = document.getElementById('content');
    content.innerHTML = `
        <h3>History</h3>
        <p>Words: ${history.words.map(w => `${w.word} (${w.timestamp})`).join(', ')}</p>
        <p>Quizzes: ${history.quizzes.join(', ') || 'None'}</p>
        <p>Activities: ${history.activities.join(', ') || 'None'}</p>
    `;
}