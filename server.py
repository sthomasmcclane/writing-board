from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# The board is index.html in the same directory
BOARD_FILE = 'index.html'

@app.route('/')
def index():
    return send_from_directory('.', BOARD_FILE)

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.get_json()
        html_content = data.get('html')
        if not html_content:
            return "No content received", 400
            
        with open(BOARD_FILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return "Board saved successfully!", 200
    except Exception as e:
        return f"Error saving board: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
