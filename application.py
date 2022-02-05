from kanban_metrics import kanban 
    
'''---------------------------------------------------------------------------------------------------------User Interface start'''

def menu():
    print("Main menu")
    print("----------------------------------")
    print("Choose an option: ")

    while True:
        print("1- KanBan metrics: ")
        print("2- Pull request metrics: ")
        print("please enter your selection: ")
        choice = input()
        if choice =="1":
            kanbanMetricMenu()
            print("Main menu")
            print("----------------------------------")
            print("Choose an option: ")    
        elif choice =="2":
            print("choice = 2")
            
        else:
            print("Option not avaible! please choose an available option")
            print("1- KanBan metrics: ")
            print("2- Pull request metrics: ")

def makeChoice(message):
    print(message)
    print("1- yes")
    print("2- no")  
    choice = input()
    done=False
    while done == False:
        if choice =="1":
            return True
        elif choice =="2":
            return False      
        else:
            print("wrong entry , please choose an available option")
            print(message)
            print("1- yes")
            print("1- no")   
            
def kanbanMetricMenu():
    loop = True
    print("KanBan metrics")
    print("----------------------------------")
    while loop:
        print("Choose an option: ")
        print("1- lead Time for a task: ")
        print("2- lead Time for tasks in a time interval: ")
        print("3- view tasks in a specific column tasks: ")
        print("4- list of tasks completed in a time interval: ")
        print("0- return to the main menu: ")
        choice = input()
        if choice =="1":
            singleTaskLeadTime_UI()
            print("KanBan metrics")
            print("----------------------------------")
            pass
        elif choice == "2":
            leadTimeForTasksInTimeInterval_UI()
            print("KanBan metrics")
            print("----------------------------------")
            pass
        elif choice == "3":
            taskInSpecificColumn_UI()
            print("KanBan metrics")
            print("----------------------------------")
            pass
        elif choice == "4":
            completedTasksInTimeInterval_UI()
            print("KanBan metrics")
            print("----------------------------------")
            pass
        elif choice == "0":
            menu()
            pass
        else :
            print("Option not avaible! Please chose a valid option between the following:")
            print("1- lead Time for a task: ")
            print("2- lead Time for tasks in a time interval: ")
            print("3- view tasks in a specific column: ")
            print("4- list of tasks completed in a time interval: ")
            print("0- return to the main menu: ")
            pass

def singleTaskLeadTime_UI():
    done =False
    tasks_list = kanban.getKanBanTaskList()
    while done ==False:
        counter = 0
        print("Which task's leadtime do you want to see: ")
        for task in tasks_list:
            print(str(counter)+" - "+task["title"])
            counter+=1 
        choice = input()
        if int(choice) >= len(tasks_list):
            print("option not avaible! please choose an available option")
        else:
            leadTime =kanban.getSingleTaskLeadtime(tasks_list[int(choice)]["number"])
            print(" - The leadtime for the task: "+tasks_list[int(choice)]["title"]+" is "+leadTime)
            
            done = not makeChoice("Do you wish you see the lead time of another task? ")
    
def taskInSpecificColumn_UI():
    done= False
    column_list = kanban.getKanBanColumnList()
    while done ==False:
        counter = 0
        print("Which column task do you want to see: ")
        for column in column_list:
            print(str(counter)+" - "+column["name"])
            counter+=1 
        choice = input()
        if int(choice) >= len(column_list):
            print("option not avaible! please choose an available option")
        else:
            taskList =kanban.getActiveTasks(column_list[int(choice)]["id"])
            print("list of active task in column: "+column_list[int(choice)]["name"])
            if len(taskList)>0:
                for task in taskList:
                    print (" - "+task["title"])
            else:
                print(" - no tasks at the moment")
                
            done = not makeChoice("Do you wish you see the tasks  of another column? ")
 
       
def leadTimeForTasksInTimeInterval_UI():
    done = False;
    while done ==False:
        print("Enter time intervals following the template (yyyy-mm-dd)")
        print("start date(yyyy-mm-dd):") 
        startDate = input()
        print("end date(yyyy-mm-dd):")           
        endDate = input()       
        leadTimes = kanban.getMultiTaskleadtime(startDate,endDate)   
        if len(leadTimes)>0:
            for leadTime in leadTimes:
                print (" - "+leadTime)
        else:
            print(" - no data at the moment")
        done = not makeChoice("Do you wish you see the lead times  between another time interval? ") 
        
def completedTasksInTimeInterval_UI():
    done = False;
    while done ==False:
        print("Enter time intervals following the template (yyyy-mm-dd)")
        print("start date(yyyy-mm-dd):") 
        startDate = input()
        print("end date(yyyy-mm-dd):")           
        endDate = input()       
        tasks = kanban.getCompletedTasks(startDate,endDate)   
        if len(tasks)>0:
            print("Task terminated between "+startDate+" and "+endDate)
            for task in tasks:
                print (" - "+task)
        else:
            print(" - no tasks")
        done = not makeChoice("Do you wish you see the tasks terminated between another time interval? ")       

'''---------------------------------------------------------------------------------------------------------User Interface end'''
def main():
    menu()
    

main()


