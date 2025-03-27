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
    try {
        const response = await fetch('/quiz');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const quiz = await response.json();
        const content = document.getElementById('content');
        console.log('Quiz data:', quiz); // Debug: Log the response

        // Check if quiz is an array (successful response) or an object (error)
        if (Array.isArray(quiz)) {
            content.innerHTML = '<h3>Quiz</h3>' + quiz.map((q, i) => `
                <div>
                    <p>${q.question}</p>
                    ${q.options.map(opt => `<label><input type="radio" name="q${i}" value="${opt}"> ${opt}</label><br>`).join('')}
                    <p><small>Correct Answer: ${q.answer}</small></p>
                </div>
            `).join('<hr>');
        } else if (quiz.error) {
            content.innerHTML = `<h3>Quiz</h3><p>Error: ${quiz.error}</p>`;
        } else {
            content.innerHTML = `<h3>Quiz</h3><p>Unexpected response format from server</p>`;
        }
    } catch (error) {
        console.error('Error fetching quiz:', error);
        document.getElementById('content').innerHTML = `<h3>Quiz</h3><p>Failed to load quiz: ${error.message}</p>`;
    }
}

async function startPassage() {
    try {
        const response = await fetch('/passage');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        const content = document.getElementById('content');
        if (data.error) {
            content.innerHTML = `<h3>Unseen Passage</h3><p>Error: ${data.error}</p>`;
        } else {
            content.innerHTML = `
                <h3>Unseen Passage</h3>
                <p>${data.passage}</p>
                ${data.questions.map((q, i) => `
                    <p>${q.question}</p>
                    <input type="text" id="answer${i}">
                    <p><small>Correct Answer: ${q.answer}</small></p>
                `).join('')}
            `;
        }
    } catch (error) {
        console.error('Error fetching passage:', error);
        document.getElementById('content').innerHTML = `<h3>Unseen Passage</h3><p>Failed to load passage: ${error.message}</p>`;
    }
}

async function startPuzzle() {
    try {
        const response = await fetch('/puzzle');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        const content = document.getElementById('content');
        if (data.error) {
            content.innerHTML = `<h3>Word Search Puzzle</h3><p>Error: ${data.error}</p>`;
        } else {
            content.innerHTML = `
                <h3>Word Search Puzzle</h3>
                <p>Find these words: ${data.words.join(', ')}</p>
                <p>(Imagine a grid here with ${data.words.join(', ')} hidden!)</p>
            `;
        }
    } catch (error) {
        console.error('Error fetching puzzle:', error);
        document.getElementById('content').innerHTML = `<h3>Word Search Puzzle</h3><p>Failed to load puzzle: ${error.message}</p>`;
    }
}