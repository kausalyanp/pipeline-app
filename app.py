from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
    app.run(host="0.0.0.0", port=8082)

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

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    print(f"Before deletion: {tasks}")  # Debugging
    tasks = [task for i, task in enumerate(tasks) if i != task_id]
    print(f"After deletion: {tasks}")  # Debugging
    return redirect('/')

#@app.route('/delete/<int:task_id>')
#def delete_task(task_id):
    #if 0 <= task_id < len(tasks):
        #tasks.pop(task_id)
    #return redirect(url_for('index'))  

if __name__ == '__main__':
    app.run(debug=True)
