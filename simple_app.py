from flask import Flask, render_template, redirect, url_for, jsonify, request

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://user@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.todo_item}>'


db.create_all()


@app.route('/todos/create', methods=['POST', ])
def create():
    todo_item = request.get_json()['todo_item']
    todo = Todo(todo_item=todo_item)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'todo_item': todo.todo_item
    })


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
