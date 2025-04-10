function showWordDetails(data) {
    const content = document.getElementById('content');
    if (data.error) {
        content.innerHTML = `<p>${data.error}</p>`;
    } else {
        content.innerHTML = `
            <h3>${data.word}</h3>
            <p><strong>Meaning:</strong> ${data.meaning}</p>
            <p><strong>Synonyms:</strong> ${
                data.synonyms.length > 0 
                ? data.synonyms.map(s => `${s.word} (${s.example})`).join(', ') 
                : "None available"
            }</p>
            <p><strong>Antonyms:</strong> ${
                data.antonyms.length > 0 
                ? data.antonyms.map(a => `${a.word} (${a.example})`).join(', ') 
                : "None available"
            }</p>
            <p><strong>Usage:</strong> ${data.usage}</p>
            <button onclick="playAudio('${data.word}')">Play Audio</button>
            <button onclick="learnMore('${data.word}')">Learn More</button>
            <button onclick="bookmark('${data.word}')">Bookmark</button>
        `;
    }
}

function playAudio(word) {
    alert(`Playing audio for ${word}`); // Placeholder
}

function learnMore(word) {
    window.open(`https://www.merriam-webster.com/dictionary/${word}`, '_blank');
}

async function bookmark(word) {
    const response = await fetch('/bookmark', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
    });
    const result = await response.json();
    alert(result.message);
}