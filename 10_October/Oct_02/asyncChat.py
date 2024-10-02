import asyncio
import websockets
import json

connected = set()

async def chat(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['type'] == 'message':
                await broadcast(json.dumps({'type': 'message', 'user': data['user'], 'content': data['content']}))
            elif data['type'] == 'join':
                await broadcast(json.dumps({'type': 'system', 'content': f"{data['user']} has joined the chat."}))
    finally:
        # Unregister.
        connected.remove(websocket)

async def broadcast(message):
    if connected:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(message) for user in connected])

start_server = websockets.serve(chat, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# HTML/JavaScript for client (save as index.html):
"""
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>
    <ul id='messages'></ul>
    <input type="text" id="messageBox" placeholder="Type your message here" />
    <button onclick="sendMessage()">Send</button>

    <script>
        var socket = new WebSocket("ws://localhost:6789/");
        var username = prompt("What's your name?");

        socket.onopen = function(e) {
            socket.send(JSON.stringify({type: 'join', user: username}));
        };

        socket.onmessage = function(event) {
            var data = JSON.parse(event.data);
            var li = document.createElement('li');
            if (data.type === 'message') {
                li.textContent = data.user + ": " + data.content;
            } else if (data.type === 'system') {
                li.textContent = data.content;
                li.style.fontStyle = 'italic';
            }
            document.getElementById('messages').appendChild(li);
        };

        function sendMessage() {
            var message = document.getElementById('messageBox').value;
            socket.send(JSON.stringify({type: 'message', user: username, content: message}));
            document.getElementById('messageBox').value = '';
        }
    </script>
</body>
</html>
"""