#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

#these lines of code were added at the top so that the modules won't need to be imported everytime they are needed
from datetime import date,datetime
now = datetime.now()
today = date.today()
#defining an empty string which the information from user.txt will be added to 
read_user = ''


#opening the file that will be used for the users to login 
login = open("user.txt","r")

#iterating over all of the users 
for lines in login:
    
    #adding all the usernames and passwords to the empty string
    read_user += lines
    
    #splitting the usernames and password to have them as seperate list items
    user_pass = read_user.split(", ")
    
    #joining the list items into a string all on a new line
    #otherwise the password on the 1st line would be joined by the user name on the second line
    user_pass = "\n".join(user_pass)
    
    #turning the string into a list seperated by the new line 
    user_pass = user_pass.split("\n")
    
    
#defining another empty list and adding all the usernames to it 
user_ = []
for x in range(len(user_pass)):
    if x%2 == 0:
        user_.append(user_pass[x])

#asking the user to enter their username
username = input("Please enter your username: ")


#defining a recursive function that will check if the user's input matches any of the usernames in the list
#if it doesn't match the function will keep asking the user to re enter their username
def log_in(username, x=0):   
    
    try:
        if username != user_[x]:
             x+=1
             log_in(username,x)
        else:
             #asking the user to enter their password and making it a global variable so it carries over to the next for loop 
            global pcheck
            global username1
            username1 = username 
            pcheck = input(f"Hello {username1}, please enter your password: ")
            return pcheck and username1
        
        
    except IndexError:
        x = 0
        username = input("Incorrect username. Please enter your username: ")
        log_in(username,x)
    
    

log_in(username)


#usinhg a for loop to iterate over the length of the list with all the user names and passwords
for x in range(len(user_pass)):
    
    
             #all the usernames are on even numbers, so we check if the username entered matches list items on an even index
          
    if x%2 == 0 and username1 == user_pass[x]:
                    

        #the corresponding password will always be the next item in the list 
        p = x+1
        
       
        # pcheck = input(f"Hello {username}, please enter your password: ")
        
        #if the password entered does not correspond to the username entered 
        if pcheck != user_pass[p]:
            
            #keep asking for the password while it does not match with the username
            while pcheck != user_pass[p]:
                pcheck = input("Incorrect password. Please try again: ")
                
                #when it does match the username break out of the loop 
                if pcheck == user_pass[p]:
                    break
        elif pcheck == user_pass[p]:
            continue
    
        
        
        
        
#close the file and continue to the rest of the code 
login.close()
        

    
def reg_user():
    with open("user.txt","a+") as f:
            
            #asking for the new users username
            
            
            #using another recursive function to make sure that the new username is not already in the list 
            new_user_ = input("Please enter the username of the new user: ")
            def user_check(user,x=0):
                
                try:
                    if user != user_pass[x]:
                        x+=1
                        user_check(user,x)
                    else:
    
                        user = input("Username already in use. Please enter the username of the new user: ")
                        
                        x = 0 
                        user_check(user,x)
                except IndexError:
                    global new_pass
                    global new_user
                    new_user = user
                    new_pass = input("Please enter the password for the new user: ")
                    return new_pass and new_user
                    
                    
            user_check(new_user_) 
            #asking them for their password and confirming that they can enter the same password
            
            p_confirm = input("Please reenter the password: ")
            if new_pass == p_confirm:
                
                #after confirming the password, the user's login details are added to user.txt
                f.write("\n"+new_user+", "+new_pass)
           
            
            else: 
                
                #if they keep entering the wrong password, the code will not continue until they enter the same one
                p_confirm = input("The passwords do not match please try again: ")
                while p_confirm != new_pass:
                    p_confirm = input("The passwords do not match please try again: ")
                    if p_confirm == new_pass:
                        break 
                f.write("\n"+new_user+", "+new_pass)
       
def add_task():
    print("You have requested to add a new task")
        
        #the tasks.txt file is open with the with as method 
    with open("tasks.txt","a+") as new_task:
            
            #the user is asked the relevant information needed to add a new task 
        user_task = input("Which user is the task assigned to: ")
        task = input("What is the title of the task: ")
        task_desc = input("Please enter a task description: ")
        due = input("Please enter the due date of the task (year-month-day 2022-12-02): ")
            
            #all the information is appended to the tasks.txt file
        new_task.write(f"""\n_________________________________________________________________
 
 Task:\t\t\t\t {task}
 Assigned to:\t\t\t {user_task}
 Date assigned:\t\t\t {today} 
 Due date:\t\t\t {due}
 Task complete?\t\t\t No
 Description:\n {task_desc}\n_________________________________________________________________. 
 
 """)
       
#if the user enters va, then all the tasks in the tasks.txt file are printed 
   
def view_all():
    print("""

              
These are all the current tasks

""")
        
    with open("tasks.txt","r") as all_task:
        for lines in all_task:
            print(lines)   
            

