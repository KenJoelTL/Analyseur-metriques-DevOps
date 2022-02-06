from kanban_metrics import kanban
from pullrequest_metrics import pullRequest
from persistant_metrics import metrics

'''---------------------------------------------------------------------------------------------------------User Interface start'''


def menu():
    print("Main menu")
    print("----------------------------------")
    print("Choose an option: ")

    while True:
        print("1- KanBan metrics: ")
        print("2- Pull request metrics: ")
        print("3- Persistant kanban metrics: ")
        print("please enter your selection: ")
        choice = input()
        if choice == "1":
            kanbanMetricMenu()
            print("Main menu")
            print("----------------------------------")
            print("Choose an option: ")
        elif choice == "2":
            pullRequestMetricMennu()
            print("Main menu")
            print("----------------------------------")
            print("Choose an option: ")
        elif choice == "3":
            persistantKanbanMetric_UI()
            print("Main menu")
            print("----------------------------------")
            print("Choose an option: ")

        else:
            print("Option not avaible! please choose an available option")


def makeChoice(message):

    done = False
    while done == False:
        print(message)
        print("1- yes")
        print("2- no")
        choice = input()
        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("wrong entry , please choose an available option")



def persistantKanbanMetric_UI():
    done = False
    while done == False:
        print("Enter time intervals following the template (yyyy-mm-dd)")
        print("start date(yyyy-mm-dd):")
        startDate = input()
        print("end date(yyyy-mm-dd):")
        endDate = input()
        tasks = metrics.getData(startDate, endDate)
        if len(tasks) > 0:
            print("Metrics  between "+startDate+" and "+endDate)
            for task in tasks:
                metrics.print_formatted_datase(task)
        else:
            print(" - no data")
        done = not makeChoice(
            "Do you wish you see the metrics between another time interval? ")

'''--------------------------------------------------------------------------------------------------------------------PR UI start'''


def pullRequestMetricMennu():
    loop = True
    print("Pull Request metrics")
    print("----------------------------------")
    while loop:
        print("Choose an option: ")
        print("1- lead time for a pull request: ")
        print("2- average lead Time for closed pull request: ")
        print("3- average pull request merge time: ")
        print("4- Pull request merge rate: ")
        print("5- Pull request rejection rate: ")
        print("0- return to the main menu: ")
        choice = input()
        if choice == "1":
            singlePRLeadTime_UI()
            print("Pull Request metrics")
            print("----------------------------------")
        elif choice == "2":
            avgClosedPRLeadTime_UI()
            print(" ")
            print("Pull Request metrics")
            print("----------------------------------")
        elif choice == "3":
            avgMergePRLeadTime_UI()
            print(" ")
            print("Pull Request metrics")
            print("----------------------------------")
        elif choice == "4":
            prMergeRate_UI()
            print(" ")
            print("Pull Request metrics")
            print("----------------------------------")
        elif choice == "5":
            prRejectionRate_UI()
            print(" ")
            print("Pull Request metrics")
            print("----------------------------------")
        elif choice == "0":
            loop = False
        else:
            print("Option not avaible! Please chose a valid option.")


def singlePRLeadTime_UI():
    done = False
    pr_list = pullRequest.getPullResquestList("all")
    while done == False:
        counter = 0
        print("Which Pull Request's leadtime do you want to see: ")
        for pr in pr_list:
            print(str(counter)+" - "+pr["title"])
            counter += 1
        choice = input()
        if int(choice) >= len(pr_list):
            print("option not avaible! please choose an available option")
        else:
            leadTime = pullRequest.getSinglePullRequestLeadtime(
                pr_list[int(choice)]["number"])
            print(" - The leadtime for the pull request: " +
                  pr_list[int(choice)]["title"]+" is "+leadTime)

            done = not makeChoice(
                "Do you wish you see the lead time of another pull request? ")


def avgMergePRLeadTime_UI():
    avg = pullRequest.averageMergeTimeClosedPR()
    if avg != None:
        print("the average merge time for merged Pull Request is "+str(avg)+" days")


def avgClosedPRLeadTime_UI():
    avg = pullRequest.averageLeadTimeClosedPR()
    if avg != None:
        print("the average leadTime for closed Pull Request is "+str(avg)+" days")


