from flask import Flask,request,jsonify
import json

app=Flask(__name__)

FILE_NAME="tasks.json"

def read_tasks():
    try:
        with open(FILE_NAME, "r")as file:
            return json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        return []

def write_tasks(target):
    with open(FILE_NAME, "w")as file:
        json.dump(target,file,indent=4)

VALID_STATUS=["Pending","Completed","In progress"]

@app.route("/tasks",methods=["GET"])
def get_tasks():
    tasks=read_tasks()
    status=request.args.get("status")
    if status:
        filtered_tasks=[]
        for task in tasks:
            if task["status"]==status:
                filtered_tasks.append(task)
        return jsonify(filtered_tasks)
    return jsonify(tasks)

@app.route("/tasks",methods=["POST"])
def create_task():
    tasks=read_tasks()
    new_task=request.json
    if new_task is None:
        return jsonify({"error": "Request body must be JSON"}), 400
    required_fields=["id","title","description","status"]
    for field in required_fields:
        if field not in new_task:
            return jsonify({"error": f"Missing field: {field}"}), 400
    for task in tasks:
        if task["id"]==new_task["id"]:
            return jsonify({"error": "Task ID already exists"}), 400
    if new_task["status"] not in VALID_STATUS:
        return jsonify({"error": "Invalid status"}), 400
    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify({
        "message": "Task created successfully",
        "task": new_task
    }), 201

@app.route("/tasks/<int:task_id>",methods=["PUT"])
def update_task(task_id):
    tasks=read_tasks()
    updated_data=request.json
    if updated_data is None:
        return jsonify({"error": "Request body must be JSON"}), 400
    for task in tasks:
        if task["id"]==task_id:
            if "title" in updated_data:
                task["title"]=updated_data["title"]
            if "description" in updated_data:
                task["description"]=updated_data["description"]
            if "status" in updated_data:
                if updated_data["status"]not in VALID_STATUS:
                    return jsonify({"error": "Invalid status"}), 400
                task["status"]=updated_data["status"]
            write_tasks(tasks)
            return jsonify({
                "message": "Task updated successfully",
                "task": task
            })
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>",methods=["DELETE"])
def delete_task(task_id):
    tasks=read_tasks()
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            write_tasks(tasks)
            return jsonify({"message": "Task deleted successfully"})
    return jsonify({"error": "Task not found"}), 404

if __name__=="__main__":
    app.run(debug=True)