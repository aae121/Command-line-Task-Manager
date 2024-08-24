# Command-Line Task Manager

## Overview

The **Command-Line Task Manager** is a Python application that provides a simple way to manage tasks via the command line. This application supports creating, updating, and managing tasks with persistent storage using JSON.

## Features

- **Create Tasks**: Add new tasks with a title and description.
- **Update Tasks**: Modify the title or description of existing tasks.
- **Mark Tasks as Completed**: Change the status of tasks to completed.
- **Delete Tasks**: Remove tasks from the list.
- **Persistent Storage**: Tasks are saved to and loaded from a JSON file.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/command-line-task-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd command-line-task-manager
    ```

### Usage

1. Run the application:
    ```bash
    python task_manager.py
    ```

2. Follow the on-screen prompts to manage tasks.

### Code Structure

- `task_manager.py`: The main script containing the implementation of the task manager.
- `tasks.json`: JSON file for storing tasks persistently.

## Example

To create a new task, run:
```bash
python task_manager.py add "Sample Task" "This is a sample task description."
