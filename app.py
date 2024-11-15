from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database (in-memory list)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

#@app.route('/delete/<task_id>', methods=['POST'])
#def delete_task(task_id):
    # Ensure task deletion logic is correct
    #tasks = [task for task in tasks if task.id != int(task_id)]
    #return redirect('/')
    
#response = client.post('/add', data={'task': 'Task to Delete'})

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
