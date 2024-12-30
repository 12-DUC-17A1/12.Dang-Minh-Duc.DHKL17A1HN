import threading

shared_list = []

def add_to_list(item):
    shared_list.append(item)

if __name__ == "__main__":
    threads = []

    for i in range(10):
        thread = threading.Thread(target=add_to_list, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Shared list: {shared_list}")
