from flask import Flask, jsonify, request, abort

app = Flask(__name__)

TODOS = {}
NEXT_ID = 1

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(list(TODOS.values()))

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = TODOS.get(todo_id)
    if not todo:
        abort(404)
    return jsonify(todo)

@app.route("/todos", methods=["POST"])
def create_todo():
    global NEXT_ID
    payload = request.json or {}
    todo = {
        "id": NEXT_ID,
        "title": payload.get("title", "new todo"),
        "done": payload.get("done", False),
    }
    TODOS[NEXT_ID] = todo
    NEXT_ID += 1
    return jsonify(todo), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    payload = request.json or {}
    todo = TODOS.get(todo_id)
    if not todo:
        abort(404)
    todo["title"] = payload.get("title", todo["title"])
    todo["done"] = payload.get("done", todo["done"])
    return jsonify(todo)

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in TODOS:
        abort(404)
    del TODOS[todo_id]
    return jsonify({"deleted": todo_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
