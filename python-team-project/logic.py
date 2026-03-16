import os

DB_PATH = "data/tasks.txt"

def add(task: str):
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(DB_PATH , "a", encoding="utf-8") as f:
            f.write(task + "\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def get():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error: {e}")
        return []

def delete(task: str):
    tasks = get()
    if task in tasks:
        tasks.remove(task)
        try:
            with open(DB_PATH, "w", encoding="utf-8") as f:
                for t in tasks:
                    f.write(t + "\n")
            return True
        except Exception as e:
            print(f"Error: {e}")
    return False

def search(task: str):
    tasks = get()
    return [t for t in tasks if task.lower() in t.lower()]