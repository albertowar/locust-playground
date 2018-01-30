'use strict'

const cluster = require('cluster');

if (cluster.isMaster) {
    // Count the machine's CPUs
    const cpuCount = require('os').cpus().length;

    // Create a worker for each CPU
    for (let i = 0; i < cpuCount; i += 1) {
        cluster.fork();
    }
} else {
    const http = require('http');

    http.createServer(function(request, response) {
        response.writeHead(200);
        response.end();
    }).listen(3000);
}