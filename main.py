FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n") 

def menu():
  print("\n1. View Tasks")
  print("2. Add Tasks")
  print("3. Remove Tasks")
  print("4. Exit")
a = load_tasks()
while True:
  menu()
  v = int(input("Please Make Your Choice: "))
  if v == 1:
      print("Your Tasks")
      if len(a) != 0:
          for i in range(len(a)):
              print(f"{i+1}. {a[i]}")
      else:
          print("You have no Tasks!")

  elif v == 2:
      while True:
          b = input("Enter a task to add: ")
          a.append(b)
          save_tasks(a)
          print(f"{b} has succesfully added to your tasks!")
          d = input("Do you want to add more tasks? (y/n): ")
          if d == "y":
              continue
          else:
              break
  elif v == 3:
            print("Your Tasks")
            if len(a) != 0:
                for i in range(len(a)):
                    print(f"{i+1}. {a[i]}")
                try:
                    c = int(input("Enter the task number to remove:")) - 1
                    a.pop(c)
                    save_tasks(a)
                except (IndexError, ValueError):
                    print("Invalid task number.")
            else:
                print("You have no Tasks!")

  elif v == 4:
      print("GoodBye")
      break

