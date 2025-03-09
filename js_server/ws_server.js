const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// In-memory store for player positions.
let players = {};
let gameStarted = false;
const NUM_OF_PLAYERS = 3;

io.on('connection', (socket) => {
  console.log('A client connected:', socket.id);

  // Send a welcome message on connection.
  socket.emit('message', { message: "Welcome to the game!" });

  // Listen for player updates.
  socket.on('update', (data) => {
    // Expected data format: { player_id: "player1", x: 100, y: 200 }
    const { player_id, x, y } = data;
    players[player_id] = { x, y };

    // Check if the game should start.
    if (!gameStarted) {
      if (Object.keys(players).length >= NUM_OF_PLAYERS) {
        gameStarted = true;
        io.emit('game_start', { message: "Game Start", players });
        console.log("Game start triggered with players:", players);
      } else {
        io.emit('update', { players });
      }
    } else {
      io.emit('update', { players });
    }
  });

  socket.on('disconnect', () => {
    console.log('A client disconnected:', socket.id);
    // Optionally, remove the player's data if you can determine which one.
  });
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
