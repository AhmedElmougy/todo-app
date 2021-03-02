from flask import Flask, render_template

app = Flask(__name__)

list = [
    {
        'desc': 'todo 1'
    },
    {
        'desc': 'todo 2'
    },
    {
        'desc': 'todo 3'
    },
    {
        'desc': 'todo 4'
    },
]


@app.route('/')
def index():
    return render_template('index.html', data=list)
