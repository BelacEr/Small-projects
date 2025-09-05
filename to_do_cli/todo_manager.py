import sys

from datetime import datetime

import json

tasks = []

def add_task(description, due_date=None, priority=-1, tags=None):
    """Function to add task"""      # Useless comment LOL.
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "tags": tags,
        "created_at": datetime.now().isformat(),
        "completed": False,
    }


def show_menu():
    print("""
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
""")



