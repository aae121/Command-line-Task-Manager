import json


class Tasks:
    def __init__(self,title,disc,due,status):
        self.title = title
        self.disc = disc
        self.due = due
        self.status = status

class Personl_Task(Tasks):
    def __init__(self,title,disc,due,status,category):
         super().init(title,disc,due,status)

         self.category = category
    @staticmethod
    def get_type():
        return "PERSONAL TASK"


class Work_Task(Tasks):
    def __init__(self,title,disc,due,status,priorty):
         super().__init__(title,disc,due,status)
         self.priorty = priorty

    @staticmethod
    def get_type():
        return "WORK TASK"


class Task_manger(Tasks):


    def __init__(self,title,desc,due_date,status,type,tasks=[]):

         super().__init__(title,desc,due_date,status)

         self.type=type

         self.tasks = tasks

    def add(self):

        if self.type.lower() == 'work' :

            Priority = input("enter the Priority : ")
            task = {
                'Title': self.title,
                'description': self.disc,
                'due_date': self.due,
                'status': self.status,
                'task type': 'WORK',
                'Priority': Priority
            }
            self.tasks.append(task)
            print("Task created!".upper())



        if self.type.lower() == 'personal' :


            category = input("enter the category : ")



            task = {
                'Title': self.title,
                'description': self.disc,
                'due_date': self.due,
                'status': self.status,
                'task type': 'PERSONAL',
                'category': category
            }
            self.tasks.append(task)
            print(self.tasks)
    @staticmethod

    def view_Tasks(tasks):
        if tasks == []:
            print("there is no tasks to show  ")
            exit()
        for i in tasks :
            if i['task type'] == "PERSONAL":
               print(Personl_Task.get_type())

               print(f"title:{i['Title']}  \ndescription : {i['description']} \ndue_date : {i['due_date']} \nstatus : {i['status']} \ntask type {i['task type']} \n category : {i['category']}")
               print(""*10)

            if i['task type'] == "WORK":
                print(Work_Task.get_type())
                print(f"title:{i['Title']}  \ndescription : {i['description']} \ndue_date : {i['due_date']} \nstatus : {i['status']} \ntask type {i['task type']} \n category : {i['Priority']}")
                print("" * 10)

    @staticmethod
    def delete_Task(TASK,i):
           TASK.remove(i)
           print("Task removed!")



    @staticmethod
    def update(task,i,new_due):
        x=task.index(i)
        task[x]["due_date"]=new_due
        print("Due date updated!")




    @staticmethod
    def mark_task_complete(task,i):
        task.remove(i)
        i['status'] = "Task Completed!"
        print("DONE!")

        task.append(i)




        file = open("data.json", "w")
        json.dump(task, file, indent=2)
        file.close()


file=open("data.json","r")
task=json.load(file)
file.close()