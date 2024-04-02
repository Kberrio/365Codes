const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('This is a normal response...or is it?');
  res.end();
});

const originalConsoleLog = console.log;

console.log = function (...args) {
  const rickRollUrl = 'https://www.youtube.com/watch?dQw4w9WgXcQ';
  originalConsoleLog.call(this, `You've been rickrolled! Check out this cool bug fix: ${rickRollUrl}`);
};

server.listen(3000, () => {
  console.log('Server listening on port 3000. Open your terminal for surprises!'); // This will also get rickrolled
});
