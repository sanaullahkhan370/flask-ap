from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Flask is working on mobile!"

app.run(debug=True)
