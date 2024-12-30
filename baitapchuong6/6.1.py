import threading

def print_thread_name(name):
    print(f"Starting {name}")

if __name__ == "__main__":
    threads = []
    thread_names = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]

    for name in thread_names:
        thread = threading.Thread(target=print_thread_name, args=(name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Exiting Main Thread")
