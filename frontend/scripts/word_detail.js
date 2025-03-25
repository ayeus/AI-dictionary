function showWordDetails(data) {
    const content = document.getElementById('content');
    if (data.error) {
        content.innerHTML = `<p>${data.error}</p>`;
    } else {
        content.innerHTML = `
            <h3>${data.word}</h3>
            <p><strong>Meaning:</strong> ${data.meaning}</p>
            <p><strong>Synonyms:</strong> ${data.synonyms.join(', ')}</p>
            <p><strong>Antonyms:</strong> ${data.antonyms.join(', ')}</p>
            <p><strong>Usage:</strong> ${data.usage}</p>
            <button onclick="alert('Audio placeholder')">Play Audio</button>
        `;
    }
}