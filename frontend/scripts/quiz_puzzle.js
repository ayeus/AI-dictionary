function showQuizOptions() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h3>Quiz/Puzzle</h3>
        <button onclick="startQuiz()">Start Quiz</button>
        <button onclick="startPassage()">Unseen Passage</button>
        <button onclick="startPuzzle()">Puzzle</button>
    `;
}

async function startQuiz() {
    const response = await fetch('/quiz');
    const quiz = await response.json();
    const content = document.getElementById('content');
    content.innerHTML = quiz.map((q, i) => `
        <p>${q.question}</p>
        ${q.options.map(opt => `<input type="radio" name="q${i}" value="${opt}">${opt}<br>`).join('')}
    `).join('<hr>');
}

async function startPassage() {
    const response = await fetch('/passage');
    const data = await response.json();
    const content = document.getElementById('content');
    content.innerHTML = `
        <p>${data.passage}</p>
        ${data.questions.map(q => `<p>${q.question} <input type="text" id="${q.question}"></p>`).join('')}
    `;
}

async function startPuzzle() {
    const response = await fetch('/puzzle');
    const data = await response.json();
    const content = document.getElementById('content');
    content.innerHTML = `<p>Word Search: Find ${data.words.join(', ')}</p>`;
}