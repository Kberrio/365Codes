const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
];

let currentPlayer = 'X';

function printBoard() {
  console.log('  0 1 2');
  for (let i = 0; i < board.length; i++) {
    console.log(i + ' ' + board[i].join(' '));
  }
}

function checkWin() {
  // Check rows
  for (let i = 0; i < 3; i++) {
    if (board[i][0] === board[i][1] && board[i][1] === board[i][2] && board[i][0] !== ' ') {
      return true;
    }
  }
  // Check columns
  for (let j = 0; j < 3; j++) {
    if (board[0][j] === board[1][j] && board[1][j] === board[2][j] && board[0][j] !== ' ') {
      return true;
    }
  }
  // Check diagonals
  if ((board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[0][0] !== ' ') ||
      (board[0][2] === board[1][1] && board[1][1] === board[2][0] && board[0][2] !== ' ')) {
    return true;
  }
  return false;
}

function checkDraw() {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === ' ') {
        return false;
      }
    }
  }
  return true;
}

function switchPlayer() {
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

function play() {
  printBoard();
  rl.question(`Player ${currentPlayer}, enter your move (row column): `, (input) => {
    const [row, col] = input.split(' ').map(pos => parseInt(pos));
    if (isNaN(row) || isNaN(col) || row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] !== ' ') {
      console.log('Invalid move! Please try again.');
      play();
    } else {
      board[row][col] = currentPlayer;
      if (checkWin()) {
        printBoard();
        console.log(`Player ${currentPlayer} wins!`);
        rl.close();
      } else if (checkDraw()) {
        printBoard();
        console.log('It\'s a draw!');
        rl.close();
      } else {
        switchPlayer();
        play();
      }
    }
  });
}

play();
