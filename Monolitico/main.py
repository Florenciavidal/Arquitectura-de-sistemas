import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    print("Tareas actuales:", tasks)
    nueva = input("Ingresa una nueva tarea: ")
    tasks.append(nueva)
    save_tasks(tasks)
    print("Tarea guardada.")

if __name__ == "__main__":
    main()
