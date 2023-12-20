import time
import threading

exc = True

def count_up_to_200():
    counter = 0
    # for i in range(201):
    #     print(f"Counting up: {i}")
    for i in range(201):
        if not exc:
            break
        print(f"Counting up: {i}")
        time.sleep(0.1)  # Simulating some work
    print("Count up complete!")

def count_down_from_200():
    for i in range(50, -1, -1):
        print(f"Counting down: {i}")
        time.sleep(0.1)  # Simulating some work
    global exc
    exc = False
    print("Count down complete!")

if __name__ == "__main__":
    # Create threads for parallel execution
    count_up_thread = threading.Thread(target=count_up_to_200)
    count_down_thread = threading.Thread(target=count_down_from_200)

    # Start the threads
    count_up_thread.start()
    count_down_thread.start()

    # Wait for both threads to finish
    count_up_thread.join()
    count_down_thread.join()

    print('Main thread exiting')
