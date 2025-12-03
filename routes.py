from app import app
from flask import render_template

@app.route('/') # www.domain.com
def index():
    # return "<h1>Todo index page</h1>"
    return render_template('index.html')

@app.route('/tasks') # www.domain.com/tasks
def all_tasks():
    return "<h1>List of all tasks</h1>"

@app.route('/task/<int:task_id>') # www.domain.com/task/1
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"

# www.domain.com/new-task
@app.route('/new-task')
def new_task():
    return "<h1>New task</h1>"