#this function replaces the old task with updated task generated in the view_mine() function 
def update_task(task,new_task):
    with open("tasks.txt","r") as f: 
        tasks = f.read()
    
    tasks = tasks.replace(task,new_task)
    
    with open("tasks.txt","w") as f:
        f.write(tasks)


def view_mine():
    all_tasks = ""
    my_name = []
    with open("tasks.txt","r+") as tasks:
        for lines in tasks:
            all_tasks += lines
            
        #defining an initial variable to start the while loop 
        my_tasks = 0
            
        #while the variable is less than the length of all the tasks- keep iterating
        while my_tasks < len(all_tasks):
                
            #after finding the first index where the username is found, the loop will keep looking for more instances
            my_tasks = all_tasks.find(username,my_tasks)
                
            #when the .find function returns -1 it means that the word is no longer the username
            if my_tasks == -1:
                break
                
        #when that is the case the code breaks out of the loop and appends all the instances where the username 
        #appears to a list
            my_name.append(my_tasks)
                
    #the length of the username is added to the variable to make finding just the username more efficient 
            my_tasks+=(len(username))
                
        
        #now that we know where the username appears, we need to print the data around it 
        #this is the initial value for the while loop 
        sections = 0
       
       
        value = []
        x=0
        while sections < len(my_name): 
                
            #this defines the starting point of the task. since all the tasks are in the same format, it was easy 
            #to find what location the username should start. so we just subract that amount to get the start of the task
            #this is the information that preceeds the location of the username
            start = my_name[sections] - 118
                
            #knowing where the task ends was also easy to calculate, so we just add that to the loaction where the username
            #was found, and that prints the rest of the information that proceeds the location of the username
            end = my_name[sections] + 234
            print(f"\n{x+1}:\n"+all_tasks[start:end])
            value.append(all_tasks[start:end])
            x+=1
    
            #this adds to the variable to ensure that all the places where the username is found is printed 
            sections+=1
        
        #initialising the variable key which will be used as keys for a dictionary      
        key = 0
        
        #defining any empty dictionary
        task_dict = {}
        
        #while the key variable does not surpass the length of the value list defined earlie- the loop will reiterate
        while key < len(value): 
            
            #a dictionary key:value pair is created with the elements from the value list 
            task_dict[key+1] = value[key]
            key+=1
        
        #ask the user if they want to view a particular task or if they wish to exit 
        which_task = int(input("Please enter the number of a task that you want to view or edit, or enter -1 to return to the menu: "))
        
            
        if which_task == -1: 
            return None
        
        
        #if they do not want to exit. they will be prompted to edit a task
        else: 
            
            
            #firstly the task they selected is printed by calling a key:value pair from the dictionary
            print(task_dict[which_task])
            selected_task = task_dict[which_task]
        
            #if the task is completed already, then it is skipped over and cannot be edited
            if selected_task.find("Yes") == -1:
                
                #all numbers for concatenation were found by copy and pasting and then finding the length of the string that had the information i wanted 
                old_date = selected_task[167:178]
                
                #the user is asked for new information to update the task or they can skip over it 
                complete = input("Is this task complete now? (yes/no):")
                new_date = input("What is the new due date? (dd mm yy/-1)")
                new_user = input("Who is the task now assigned to? (username/-1)")
               
                #for readability a new variable is defined
                edited_task = selected_task
                
                #if the user entered new information then the string edited task replaces the old information with the new one
                if complete == "yes":
                    edited_task = edited_task.replace("No","Yes")
                if new_user != "-1" :
                    edited_task = edited_task.replace(username,new_user)
                if new_date != "-1":
                    edited_task = edited_task.replace(old_date,new_date)
                    
                #the function defined above is then called and used to edit the file tasks.txt
                update_task(selected_task, edited_task)
                
                
                
                
            else: 
                return None
            

                      
def stats():
    with open("task_overview.txt","r") as t_o:
        for lines in t_o:
            print(lines)
    
        
    print("User Overview")
    with open("user_overview.txt","r") as u_o:
        for lines in u_o:
            print(lines)
            
    

                
