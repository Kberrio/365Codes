const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const PORT = process.env.PORT || 3000;

let players = {};
let game = {
    turn: null,
    players: [],
    cards: [], // This should be your deck of cards. 
};

app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('New client connected');
    
    socket.on('joinGame', (username) => {
        players[socket.id] = { username, hand: [], health: 30 };
        game.players.push(socket.id);
        
        if (game.players.length === 2) {
            startGame();
        }
    });

    socket.on('playCard', (cardIndex) => {
        const player = players[socket.id];
        if (game.turn === socket.id && player.hand[cardIndex]) {
            // Implement card playing logic here
            io.to(game.players[1]).emit('opponentPlayedCard', player.hand[cardIndex]);
            player.hand.splice(cardIndex, 1);
            nextTurn();
        }
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
        delete players[socket.id];
        game.players = game.players.filter(id => id !== socket.id);
    });
});

const startGame = () => {
    game.turn = game.players[0];
    // Initialize decks and hands
    game.players.forEach(id => {
        players[id].hand = drawInitialCards();
    });
    io.to(game.players[0]).emit('yourTurn', players[game.players[0]].hand);
    io.to(game.players[1]).emit('opponentTurn');
};

const drawInitialCards = () => {
    // Draw 3 cards for initial hand, adjust as needed
    return Array(3).fill().map(drawCard);
};

const drawCard = () => {
    // Implement card drawing logic
    return game.cards.pop();
};

const nextTurn = () => {
    game.turn = game.turn === game.players[0] ? game.players[1] : game.players[0];
    io.to(game.turn).emit('yourTurn', players[game.turn].hand);
    io.to(game.players.find(id => id !== game.turn)).emit('opponentTurn');
};

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
