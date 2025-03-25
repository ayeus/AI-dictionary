async function startQuiz() {
    const response = await fetch('/quiz');
    const quiz = await response.json();
    const content = document.getElementById('content');
    content.innerHTML = quiz.map((q, i) => `
        <p>${q.question}</p>
        ${q.options.map(opt => `<input type="radio" name="q${i}" value="${opt}">${opt}<br>`).join('')}
    `).join('<hr>');
}