from datetime import datetime
import json
import sys
import os

def load_tasks():
    if not os.path.exists("data.json"):
        return []
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    json_str = json.dumps(tasks, indent=4)
    with open("data.json", "w") as f:
        f.write(json_str)

def add_tasks(description):
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    
    new_tasks = {
    "id" : new_id,
    "description" : description,
    "Status" : "Pending",
    "CreatedAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "UpdatedAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(new_tasks)
    save_tasks(tasks)
    print(f"Task Successfully Added (ID: {new_id})")

def update_description(task_id, new_desctiption):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_desctiption
            task["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"tasks successfully upated (ID: {task['id']})")
            return
    print("task not found!")
def update_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["Status"] = new_status
            task["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("Task succesfully updated")
            return
def list_done(status):
    tasks = load_tasks()
    for task in tasks:
        if task["Status"] == status:
            print(task)
def list_all():
    tasks = load_tasks()
    for task in tasks:
        print(task)
while(True):
    print("CLI-Task-Planner",end=" ")
    task = input().strip().lower()
    if task.lower() == "add":
        description = (input())
        add_tasks(description)
    elif task.lower() == "update":
        id = int(input())
        new_desc = (input())
        update_description(id, new_desc)
    elif task.lower() == "mark-in-progress":
        id = int(input())
        update_status(id, "in-progress")
    elif task.lower() == "mark-done":
        id = int(input())
        update_status(id, "done")
    elif task.lower() == "list":
        list_all()
    elif task.lower() == "list-done":
        list_done("done")
    elif task.lower() == "list-in-progress":
        list_done("in-progress")
    elif task.lower() == "help":
        print("Commands : Add(add a new task),\n"
        "Update(update description of exising task,(id--<newline>--new_desc))\n" \
        "mark-done(marks status of existing tasks as done,--<newline>--(id))\n" \
        "mark-in-progress(marks the status of existing tasks as in-progress,--<newline>--(id))\n" \
        "list(lists all tasks), list-done(lists tasks with status-done)\n" \
        "list-in-progress(lists tasks with status in-progress)"\
        "exit(exit the CLI-Task-Planner)\n"\
        "All data will be stored at data.json in the same directory")
    elif task.lower() == "exit":
        break