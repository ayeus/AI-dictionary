async function showCategories() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <button onclick="fetchCategory('easy')">Easy</button>
        <button onclick="fetchCategory('medium')">Medium</button>
        <button onclick="fetchCategory('hard')">Hard</button>
        <div id="category-words"></div>
    `;
}

async function fetchCategory(level) {
    const response = await fetch(`/categories/${level}`);
    const words = await response.json();
    document.getElementById('category-words').innerHTML = words.map(word => `<p onclick="searchWord('${word}')">${word}</p>`).join('');
}