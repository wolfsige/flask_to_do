from operator import methodcaller

from flask import Flask, render_template, request


app = Flask(__name__)

tasks = ["Task 1", "Task 2", "Task 3"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