def prRejectionRate_UI():
    rate = pullRequest.prRejectionRate()
    if rate != None:
        print("Pull Request rejection rate is "+str(rate)+" %")


def prMergeRate_UI():
    rate = pullRequest.prMergeRate()
    if rate != None:
        print("Pull Request merging rate is "+str(rate)+" %")


'''----------------------------------------------------------------------------------------------------------PR UI end'''


def kanbanMetricMenu():
    loop = True
    print("KanBan metrics")
    print("----------------------------------")
    while loop:
        print("Choose an option: ")
        print("1- lead Time for a task: ")
        print("2- lead Time for closed tasks in a time interval: ")
        print("3- view tasks in a specific column tasks: ")
        print("4- list of completed tasks in a time interval: ")
        print("0- return to the main menu: ")
        choice = input()
        if choice == "1":
            singleTaskLeadTime_UI()
            print("KanBan metrics")
            print("----------------------------------")
        elif choice == "2":
            leadTimeForTasksInTimeInterval_UI()
            print("KanBan metrics")
            print("----------------------------------")
        elif choice == "3":
            taskInSpecificColumn_UI()
            print("KanBan metrics")
            print("----------------------------------")
        elif choice == "4":
            completedTasksInTimeInterval_UI()
            print("KanBan metrics")
            print("----------------------------------")
        elif choice == "0":
            menu()
        else:
            print("Option not avaible! Please chose a valid option.")


def singleTaskLeadTime_UI():
    done = False
    tasks_list = kanban.getKanBanTaskList()
    while done == False:
        counter = 0
        print("Which task's leadtime do you want to see: ")
        for task in tasks_list:
            print(str(counter)+" - "+task["title"])
            counter += 1
        choice = input()
        if int(choice) >= len(tasks_list):
            print("option not avaible! please choose an available option")
        else:
            leadTime = kanban.getSingleTaskLeadtime(
                tasks_list[int(choice)]["number"])
            print(" - The leadtime for the task: " +
                  tasks_list[int(choice)]["title"]+" is "+leadTime)

            done = not makeChoice(
                "Do you wish you see the lead time of another task? ")


def taskInSpecificColumn_UI():
    done = False
    column_list = kanban.getKanBanColumnList()
    while done == False:
        counter = 0
        print("Which column task do you want to see: ")
        for column in column_list:
            print(str(counter)+" - "+column["name"])
            counter += 1
        choice = input()
        if int(choice) >= len(column_list):
            print("option not avaible! please choose an available option")
        else:
            taskList = kanban.getActiveTasks(column_list[int(choice)]["id"])
            print("list of active task in column: " +
                  column_list[int(choice)]["name"])
            if len(taskList) > 0:
                for task in taskList:
                    print(" - "+task["title"])
            else:
                print(" - no tasks at the moment")

            done = not makeChoice(
                "Do you wish you see the tasks  of another column? ")


def leadTimeForTasksInTimeInterval_UI():
    done = False
    while done == False:
        print("Enter time intervals following the template (yyyy-mm-dd)")
        print("start date(yyyy-mm-dd):")
        startDate = input()
        print("end date(yyyy-mm-dd):")
        endDate = input()
        leadTimes = kanban.getMultiTaskleadtime(startDate, endDate)
        if len(leadTimes) > 0:
            for leadTime in leadTimes:
                print(" - "+leadTime)
        else:
            print(" - no data at the moment")
        done = not makeChoice(
            "Do you wish you see the lead times  between another time interval? ")


def completedTasksInTimeInterval_UI():
    done = False
    while done == False:
        print("Enter time intervals following the template (yyyy-mm-dd)")
        print("start date(yyyy-mm-dd):")
        startDate = input()
        print("end date(yyyy-mm-dd):")
        endDate = input()
        tasks = kanban.getCompletedTasks(startDate, endDate)
        if len(tasks) > 0:
            print("Task terminated between "+startDate+" and "+endDate)
            for task in tasks:
                print(" - "+task)
        else:
            print(" - no tasks")
        done = not makeChoice(
            "Do you wish you see the tasks terminated between another time interval? ")


'''---------------------------------------------------------------------------------------------------------User Interface end'''


def main():
    menu()


if __name__ == "__main__":
    main()
