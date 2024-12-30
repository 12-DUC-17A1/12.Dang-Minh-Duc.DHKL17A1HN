import threading
import time

def task(name, duration):
    print(f"Starting {name}")
    time.sleep(duration)
    print(f"Completed {name}")

if __name__ == "__main__":
    threads = []
    tasks = [("Task-1", 1), ("Task-2", 2), ("Task-3", 3)]

    for name, duration in tasks:
        thread = threading.Thread(target=task, args=(name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tasks completed")
