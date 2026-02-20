from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Use the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_home():
    return send_from_directory(BASE_DIR, 'wos.html')

@app.route('/programs')
def serve_programs():
    return send_from_directory(BASE_DIR, 'programs.txt')

@app.route('/desktop.wasm')
def serve_wasm():
    # Adding mimetype for WASM is good practice for browser compatibility
    return send_from_directory(BASE_DIR, 'desktop.wasm', mimetype='application/wasm')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
