import threading

def task(name):
    print(f"Executing task: {name}")

if __name__ == "__main__":
    threads = []
    tasks = ["Task-A", "Task-B", "Task-C"]

    for t in tasks:
        thread = threading.Thread(target=task, args=(t,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tasks completed")