def reports():
   
    #this clears the .txt file of the previous report which is now outdated
    with open("user_overview.txt","w") as u_o:
        u_o.write(" ")
    
    all_tasks = ""
    with open("tasks.txt","r") as r:
        for line in r:
            all_tasks += line
        
        #adding all the lines of the file to a string 
    
    
        #using the .count function to count the number of incomplete and complete tasks
        complete = all_tasks.count("Yes")
        t_incomplete = all_tasks.count("No")
        
        #defining empty lists to add items to later. and seperating the string into individual task elemnts
        dates = []
        task = all_tasks.split(".")
        places = []
      
        
        for x in range(0,len(task)-1):
            due_dates = task[x].find("Due")
            
            #splittig by the "." created some errors so i make sure that only elements with a date continue 
            if due_dates != -1:
                places.append(x)
                
                #the concatenation was calculated earlier so only the date is added to the list in the form 2022-02-02
                dates.append((task[x])[due_dates+13:(due_dates+23)])
                
                
        
            else:
                pass
            
            
        
         
        #defining empty list and initiating variables
        overdue = 0  
        overdueusers = []
        formated_dates = []
        
        #this for loop formats the dates which are saved as strings into datetime objects 
        for due_date in dates:
            due = date.fromisoformat(due_date)
            formated_dates.append(due)
        
        #to align the dates with the corresponding task, i created another empty list so both the  len(formated_dates) and len(arranged_tasks) (both are lists) is the same 
        arranged_task = []
        for x in places: 
            arranged_task.append(task[x])
            
        
        for x in range(len(places)):
            
            #this code checks to see if the date it was due is overdue and if the task is still not complete
            if formated_dates[x] < today and arranged_task[x].find("No") != -1:
                
                #if it is overdue then the tally is added to the overdue variable
                overdue += 1
                
                #i define start and end values to extract the name of the user who the task is overdue for 
                start = arranged_task[x].find("Assigned")
                end = arranged_task[x].find("Date")
                       
        
                #the users name is added to a list 
                overdueusers.append(((arranged_task[x])[start:end-2]).replace("Assigned to:\t\t\t ",""))
            
            else:
                pass
        
        #the required calculations are completed and stored as variables 
        total_tasks = complete+t_incomplete 
        per_not = (t_incomplete/total_tasks)*100
        per_odue = (overdue/total_tasks)*100
        
        
        #this will go over every user 
        for user in user_:
            #each user will have a number of done and incomplete tasks
            done = 0
            incomplete = 0 
            
            #this checks if both the user's name and 'no' or 'yes' are present 
            #the corresponding tally is added to depending on which case it is 
            for elements in task:
                if elements.find(user) != -1 and elements.find("No") != -1:
                    incomplete += 1
                elif elements.find(user) != -1 and elements.find("Yes") != -1:
                    done +=1
            
            
            #i use a try except block here to make sure that if a user has no tasks they are not added to the user_overview
            try: 
                total_user = done+incomplete
                overdue_user = overdueusers.count(user)
                per_udone = done/total_user*100
                per_nudone = incomplete/total_user*100
                per_overdue = overdue_user/total_user*100
                
                #the information is then written to the given files in a readable manner
                
                
                with open("user_overview.txt","a+") as u_o:
            
                    u_o.write(f"""

{user}'s Overview {now}                             
{user} has {total_user} tasks
They have done {done} tasks
There are still {incomplete} tasks for {user} to do
{per_udone}% of their tasks are done
{per_nudone}% of their tasks are not done
{per_overdue}% of their tasks are overdue

""")
            
            except ZeroDivisionError:
                pass
                    
    with open("task_overview.txt","w") as t_o:
        t_o.write(f"""
Task Overview:
Total number of tasks generated: {total_tasks}
Total number of completed tasks: {complete}
Total number of incomplete tasks: {t_incomplete}
Total number of overdue tasks: {overdue}
Percentage of tasks that are incomplete: {per_not}%
Percentage of tasks that are overdue: {per_odue}% 

""")



        
#the admin section is the EXACT same as the other user section except that there are two extra options 
while username1 == 'admin':
    
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports 
ds - view statistics
e - Exit
: ''').lower()

#if the user enters r a new user will be added to the user.txt file
    if menu == 'r':
        reg_user()
            
                    
       
#if a is entered, a new task will be added to the file tasks.txt
    elif menu == 'a':
        add_task()
        #to include the date the task was assigned, the current date is imported from a built in python function
        
    elif menu == 'va':
        view_all()
                

#if the user enters vm, then only their tasks are printed out 
    elif menu == 'vm':
        view_mine()
        
     
#if the user enters s then information about the number of users and number of tasks is extracted from both files 
    elif menu == 'ds':
        stats()
    
    elif menu == "gr":
        reports()

                
#the last option is entered when the user is done with task_manager.py, the loop breaks and the code stops
    elif menu == 'e':
        print('Goodbye!!!')
        break
    
#if none of the letters are entered then the user is prompted to enter a correct letter 
    else:
        print("You have made a wrong choice, Please Try again")
  
        
  #I am sure that there is a more efficient way to make it so only the admin has access to some features whereas other users do not
  #using def(function): and defining a new function could be used but i am rusty on that aspect so I simply copied the above code 
  #users that are not the admin only get access to the a,va,vm, and e options which are the same as the ones above so no new comments were added
        
while username1 != 'admin': 
    
            
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

#if the user enters r a new user will be added to the user.txt file
    if menu == 'r':
        reg_user()
                              
       
#if a is entered, a new task will be added to the file tasks.txt
    elif menu == 'a':
        add_task()
    
#if va is entered all the tasks will be shows         
    elif menu == 'va':
        view_all()
                

#if the user enters vm, then only their tasks are printed out 
    elif menu == 'vm':
        view_mine()
         
    elif menu == 'e':
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please Try again")