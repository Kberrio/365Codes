const questions = [
    { question: "Bonjour means...", answer: "Hello", options: ["Hello", "Goodbye", "Thank you"] },
    { question: "Merci means...", answer: "Thank you", options: ["Please", "Thank you", "You're welcome"] },
    { question: "Au revoir means...", answer: "Goodbye", options: ["Hello", "Goodbye", "Good morning"] }
  ];
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  function displayQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById('question').textContent = question.question;
    
    const optionsContainer = document.getElementById('options');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, index) => {
      const button = document.createElement('button');
      button.textContent = option;
      button.onclick = () => checkAnswer(option);
      optionsContainer.appendChild(button);
    });
  }
  
  function checkAnswer(selectedAnswer) {
    const question = questions[currentQuestionIndex];
    
    if (selectedAnswer === question.answer) {
      score++;
      alert('Correct!');
    } else {
      alert('Incorrect. The correct answer is: ' + question.answer);
    }
    
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
      displayQuestion();
    } else {
      endGame();
    }
  }
  
  function endGame() {
    alert(`Game over! Your score: ${score}/${questions.length}`);
    currentQuestionIndex = 0;
    score = 0;
    displayQuestion();
  }
  
  displayQuestion();