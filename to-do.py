tasks = []

while True:
    action = input("\n[a]dd  [v]iew  [d]one  [q]uit: ").lower()

    if action == 'a':
        task = input("Task: ")
        tasks.append(task)
    elif action == 'v':
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif action == 'd':
        num = int(input("Task number done: ")) - 1
        if 0 <= num < len(tasks):
            print(f"Completed: {tasks.pop(num)}")
    elif action == 'q':
        break
    else:
        print("Invalid option.")
