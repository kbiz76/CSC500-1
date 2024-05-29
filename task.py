tasks = ["TEAMS Meeting", "Sprint Planning", "Power Hour", "Snapshot", "Requirements Gathering", "Synch Up", "Lab Meeting"]

print("Tasks for the week:")
for task in tasks:
  print(f"- {task}")

completed_task_index = tasks.index("Sprint Planning")
tasks[completed_task_index] = "Sprint Complete"
print("\nUpdated task list:")
for task in tasks:
  print(f"- {task}")
