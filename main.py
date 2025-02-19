from flask import Flask
app = Flask(__name__)

@app.route('/')
def wut():
    return 'What are you doing here?'

@app.route('/hay')
def hayyy():
    return '<h1>HAYYY</h1>'