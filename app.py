from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_maze(n):
    maze = [[1 for _ in range(n)] for _ in range(n)]

    # Create guaranteed path
    x, y = 0, 0
    path = [(0,0)]
    while x < n-1 or y < n-1:
        if x < n-1 and (y == n-1 or random.choice([True, False])):
            x += 1
        else:
            y += 1
        path.append((x,y))

    # Add random walls
    for i in range(n):
        for j in range(n):
            if random.random() < 0.3:
                maze[i][j] = 0

    # Keep path open
    for (i,j) in path:
        maze[i][j] = 1

    maze[0][0] = 1
    maze[n-1][n-1] = 1

    return maze


@app.route("/", methods=["GET", "POST"])
def index():
    size = 10
    if request.method == "POST":
        size = int(request.form["size"])

    maze = generate_maze(size)

    return render_template("index.html", maze=maze, size=size)


if __name__ == "__main__":
    app.run(debug=True)