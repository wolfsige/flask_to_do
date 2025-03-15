from crypt import methods

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Task 1", "Task 2", "Task 3"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template('index.html', tasks=tasks)

@app.route("/new", methods=["GET"])
def new():
    return render_template('new.html')

@app.route("/remove/<int:index>", methods=["GET", "POST"])
def remove_item(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
