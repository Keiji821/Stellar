#!/usr/bin/env python3
from flask import Flask, send_file, request, render_template, send_from_directory
import argparse
import os
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "access.log"
BASE_DIR = Path(__file__).parent.absolute()
IMAGE_PATH = BASE_DIR / "static" / "hola.jpg"

def log_access(ip, user_agent):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip} | User-Agent: {user_agent}"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

@app.route('/')
def index():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconocido')
    log_access(ip, user_agent)
    return render_template('index.html', image_url=f"{request.host_url}hola.jpg")

@app.route('/hola.jpg')
def serve_image():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconocido')
    log_access(ip, user_agent)
    return send_file(IMAGE_PATH, mimetype='image/jpeg')

@app.route('/favicon.ico')
def favicon():
    return send_file(IMAGE_PATH, mimetype='image/jpeg')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    
    static_dir = BASE_DIR / "static"
    static_dir.mkdir(exist_ok=True)
    
    app.run(host='0.0.0.0', port=args.port)