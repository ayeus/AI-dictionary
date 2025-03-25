async function showCategories() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h3>Categories</h3>
        <button onclick="fetchCategory('easy')">Easy</button>
        <button onclick="fetchCategory('medium')">Medium</button>
        <button onclick="fetchCategory('hard')">Hard</button>
        <div id="category-words"></div>
    `;
}

async function fetchCategory(level) {
    const response = await fetch(`/categories/${level}`);
    const words = await response.json();
    document.getElementById('category-words').innerHTML = words.map(word => `
        <p onclick="searchWordSpecific('${word}')">${word}</p>
    `).join('');
}

async function searchWordSpecific(word) {
    const response = await fetch('/search_word', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
    });
    const data = await response.json();
    showWordDetails(data);
}