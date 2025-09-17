# While loop - for continuous user input

# Positional arguments
# Def function for add, del, mark and etc
# Conditionals - for defining which command to use

# JSON - for data storage, dicts --> json
# dicts --> json
# rewriting file with appending it
# loagin file data to show task list

import json

user_input = None
print("Command options:\n1 - add task \n2 - list tasks \n3 - change task status \n4 - delete task")
while (user_input == None):
    # Works for str --> int user input
    try:
        input_ = int(input("Enter the command: "))
        if (1 <= input_<= 4):
            user_input = input_

            if (user_input == 1):
                print("Add task")
                # Task ID works as a unique key, ID is provided by user input
                task_ID = input("Enter name of task: ")
                task_descr = input("Enter description of task: ")
                priority = input("Enter task priority: ")
                task_due = input("Enter the due date: ")

                
                # Read, modify, write cycle
                try:
                    with open("tasks_data.json", mode="r", encoding="utf-8") as modify_file:
                        # Do not load if json is empty/not exist
                        tasks_data = json.load(modify_file)
                    
                    tasks_data[task_ID] = {
                        "descr":task_descr,
                        "prior":priority,
                        "due_date":task_due,
                        "status":"to-do"
                    }

                    with open("tasks_data.json", mode ="w", encoding="utf-8") as append_file:
                        json.dump(tasks_data, append_file, indent=4) 

                except:
                    with open("tasks_data.json", mode="w", encoding="utf-8") as write_file:
                        tasks_data = {}
                        tasks_data[task_ID] = {
                            "descr":task_descr,
                            "prior":priority,
                            "due_date":task_due,
                            "status":"to-do"                          
                        }                   
                        json.dump(tasks_data, write_file, indent=4)



            # Next: prettify json output for user
            # Next: option to see tasks divided by "status" value
            elif (user_input == 2):
                # Use json.load to see list of tasks
                try:                  
                    with open("tasks_data.json", mode="r", encoding="utf-8") as read_file:
                        task_data = json.load(read_file)

                        # Next: how to print only task names and due dates
                        print("Task List: ")
                        for i in task_data:
                            # Next: show in one line, not two - e.g. Name:"-----"     Date:"-----"
                            print("Name:    ", [i][0])
                            deadline = task_data.get(i, {}).get("due_date")
                            print("Deadline:", deadline)
                        
                    

                except:
                    print("There is no JSON file in current directory")


            
            # Next: change status feature - in progress/to-do/done
            elif (user_input == 3):
                print("Change task status")
                task_name = input("Please enter task name: ")

                with open("tasks_data.json", mode="r", encoding="utf-8") as update_file:
                    task_status = json.load(update_file)
                    
                    # Next: if file does not exist --> break & print("Error")
                    for i in task_status:
                        if([i][0] == task_name):
                            continue


                print("Change status:\n1 - Done\n2 - In progress\n3 - To-do")
                try:
                    command_status = int(input("Enter the command: "))
                    if ( 1 <= command_status <= 3):

                        print("done")
                        if (command_status == 1):

                            # Deletes full json file instead of updating it
                            task_status[task_name]["status"] = "done"
                            print(task_status)
                            with open("tasks_data.json", mode="w", encoding="utf-8") as write_file:
                                json.dump(task_status, write_file, indent=4)
                        elif (command_status == 2):
                            task_status[task_name]["status"] = "in progress"
                            with open("tasks_data.json", mode="w", encoding="utf-8") as write_file:
                                json.dump(task_status, write_file, indent=4) 
                        else:
                            task_status[task_name]["status"] = "to-do"
                            with open("tasks_data.json", mode="w", encoding="utf-8") as write_file:
                                json.dump(task_status, write_file, indent=4)                             


                    else: 
                        print("Please enter existing command options")

                              

                except:
                    print("Please enter existing command options")



            # Next: provide user list of existing tasks and option to delete one of them
            else:
                try:
                    task_name = input("Please enter task name: ")                
                    with open("tasks_data.json", mode="r", encoding="utf-8") as read_file:
                        tasks_data = json.load(read_file)
                        del tasks_data[task_name]

                    with open("tasks_data.json", mode="w", encoding="utf-8") as modify_file:
                        tasks_data = json.dump(tasks_data, modify_file, indent=4)
                    print("Task is deleted")
                except:
                    print("There is no such file in current directory")


        else:
            print("Please enter existing command options")
            continue

            
        
    except:
        print("Please enter existing command options")
        continue
 
 
            






