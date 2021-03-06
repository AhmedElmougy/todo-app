import sys

from flask import Flask, render_template, redirect, url_for, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import desc


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://user@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    todo_item = db.Column(db.String(), nullable=False)
    checked = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.todo_item}>'


@app.route('/todos/<todo_id>/edit', methods=['POST'])
def update_todo_item_state(todo_id):
    error = False
    body = {}

    try:
        checked = request.get_json()['checked']
        todo = Todo.query.get(todo_id)
        todo.checked = checked
        db.session.commit()
        body['id'] = todo.id
        body['checked'] = todo.checked
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(404)
    else:
        return jsonify(body)


@app.route('/todos/create', methods=['POST', ])
def create():
    error = False
    body = {}

    try:
        todo_item = request.get_json()['todo_item']
        todo = Todo(todo_item=todo_item)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['todo_item'] = todo.todo_item
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(404)
    else:
        return jsonify(body)


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by(desc('id')).all())
