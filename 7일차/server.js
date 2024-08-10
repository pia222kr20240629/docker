const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public'));
io.on('connection',(socket) => {
	console.log("New user connected");
	socket.on('message', (msg) => {
		io.emit('message', msg);
	});

	socket.on('disconnect', () => {
		console.log('user disconnected');
	});
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
	console.log('listening on : 3000');
});
