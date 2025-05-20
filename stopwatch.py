import time

def stopwatch():
    print("Stopwatch")
    print("Commands: start | stop | reset | exit")

    running = False
    start_time = 0
    elapsed = 0

    while True:
        command = input("Enter command: ").lower()

        if command == "start":
            if not running:
                running = True
                start_time = time.time() - elapsed
                print("Stopwatch started.")
            else:
                print("Already running.")

        elif command == "stop":
            if running:
                elapsed = time.time() - start_time
                running = False
                print(f"Stopped at {elapsed:.2f} seconds.")
            else:
                print("Stopwatch is not running.")

        elif command == "reset":
            running = False
            start_time = 0
            elapsed = 0
            print("Stopwatch reset.")

        elif command == "exit":
            print("Exiting stopwatch.")
            break

        else:
            print("Invalid command.")

stopwatch()
