const http = require('http');
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');
const os = require('os');

if (isMainThread) {
  const numCPUs = os.cpus().length;
  const workers = [];

  for (let i = 0; i < numCPUs; i++) {
    const worker = new Worker(__filename);
    worker.on('message', (message) => {
      console.log(`Worker ${worker.threadId} says: ${message}`);
    });
    workers.push(worker);
  }

  const server = http.createServer((req, res) => {
    const worker = workers[Math.floor(Math.random() * workers.length)];
    worker.postMessage({ req: req.url, method: req.method });
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, World!\n');
  });

  server.listen(8080, () => {
    console.log('Server running at http://127.0.0.1:8080/');
  });
} else {
  parentPort.on('message', (message) => {
    parentPort.postMessage(`Received request: ${message.method} ${message.req}`);
  });
}
