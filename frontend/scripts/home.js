async function searchWord() {
    const word = document.getElementById('word-input').value;
    const response = await fetch('/search_word', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
    });
    const data = await response.json();
    showWordDetails(data);
    notify(`New word searched: ${word}`);
}

function showTab(tab) {
    const content = document.getElementById('content');
    content.innerHTML = '';
    if (tab === 'daily') fetchDailyWord();
    else if (tab === 'categories') showCategories();
    else if (tab === 'quiz') showQuizOptions();
    else if (tab === 'recap') showRecap();
    else if (tab === 'history') showHistory();
    else if (tab === 'profile') showProfile();
}

async function fetchDailyWord() {
    const response = await fetch('/daily_word');
    const data = await response.json();
    showWordDetails(data);
    notify("Here's your daily word!");
}

function notify(message) {
    if (Notification.permission === "granted") {
        new Notification(message);
    } else if (Notification.permission !== "denied") {
        Notification.requestPermission().then(permission => {
            if (permission === "granted") new Notification(message);
        });
    }
}