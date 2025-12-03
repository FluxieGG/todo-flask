from app import app
from flask import render_template, request, url_for, redirect

todos = [
    {
        "id": 1,
        "title": "Set up Flask Project Structure",
        "description": "Create the Flask application, configure routes, and establish the basic folder structure for templates, static files, and modules.",
        "created_at": "2025-12-01 09:42:17",
    },
    {
        "id": 2,
        "title": "Design Blog Post Model",
        "description": "Define the database schema for blog posts, including title, content, author, and timestamp fields, using SQLAlchemy or an equivalent ORM.",
        "created_at": "2025-12-03 15:26:49",
    },
    {
        "id": 3,
        "title": "Implement Post Creation Form",
        "description": "Add a form using Flask-WTF to allow users to create new blog posts, validate inputs, and store entries in the database.",
        "created_at": "2025-11-30 11:58:05",
    }
]

@app.route('/') # www.domain.com
def index():
    todo_count = len(todos)
    return render_template('index.html', count=todo_count)

@app.route('/tasks') # www.domain.com/tasks
def all_tasks():
    return render_template('tasks.html', todos=todos)    

@app.route('/task/<int:task_id>') # www.domain.com/task/1
def task(task_id):
    task = todos[task_id - 1]
    return render_template('task.html', task=task)

# www.domain.com/new-task
@app.route('/new-task')
def new_task():
    return render_template('new_task.html')

@app.route('/edit-task/<int:task_id>', methods=["GET", "POST"])
def edit_task(task_id):
    index = task_id - 1
    task = todos[index]    
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        todos[index]["title"] = title
        todos[index]["description"] = description 
        return redirect(url_for("task", task_id=task_id))       
    return render_template('task_form.html', task=task)