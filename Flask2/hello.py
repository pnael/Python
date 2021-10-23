from flask import Flask

app = Flask(__name__)

@app.route('/')
Def Hello():
    return 'Hello World!'
