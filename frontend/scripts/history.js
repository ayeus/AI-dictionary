async function showHistory() {
    const response = await fetch('/history');
    const history = await response.json();
    document.getElementById('content').innerHTML = history.map(h => `<p>${h.word} - ${h.timestamp}</p>`).join('');
}