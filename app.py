from flask import Flask, render_template, request, redirect, url_for
import json, os, sys
from datetime import datetime, date

app = Flask(__name__)
PORT = int(sys.argv[1])
TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    tasks = load_tasks()
    bg_class = 'blue-bg' if PORT == 5001 else 'pink-bg'
    today = date.today().strftime('%d-%m-%Y')
    return render_template('index.html', tasks=tasks, port=PORT, bg_class=bg_class, today=today)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': request.form['title'],
        'done': False,
        'timestamp': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/complete')
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/delete')
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=PORT)
