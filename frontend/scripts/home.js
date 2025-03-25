async function searchWord() {
    const word = document.getElementById('word-input').value;
    const response = await fetch('/search_word', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
    });
    const data = await response.json();
    showWordDetails(data);
}

function showTab(tab) {
    const content = document.getElementById('content');
    content.innerHTML = '';
    if (tab === 'daily') fetchDailyWord();
    if (tab === 'categories') showCategories();
    if (tab === 'quiz') startQuiz();
    if (tab === 'recap') showRecap();
    if (tab === 'history') showHistory();
    if (tab === 'profile') showProfile();
}

async function fetchDailyWord() {
    const response = await fetch('/daily_word');
    const data = await response.json();
    showWordDetails(data);
}