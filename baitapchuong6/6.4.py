import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        for _ in range(1000):
            counter += 1

if __name__ == "__main__":
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")
