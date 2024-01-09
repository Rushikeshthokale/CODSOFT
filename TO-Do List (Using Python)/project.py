tasks=[]

def addTask():
  task=input("Please enter the task you want to add: ")
  tasks.append(task)
  print(f"Task '{task}' added successfully")

def listTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index,task in enumerate(tasks):
      print(f"Task {index}: {task}")



def deleteTask():
  listTasks()
  try:
    taskToDelete=int(input("Enter the task number to delete:"))
    if taskToDelete>=0 and taskToDelete<len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed")
    else:
      print(f"Task #{taskToDelete} does not exist")
  except:
    print("Invalid input")
if __name__=="__main__":
  ###Create a loop to run the app
  print("Welcome to the To-Do List App")
  while True:
    
    print("---------------------------------")
    print("1.Add a task")
    print("2.Delete a task")
    print("3.List tasks")
    print("4.Quit")

    choice=input("Enter your choices: ")

    if(choice=="1"):
      addTask()
    elif(choice=="2"):
      deleteTask()
    elif(choice=="3"):
      listTasks()
    elif(choice=="4"):
      break
    else:
      print("Invalid choice. Please try again.")


  print("Goodbye!")