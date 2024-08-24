# Command-Line Task Manager

**Command-Line Task Manager** is a Python application designed to help you manage tasks directly from the command line. With this tool, you can create, update, and manage tasks, and it uses JSON for persistent storage to keep your data safe between sessions.

## Features

- **Create Tasks**: Add new tasks with a title and description.
- **Update Tasks**: Modify the title or description of existing tasks.
- **Mark Tasks as Completed**: Change the status of tasks to completed.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Persistent Storage**: Tasks are saved in a JSON file, ensuring data is preserved between sessions.

## Usage

To use the Command-Line Task Manager, run the application with Python and use the provided commands to manage your tasks.

## Example Commands

- **Add a Task**: 
  ```bash
  python task_manager.py add --title "Task Title" --description "Task Description"
