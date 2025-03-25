function showWordDetails(data) {
    const content = document.getElementById('content');
    if (data.error) {
        content.innerHTML = `<p>${data.error}</p>`;
    } else {
        content.innerHTML = `
            <h3>${data.word}</h3>
            <p><strong>Meaning:</strong> ${data.meaning}</p>
            <p><strong>Synonyms:</strong> ${data.synonyms.map(s => `${s.word} (${s.example})`).join(', ')}</p>
            <p><strong>Antonyms:</strong> ${data.antonyms.map(a => `${a.word} (${a.example})`).join(', ')}</p>
            <p><strong>Usage:</strong> ${data.usage}</p>
            <button onclick="playAudio('${data.word}')">Play Audio</button>
            <button onclick="learnMore('${data.word}')">Learn More</button>
            <button onclick="bookmark('${data.word}')">Bookmark</button>
        `;
    }
}

function playAudio(word) {
    // Placeholder: In production, fetch real audio
    alert(`Playing audio for ${word}`);
}

function learnMore(word) {
    window.open(`https://www.merriam-webster.com/dictionary/${word}`, '_blank');
}

async function bookmark(word) {
    await fetch('/bookmark', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
    });
    alert(`${word} bookmarked!`);
}