# CLI Task Planner

A simple and efficient command-line task management tool built with Python. Manage your tasks directly from the terminal with easy-to-use commands.

## Features

- ✅ Add new tasks
- ✏️ Update task descriptions
- 🔄 Mark tasks as in-progress or done
- 📋 List all tasks or filter by status
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON

## Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone or download the repository
2. Ensure `task_planner.py` is in your working directory
3. The script will automatically create `data.json` for storing tasks

## Usage

### Add a Task

```bash
python task_planner.py add "Complete Task Planner"
```

**Output:**
```
Task Successfully Added (ID: 1)
```

### Update a Task

```bash
python task_planner.py update 1 "Complete Task Planner and Homework"
```

**Output:**
```
Task successfully updated (ID: 1)
```

### Mark Task as In-Progress

```bash
python task_planner.py mark-in-progress 1
```

**Output:**
```
Task successfully updated
```

### Mark Task as Done

```bash
python task_planner.py mark-done 1
```

**Output:**
```
Task successfully updated
```

### List All Tasks

```bash
python task_planner.py list
```

**Output:**
```
ID: 1 | Complete Task Planner and Homework | Status: done
ID: 2 | Buy groceries | Status: pending
ID: 3 | Write documentation | Status: in-progress
```

### List Tasks by Status

**List completed tasks:**
```bash
python task_planner.py list-done
```

**List in-progress tasks:**
```bash
python task_planner.py list-in-progress
```

**List pending tasks:**
```bash
python task_planner.py list-pending
```

### Delete a Task

```bash
python task_planner.py delete 1
```

**Output:**
```
Task deleted (ID: 1)
```

## Command Reference

| Command | Syntax | Description |
|---------|--------|-------------|
| `add` | `add "description"` | Create a new task |
| `update` | `update <id> "new description"` | Update task description |
| `mark-in-progress` | `mark-in-progress <id>` | Mark task as in-progress |
| `mark-done` | `mark-done <id>` | Mark task as completed |
| `delete` | `delete <id>` | Remove a task |
| `list` | `list` | Show all tasks |
| `list-done` | `list-done` | Show completed tasks |
| `list-in-progress` | `list-in-progress` | Show in-progress tasks |
| `list-pending` | `list-pending` | Show pending tasks |

## Task Status

Tasks can have three statuses:

- **pending** - Default status for new tasks
- **in-progress** - Tasks currently being worked on
- **done** - Completed tasks

## Data Storage

Tasks are stored in `data.json` in the following format:

```json
[
  {
    "id": 1,
    "description": "Complete Task Planner",
    "status": "done",
    "CreatedAt": "2025-10-28T10:30:00.123456",
    "UpdatedAt": "2025-10-28T11:45:00.654321"
  }
]
```

## Examples

### Typical Workflow

```bash
# Add a new task
python task_planner.py add "Write project documentation"

# Start working on it
python task_planner.py mark-in-progress 1

# Update the description
python task_planner.py update 1 "Write comprehensive project documentation"

# Complete the task
python task_planner.py mark-done 1

# View all completed tasks
python task_planner.py list-done
```

## Error Handling

The application provides helpful error messages:

- **Missing arguments:** Displays usage instructions
- **Task not found:** Notifies when an invalid task ID is provided
- **Invalid command:** Suggests running without arguments for help

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

---
**Created as a project from [Roadmap.sh](https://roadmap.sh/projects/task-tracker)
**Happy task managing! 🚀**
