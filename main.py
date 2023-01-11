"""
Made by- Abdullah Al Saimun

"""
import datetime
import uuid

#store object
all_tasks=[]
Completed_tasks=[]
 
 
#task class
class Task:
    def __init__(self,name) -> None:
        self.id=str(uuid.uuid4())
        self.task=name
        self.created_time=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_time="NA"
        self.task_done=False
        self.completed_time="NA"
        all_tasks.append(self)
 
#update task
    def update_task(self,new_task):
        self.task=new_task
        self.updated_time=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\nTask Updated Successfully\n")
 
#complete task
    def complete_task(self):
        self.task_done=True
        self.completed_time=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        Completed_tasks.append(self)
        print("\nTask Completed Successfully\n")
 
#print all_tasks objects data
def show_all():
    chk=False
    for obj in all_tasks:
        chk=True
        print()
        print(f"ID - {obj.id}")
        print(f"Task - {obj.task}")
        print(f"Created time - {obj.created_time}")
        print(f"Updated time - {obj.updated_time}")
        print(f"Completed - {obj.task_done}")
        print(f"Completed time - {obj.completed_time}")
        print()
 
    if chk==False:
        print("No Task")
 
 
#main system
while(True):
    print('1. Add New Task')
    print('2. Show All Task')
    print('3. Show Incomplete Task')
    print('4. Show Completed Task')
    print('5. Update Task')
    print('6. Mark A Task Completed')
    n=int(input("Enter Option: "))
    if(n==1):  #add new task
        name=input("Enter New Task: ")
        task=Task(name)
        print("\nTask Created Successfully\n")
 
    elif(n==2):  #show all task
        show_all()
 
    elif(n==3):  #show incomplete task
        chk=False
       
        for obj in all_tasks:
            if obj.task_done==False:
                chk=True
                print()
                print(f"ID - {obj.id}")
                print(f"Task - {obj.task}")
                print(f"Created time - {obj.created_time}")
                print(f"Updated time - {obj.updated_time}")
                print(f"Completed - {obj.task_done}")
                print(f"Completed time - {obj.completed_time}")
                print()
        if chk==False:
            print("\nNo Incomplete Task\n")
 
    elif(n==4):   #show complete task
        chk=False
        for obj in Completed_tasks:
                chk=True
                print()
                print(f"ID - {obj.id}")
                print(f"Task - {obj.task}")
                print(f"Created time - {obj.created_time}")
                print(f"Updated time - {obj.updated_time}")
                print(f"Completed - {obj.task_done}")
                print(f"Completed time - {obj.completed_time}")
                print()
        if chk==False:
            print("\nNo Complete Task\n")
   
    elif(n==5):   # update task
        incompleted=[]
        for obj in all_tasks:
            if obj.task_done==False:
                incompleted.append(obj)
        if len(incompleted)==0:
            print("\nNO Task To Update\n")
            continue
 
        print("\nSelect Which Task To Update\n")
        for i,obj in enumerate(incompleted):
                print()
                print(f"Task No - {i+1}")
                print(f"ID - {obj.id}")
                print(f"Task - {obj.task}")
                print(f"Created time - {obj.created_time}")
                print(f"Updated time - {obj.updated_time}")
                print(f"Completed - {obj.task_done}")
                print(f"Completed time - {obj.completed_time}")
                print()
        k=int(input("Enter Task: "))
        name=input("Enter New Task: ")
        incompleted[k-1].update_task(name)
 
    elif(n==6):  # mark a task completed
        incompleted=[]
        for obj in all_tasks:
            if obj.task_done==False:
                incompleted.append(obj)
        if len(incompleted)==0:
            print("\nNO Task To Complete\n")
            continue
 
        print("\nSelect Which Task To Complete\n")
        for i,obj in enumerate(incompleted):
                print()
                print(f"Task No - {i+1}")
                print(f"ID - {obj.id}")
                print(f"Task - {obj.task}")
                print(f"Created time - {obj.created_time}")
                print(f"Updated time - {obj.updated_time}")
                print(f"Completed - {obj.task_done}")
                print(f"Completed time - {obj.completed_time}")
                print()
        k=int(input("Enter Task: "))
        incompleted[k-1].complete_task()
 

