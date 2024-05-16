from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index(): 
    return '''
        <h1>Hello, World!</h1>
        <h2>Paramita Ban</h2>
        <p>This is the attendance system for Paramita Ban</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)