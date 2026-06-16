import schedule
import time
from datetime import datetime

tasks = []

def execute_task(task_name):
    print(f"Task Executed: {task_name}")
    with open("task_log.txt", "a") as file:
        file.write(f"{datetime.now()} - {task_name}\n")

def add_task(task_name, schedule_time):
    schedule.every().day.at(schedule_time).do(execute_task, task_name)
    tasks.append((task_name, schedule_time))
    print("Task Added Successfully")

print("=== Task Scheduler Tool ===")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Start Scheduler")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        task_name = input("Enter Task Name: ")
        task_time = input("Enter Time (HH:MM): ")
        add_task(task_name, task_time)

    elif choice == "2":
        print("\nScheduled Tasks:")
        for task in tasks:
            print(task)

    elif choice == "3":
        print("Scheduler Running...")
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
