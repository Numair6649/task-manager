import json
from pprint import pprint



def addTask(task):
    next_id = 1
    new_task = task
    status = "Not Started"
    new_data = [{
                       "id":next_id,
                       "Task":new_task,
                       "Status":status
                    }
    ]

    try:
        with open("Task Manager/tasks.json", mode="r") as file:
                
                data = json.load(file)
                
                if data:
                    max_id = max(item["id"] for item in data if "id" in item)
                    

                    next_id = max_id + 1
                
                new_data = {
                       "id":next_id,
                       "Task":new_task,
                       "Status":status
                }
                data.append(new_data)
                
    except FileNotFoundError:
        with open("Task Manager/tasks.json", mode="w") as file:
            json.dump(new_data,file,indent=4)
    else:
        with open("Task Manager/tasks.json", mode="w") as file:
            json.dump(data,file,indent=4)


def viewTask():
    data = list()
    try:
        with open("Task Manager/tasks.json", mode="r") as file:  
                data = json.load(file)
                pprint(data)
    except FileNotFoundError:
        with open("Task Manager/tasks.json", mode="w") as file:
                json.dump(data,file)
                pprint(data)
                
def updateTask():
    
    try:
        with open("Task Manager/tasks.json", mode="r") as file:
            data = json.load(file)
            pprint(data)

       
    except FileNotFoundError:
        print("As there is no tasks there, we cannot update for any given task.")
    else:
        id_flag = False
        while not id_flag:
            task_id_tp_update = input("Please provide me the task_id you want to update? ")

            update_choice = input("Do You want to change the Task or its status? ").lower()

            if update_choice == "task":
                updated_task = input("what is the new task that you want to be updated instead pf the old task? \n")
                for task in data:
                    
                    if task["id"] == int(task_id_tp_update):
                        task["Task"] = updated_task
                        id_flag = True
                if not id_flag:
                    print("No task with this id found. Try again")
                    
                
            elif update_choice == "status":
                updated_status = input("what is the new status that you want to be updated instead pf the old status? \n")
                for task in data:
                    if task["id"] == int(task_id_tp_update):
                        task["Status"] = updated_status
                        id_flag = True
                if not id_flag:
                    print("No task with this id found. Try again")
                    
            else:
                print("wrong input. Try again")
                
            with open("Task Manager/tasks.json", mode="w") as file:
                json.dump(data,file,indent=4)

        
def deleteTask():
    id_flag = False
    try:
        with open("Task Manager/tasks.json", mode="r") as file:  
                data = json.load(file)
                pprint(data)
    except FileNotFoundError:
        pprint("No Data Exists. Thus no deletion can be Done")
    else:
        while not id_flag:
            id_to_delete = int(input("Which Task_id do you want to Delete? "))

            updated_data = [item for item in data if item["id"]!= id_to_delete]
            
            for item in data:
                if item["id"] == id_to_delete:
                    id_flag = True
                    
            if not id_flag:
                print("There is no Task associated with that id")
                
            with open("Task Manager/tasks.json", mode="w") as file:
                json.dump(updated_data,file,indent=4)
        
        

        



print("Welcome to Task Manager \n")
user_input = input("What do want to do in the task Manager? View/Update/Add/Delete a task ?").lower()

if user_input == "add":
        user_task = input("What Task do you want to add?  ")
        addTask(user_task)
elif user_input == "view":
    viewTask()
elif user_input == "update":
    updateTask()
elif user_input == "delete":
    deleteTask()
else:
    print("Wrong Command")
    
     



