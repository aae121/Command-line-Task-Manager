import json
from maro import Tasks
from maro import Work_Task
from maro import Personl_Task
from maro import Task_manger

task=[]

file = open("data.json","r")
task = json.load(file)
file.close()
task1 = ''

def main():
 while True:
    print("Choose  one of the following options")
    print("[1] if you want to create a Task \n[2] if you to update your task".upper())
    print("[3] if you want to view list of tasks\n[4] if you want to delete a task\n[5] if you want to mark a task as completed\n[6]"
          "if you want to exit\n".upper())


    cho=input("enter your choice : ")
    while True:
      try :
          cho = int (cho)
          break
      except :

          cho = input("enter your choose between [1 to 6] : ")

    while cho not in [1,2,3,4,5,6]:
        cho = input("enter your choose between [1 to 6] : ")
        while True:
            try:
                while cho not in [1, 2, 3, 4, 5, 6]:
                    cho = input("enter your choose between [1 to 6] : ")
                    cho = int(cho)
                break

            except:

                cho = input("enter your choice : ")



    if cho == 6:
        print("Thank you !".upper())
        exit()

    if cho == 1:
       title = input(f"Enter the (title) of the task : \n")

       for i in task :
         while i ['Title'] == title:
               print("You are already using this name in a task")
               title = input(f"Enter the (title) of the task : \n")


       desc = input("Enter the (description) of the task : \n")

       due_date = input("Enter the (due date) of the task : \n")
       dued = due_date.split('/')
       while len(dued) != 3 :
           due_date = input("Enter the (due date) of the task (in this form DD/MM/YYYY) : \n")
           dued = due_date.split('/')

#**************************************
       while True:
            try:
                for i in dued:
                    i = int(i)
                break
            except:
                due_date = input("Enter the (due date) of the task : \n")
                dued = due_date.split('/')
                while len(dued) != 3:
                    due_date = input("Enter the (due date) of the task (in this form DD/MM/YYYY) : \n")
                    dued = due_date.split('/')

#****************************************

       status = input("Enter the (status) of the task : \n")
       while status.lower() not in ["completed","incompleted","inprogress","in progress"]:
           status = input("Enter the (status) of the task [completed,incompleted,inprogress]: \n")



       task_type=input("enter the type of the task : ")
       while task_type.lower() not in ['personal','work']:
            task_type = input("enter the type of the task [PERSONAL or WORK ] : ")

       task1=Task_manger(title,desc,due_date,status,task_type,task)
       task1.add()
       for i in task:
           if i['task type'] == "PERSONAL":
               print(
                   f"title:{i['Title']}  \ndescription : {i['description']} \ndue_date : {i['due_date']} \nstatus : {i['status']} \ntask type {i['task type']} \n category : {i['category']}")
               print("*" * 10)
           if i['task type'] == "WORK":
               print(
                   f"title:{i['Title']}  \ndescription : {i['description']} \ndue_date : {i['due_date']} \nstatus : {i['status']} \ntask type {i['task type']} \n Priority : {i['Priority']}")
               print("*" * 10)


       file = open("data.json", "w")
       json.dump(task, file, indent=2)
       file.close()


    if cho == 2:
        title = input("Enter the title of the task : ")
        for i in task:
            if title != i["Title"]:
                y = 1
            if title == i["Title"]:
                new_due=input("Enter your new due date")
                Task_manger.update(task,i,new_due)


                file = open("data.json", "w")
                json.dump(task, file, indent=2)
                file.close()


    if cho ==3:
          Task_manger.view_Tasks(task)

    y=0
    if cho ==4:
       title=input("Enter the title of the task : ")
       for i in task :
           if title != i ["Title"]:
               y=1
           if title == i ["Title"]:

               Task_manger.delete_Task(task,i)

               file = open("data.json", "w")
               json.dump(task, file, indent=2)
               file.close()

    if cho == 5:
        title = input("Enter the title of the task : ")
        for i in task:
            if title != i["Title"]:
                y = 1
            if title == i["Title"]:
               y=0

               Task_manger.mark_task_complete(task, i)
               break
    if y == 1 :
            print("invalid title")

main()