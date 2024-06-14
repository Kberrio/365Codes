const http = require('http');
const https = require('https');
const fs = require('fs');
const express = require('express');
const cookieParser = require('cookie-parser');

const PORT = 8080;
const SSL_PORT = 8443;

// Backend servers to distribute the load
const servers = [
    { host: 'localhost', port: 3001 },
    { host: 'localhost', port: 3002 },
    { host: 'localhost', port: 3003 }
];

let currentServerIndex = 0;

// SSL options
const sslOptions = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem')
};

// Create an Express app
const app = express();
app.use(cookieParser());

// Health check endpoint for the load balancer
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// Function to check the health of backend servers
async function checkServerHealth(server) {
    return new Promise((resolve) => {
        const options = {
            hostname: server.host,
            port: server.port,
            path: '/health',
            method: 'GET',
            timeout: 2000
        };

        const req = http.request(options, (res) => {
            resolve(res.statusCode === 200);
        });

        req.on('error', () => resolve(false));
        req.end();
    });
}

// Function to get the next healthy server
async function getNextServer() {
    const initialIndex = currentServerIndex;
    let tries = 0;

    do {
        const server = servers[currentServerIndex];
        currentServerIndex = (currentServerIndex + 1) % servers.length;
        const isHealthy = await checkServerHealth(server);

        if (isHealthy) {
            return server;
        }
        
        tries++;
    } while (tries < servers.length && currentServerIndex !== initialIndex);

    throw new Error('No healthy servers available');
}

// Function to handle incoming requests and proxy them to backend servers
async function handleRequest(req, res) {
    try {
        const server = await getNextServer();
        const proxyOptions = {
            hostname: server.host,
            port: server.port,
            path: req.url,
            method: req.method,
            headers: req.headers
        };

        const proxyReq = http.request(proxyOptions, (proxyRes) => {
            res.writeHead(proxyRes.statusCode, proxyRes.headers);
            proxyRes.pipe(res, { end: true });
        });

        req.pipe(proxyReq, { end: true });
    } catch (error) {
        res.statusCode = 503;
        res.end('Service Unavailable');
    }
}

app.use(handleRequest);

// Create a HTTP and HTTPS servers
const httpServer = http.createServer(app);
const httpsServer = https.createServer(sslOptions, app);

httpServer.listen(PORT, () => {
    console.log(`HTTP Load Balancer running on port ${PORT}`);
});

httpsServer.listen(SSL_PORT, () => {
    console.log(`HTTPS Load Balancer running on port ${SSL_PORT}`);
});
