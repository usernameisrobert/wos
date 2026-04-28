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

@app.route('/<filename>.wasm')
def serve_wasm(filename):
    # Construct the full filename with the extension
    wasm_file = f"{filename}.wasm"
    
    # send_from_directory safely handles path traversal 
    return send_from_directory(BASE_DIR, wasm_file, mimetype='application/wasm')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
