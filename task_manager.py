#=====importing libraries===========
# This import allows the program to access the date functions which
# will be used to access the current date.
import datetime 
import os.path

def reg_user():
    # The set_password boolean is used for the loop that checks whether the user has entered
    # the correct password.
    set_password = True
    set_username = True
    user = ""

    # This opens the user.txt file with read permissions.
    # The newline characters are replaced with commas and the spaces are replaced with nothing and stored in the user variable.
    # This variable is then split by commas and stored in a variable called credentials making them easier to access later.
    # The usernames are stored in a user variable by slicing the credentials variable starting at the first index position and
    # stepping through every two elements to match the format the usernames are stored in the user.txt file.
    with open('user.txt', 'r+') as f:
            for line in f:
                user += line
                user = user.replace('\n', ',')
                user = user.replace(' ', '')
            credentials = user.split(",") 
            user = credentials[0::2]

    # While the set_username variable is set to True, the user is asked to enter the new users, username until they enter one
    # that is not already in use.
    while set_username:
        new_username = input("Please enter the new username: ")

        if new_username in user:
            print("This user already exists. Please select a different username.")
        else:
            set_username = False

    # While the set_password variable is set to True, the user is asked to enter the new users, username and password. They are
    # asked to confirm the password.
    while set_password:
        new_password = input("Please enter the new password: ")
        confirm_password = input("Please re-enter the new password: ")

        # If both entries of the password match, the username and password are stored in a variable called new_credentials with a
        # comma appended to the end of the username and a space before the new password to maintain the same format in the text file.
        if confirm_password == new_password:
            new_credentials = new_username + ","
            new_credentials += " " + new_password
            set_password = False

            # This write the new_credentials variable into the user.txt file. If the passwords do not match then the user is asked to
            # start over from entering the username.
            with open('user.txt', 'a') as f:
                f.write('\n' + new_credentials)
        else:
            print("The passwords do not match please try again: ")
def add_task():
    # The current_date variable stores current date.
    current_date = datetime.datetime.now()

    # The user is asked to enter: who the task is assigned to, the title, the task description, the task date and the current date.
    # This information is then appended into relevant variables
    task_user = input("Who is this task assigned to: ")
    title = input("What is the title for this task: ")
    task_desc = input("What is the description of this task: ")
    task_date = input("What is the due date for this task: ")
    current_date = current_date.strftime('%d %b %y')

    # Below the variables are added to the new_task variable adding commas and spaces to maintain the same format in the tasks.txt
    new_task = task_user + (',')
    new_task += (' ') + title + (',')
    new_task += (' ') + task_desc + (',')
    new_task += (' ') + task_date + (',')
    new_task += (' ') + current_date + (',')
    new_task += (' ') + 'No'
        
    # The tasks.txt file is opened with append permissions which allows new elements to be added to the bottom of the file
    # The new_task variable is written to the tasks.txt file
    with open('tasks.txt', 'a') as f:
        f.write('\n' + new_task)
def view_all():
    # The all_tasks variable stores the contents of the tasks.txt file.
    all_tasks = ""
    # This opens the task.txt file with read/write permissions
    with open('tasks.txt', 'r+') as f:
        # This loop adds each line from the text file with a newline character to a variable called all_tasks
        #  and prints all the tasks to the user
        for line in f:
            all_tasks += line + ("\n")
        print(all_tasks)
def view_mine():
    task_selection = True
    my_task = ''
    current_task = ''
    all_tasks = ''
    tasks = ''
    tasks_to_write = ''
    index = 0
    # This opens the task.txt file with read/write permissions
    with open('tasks.txt', 'r+') as f:
        # This loop adds each line from the text file to a variable called my_task.
        # If the the current user's username is in the current line of the loop that line is added to the my_task variable.
        # The my_task variable is then added to a list called my_tasks. This is done by first splitting all the data by the commas
        # and then splitting the strings into to separate lists by splitting using the newline character.
        for line in f:
            if username in line:
                my_task += line
                my_tasks = [my_split_task.split(",") for my_split_task in my_task.split("\n")]

        # This loop is used to check that the username of the current user that is logged in matches the username in the task which,
        # is stored in the first index position of each list. 
        # If it matches then an ID number is appended to the list which matches the tasks index position in the list and all matching
        # tasks are printed to the user as a string.
        for task in my_tasks:
            if task[0] == username:
                task.insert(0,str(index))
                index += 1
                print(', '.join(task) + "")
    # This loop checks a boolean value to ensure that the user is not able to enter an incorrect value and continue 
    # through the program. 
    # If the user selects a valid task they a prompted to select some further options. If the user enters -1 they are taken
    # back to the main menu and, if they do not enter -1 or a valid ID number they are prompted to enter a number again.
    while task_selection:
        task_index = (input("\nPlease enter the ID of the task you'd like to select: \nTo return to the main menu enter '-1': "))
        for task in my_tasks:
            if task_index == task[0]:
                current_task = task
                task_selection = False
                break

            elif task_index == '-1':
                task_selection = False
                return
                                
            else: 
                print("You have not selected a valid option.")

     # The user is asked what action they would like to take. If the user chooses to mark the selected task as complete then
     # the date is changed and the updated task is printed to the user.   
    user_choice = input("\nWould you like to: \n1. Mark this task ask compelete\n2. Edit the task \n: ")

    # This if statement checks whether the task has already been completed. If is has not then the user is presented with
    # further options to edit the task.
    if user_choice == '1':
        if current_task[6] != ' Yes':
            current_task.remove(' No')
            current_task.append(' Yes')
            print(', '.join(current_task))
        
        # If the task is already marked as complete in the tasks.txt file then the user is informed.
        else:
            print("\nThis task has already been completed")
            return

    # If the user chooses to edit the task they are presented with further options. The user can choose to either edit the 
    # assigned user or edit the due date of the selected task.
    elif user_choice == '2':
        # This if statement checks whether the task has already been completed. If is has not then the user is presented with
        # further options to edit the task.
        if current_task[6] != ' Yes':
            edit_task = input("\nWould you like to: \n1. Edit the user\n2. Edit the due date \n: ")

            # If the user chooses to changed the user that the task is assigned to then they are asked for the new user. The current
            # users name is then removed from the task and the new users is added.
            if edit_task == '1':
                user_change = input("Who is the new user? ")
                current_task.pop(1)
                current_task.insert(1, user_change)
                print(" ")
                print(', '.join(current_task))

            # If the user chooses to edit the due date, they are asked what the new due date is. The old date is removed from the
            # task and the new date is added
            elif edit_task == '2':
                print(f"\nThe current due date is: {current_task[5]}")
                date_change = input("What would you like the new due date to be: ")
                current_task.pop(5)
                current_task.insert(5, date_change)
                print(', '.join(current_task))
        
        # If the task is already marked as complete in the tasks.txt file then the user is informed.
        else:
            print("\nThis task has already been completed")
            return

    # This opens the task.txt file with read/write permissions. All tasks from the file are read line by line and stored in the tasks
    # variable. Each line is then split by comma and split further into separate lists by the newline character.
    with open('tasks.txt', 'r+') as f:
        for line in f:
            tasks += line
            all_tasks = [split_tasks.split(",") for split_tasks in tasks.split("\n")]
    
    # This line removes the ID number from the task stored in current_task before writing it back into the file.
    current_task.pop(0)

    # This loop takes each item stored in the current_task list and compares the title with the title from the all_tasks list both,
    # of which are stored in the 1st index position of their respective lists. If they match the task is deleted from the all_task
    # list and replaced with the task stored in the current_list.
    for line in current_task:
        for count, task in enumerate(all_tasks):
            if current_task[1] == task[1]:
                all_tasks.pop(count)
                all_tasks.insert(count, current_task)

    # This loop joins each split element of the task line into one line and adds it to a new a new list called tasks_to_write with
    # a newline character to ensure each line appears as a new line in the txt file.
    for task in all_tasks:
        tasks_to_write += ','.join(task) + "\n"

   # This opens the tasks.txt file with write permissions and writes in each of the tasks stored in the tasks_to_write list to the
   # file, overwriting what was stored in the file before. 
    with open('tasks.txt', 'w') as f:
        for task in tasks_to_write:
            f.write(task)  
def generate_reports():
    current_date = datetime.datetime.now()
    my_task = ''
    all_tasks = ''
    number_of_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    incomplete_percentage = 0
    overdue_percentage = 0
    task_overview = []
   

    number_of_users = 0
    task_count = 0
    complete_count = 0
    incomplete_count = 0
    overdue_count = 0
    task_count_per_user = []
    task_percentage_per_user = []
    complete_tasks_count = []
    incomplete_tasks_count = []
    overdue_tasks_count = []
    completed_tasks_percentage = []
    incomplete_tasks_percentage = []
    overdue_tasks_percentage = []
    user_overview = []
    users = ''
    user_task_count = ''
    user_task_percentage = ''
    user_complete_percentage = ''
    user_incomplete_percentage = ''
    user_overdue_percentage = ''
    user_overview_string = ''

        
    # This opens the task.txt file with read/write permissions
    with open('tasks.txt', 'r+') as f:
        # This loop will add 1 to the number_of_tasks variable for every line in the tasks.txt
        # It will also take each task from the file and insert them into a list called all_tasks. The tasks are split by commas 
        # and then split further into separate lists within the list split by the new line character. 
        for line in f:
            number_of_tasks += 1
            my_task += line
            all_tasks = [my_split_task.split(",") for my_split_task in my_task.split("\n")]

        # This removes the final empty list element created by the final new line character when the tasks are written to the file.
        all_tasks.pop(-1)

        # This loop iterates through each task in the all task list. 
        for task in all_tasks:

            # This strips the space in front of the date stored in the 3rd element in the list then, it is converted into a 
            # datetime object and stored in a variable called due_date.
            task[3] = task[3].strip(" ")
            due_date = datetime.datetime.strptime(task[3], '%d %b %Y')

            # If the final element of each task is equal to " Yes" then 1 is added to the completed_tasks variable.
            if task[5] == " Yes":
                completed_tasks += 1

            # If the final element of each task is equal to " No" then 1 is added to the incomplete_tasks variable.
            elif task[5] == " No":
                incomplete_tasks += 1

                # If the current date is greater than the due date of the task then 1 is added to overdue_tasks variable
                if current_date > due_date:
                    overdue_tasks += 1
        
        # The following calculations give us the percentage value of incomplete tasks and overdue tasks and stores them in a
        # relevant variable.
        incomplete_percentage = incomplete_tasks / number_of_tasks * 100
        overdue_percentage = overdue_tasks / number_of_tasks * 100

        # The following block appends all the results of the above checks and calculations and stores them in a list.
        task_overview.append("Number of tasks: " + str(number_of_tasks))
        task_overview.append("Completed tasks: " + str(completed_tasks))
        task_overview.append("Incomplete tasks: " + str(incomplete_tasks))
        task_overview.append("Overdue tasks: " + str(overdue_tasks))
        task_overview.append("Percentage incomplete: " + str(round(incomplete_percentage, 2)))
        task_overview.append("Percentage overdue: " + str(round(overdue_percentage, 2)))

    # This opens the task_overview.txt file with write permissions. If it doesn't not exist then it is created. This file will be
    # overwritten every time this function is called so the values are updated.
    with open('task_overview.txt', 'w') as f:

        # This loop will iterate through the list and write each value to the task_overview.txt file with a newline character on the end.
        for item in task_overview:
            f.write(item + "\n")

    # This opens the user.txt file with read/write permissions
    with open('user.txt', 'r+') as f:
        # This loop will add 1 to the number_of_users variable for every line in the user.txt
        for line in f:
            number_of_users += 1

        # This loop checks iterates through each task in all_tasks. 
        for username in all_tasks:
            # If the username (which is stored in the 0 index position of each task in the list) is not in the users string then 
            # it is added with a comma and a space. This is then split into a list using the comma and the space and lastly the 
            # final blank space is removed.
            if username[0] not in users:
                users += username[0] + ", "
                user = users.split(", ")
                user.pop(-1)

        # This loop iterates through the list of users and the list of tasks. If the username in the user list matches the user in
        # the task then one is added to the task list. At the end a new list is created stating how many tasks is assigned to each 
        # user. 
        # The task_count is reset to 0 for each user.
        for username in user:
            for task in all_tasks:
                if task[0] == username:
                    task_count += 1
            user_task_count += "The " + username + " user has " + str(task_count) + " task(s) assigned to them, "
            task_count_per_user.append(task_count)
            task_count = 0
        user_task_count+= "\n"
        
        # This loop iterates through the list containing the task count for each user. The percentage is worked out by 
        # dividing the task count by the total number of tasks and multiplying by 100. The result is then stored in a new list
        # rounded to two digits.
        for task in task_count_per_user:
            user_percentage = task / number_of_tasks * 100
            task_percentage_per_user.append(str(round(user_percentage, 2)))
        
        # This loop uses the enumerate function and iterates through the task percentage per user list using the count function 
        # created by the enumerate function to move through the user list so that the correct user is selected with the correct
        # percentage. This is then stored in a string.
        for count, task in enumerate(task_percentage_per_user):
            user_task_percentage += "The " + user[count] + " user has " + task + "% of the total tasks assigned to them, "
        user_task_percentage += "\n"

        # This loop iterates through each username stored in the user list and each task in the all_tasks list.
        for username in user:
            for task in all_tasks:
                # This strips the leading space from the date and assigns it to a variable called due_date so we can compare it easily.
                task[3] = task[3].strip(" ")
                due_date = datetime.datetime.strptime(task[3], '%d %b %Y')

                # If the username in the task matches the name in the user list and the task is marked as completed then 1 is added
                # to the complete count variable.
                if task[0] == username and task[5] == ' Yes':
                    complete_count += 1
                # If the username in the task matches the name in the user list and the task is marked as incomplete then 1 is added
                # to the incomplete count variable.
                elif task[0] == username and task[5] == ' No':
                    incomplete_count += 1

                    # If the factors above are true and the due date is older than the current date then 1 is also added to the overdue
                    # count variable.
                    if current_date > due_date:
                        overdue_count += 1

            # Each total is appended to their relevant lists and the counts are all reset to 0 before moving on to the next user in the user list.
            complete_tasks_count.append(complete_count)
            incomplete_tasks_count.append(incomplete_count)
            overdue_tasks_count.append(overdue_count)
            complete_count = 0
            incomplete_count = 0
            overdue_count = 0

        # These loops use the zip function to iterate through two lists at the same time. This is done so that we can match the 
        # total tasks assigned to each user to the complete tasks, incomplete tasks and overdue tasks and calculate the percentages.
        # Once calculated they are appended to the relevant lists.
        for (total, complete) in zip(task_count_per_user, complete_tasks_count):
            complete_percentage = complete / total * 100
            completed_tasks_percentage.append(str(round(complete_percentage, 2)))
        
        for (total, incomplete) in zip(task_count_per_user, incomplete_tasks_count):
            incomplete_percentage = incomplete / total * 100
            incomplete_tasks_percentage.append(str(round(incomplete_percentage, 2)))

        for (total, overdue) in zip(task_count_per_user, overdue_tasks_count):
            overdue_percentage = overdue / total * 100
            overdue_tasks_percentage.append(str(round(overdue_percentage, 2)))
        
        # These loops use the enumerate function and iterate through the user complete percentage, user incomplete percentage and
        # user overdue percentage lists respectively, using the count function created by the enumerate function to move through 
        # the user list so that the correct user is selected with the correct percentage. This is then stored in a string with a 
        # newline character appended to the end to help keep the different groups separated.
        for count, task in enumerate(completed_tasks_percentage):
            user_complete_percentage += "The " + user[count] + " user has " + task + "% of the total tasks assigned to them marked as complete, "
        user_complete_percentage += "\n"

        for count, task in enumerate(incomplete_tasks_percentage):
            user_incomplete_percentage += "The " + user[count] + " user has " + task + "% of the total tasks assigned to them marked as incomplete, "
        user_incomplete_percentage += "\n"

        for count, task in enumerate(overdue_tasks_percentage):
            user_overdue_percentage += "The " + user[count] + " user has " + task + "% of the total tasks assigned to them marked as incomplete and overdue, "
        user_overdue_percentage += "\n"

    # The following block appends all the results of the above checks and calculations and stores them in a list.
    user_overview.append(f"There are {number_of_users} user(s)")
    user_overview.append("\n")
    user_overview.append(user_task_count)
    user_overview.append(user_task_percentage)
    user_overview.append(user_complete_percentage)
    user_overview.append(user_incomplete_percentage)
    user_overview.append(user_overdue_percentage)

    # This loop iterates through the user_overview list and adds each element to a string called user_overview_string.
    # This string is then split by the commas and space and the end of each element as well as by the new line characters
    # at the end of each group which creates a list of lists.
    for element in user_overview:
        user_overview_string += element        
        users_overview = [my_split_users.split(", ") for my_split_users in user_overview_string.split("\n")]
    
    # This removes the empty element at the end of the users_overview list.
    users_overview.pop(-1)

    # This loop removes the empty element at the end of each list contained in the users_overview list.
    for user in users_overview[1:]:
        user.pop(-1)

 # This opens the user_overview.txt file with write permissions. If it doesn't not exist then it is created. This file will be
    # overwritten every time this function is called so the values are updated.
    with open('user_overview.txt', 'w') as f:

        # The outer loop will iterate through the list containing all the lists. 
        for item in users_overview:
            # The inner loop iterates through each element of the lists and writes each value to the user_overview.txt file 
            # with a newline character on the end.
            for element in item:
                f.write(element + "\n")
            
            # This adds a newline between each separate peice of information making it easier to see which are related and 
            # which are different.
            f.write("\n")

def view_stats():

    # These two variables store a boolean value of True or False depending on whether the task_overview and user_overview files 
    # have been created yet.
    task_file_exists = os.path.exists('task_overview.txt')
    user_file_exists = os.path.exists('user_overview.txt')

    # If the task_overview.txt file does not exist yet then the generate reports function is called before being displayed to
    # the user.
    if task_file_exists == False:
        generate_reports()

    # If the user_overview.txt file does not exist yet then the generate reports function is called before being displayed to
    # the user.
    if user_file_exists == False:
        generate_reports()

    # This opens the task_overview.txt file with read/write permissions
    with open('task_overview.txt', 'r+') as f:
        print("Task Overview:\n")
        # This loop will print each line in the task_overview.txt file
        for line in f:
            print(line)
            
    # This opens the user_overview.txt file with read/write permissions
    with open('user_overview.txt', 'r+') as f:
        print("User Overview: \n")
        # This loop will print each line in the user_overview.txt file
        for line in f:
            print(line)

# The passw and user variables are used to store the values from the file.
# The username and password variables are used to store the user input.
# The login boolean is used for the while loops in the login section.
passw = ""
user = ""
login = True


#====Login Section====
# This opens the user.txt file with read permissions.
# The newline characters are replaced with commas and the spaces are replaced with nothing and stored in the user variable.
# This variable is then split by commas and stored in a variable called credentials making them easier to access later.
# The usernames are stored in a user variable by slicing the credentials variable starting at the first index position and
# stepping through every two elements to match the format the usernames are stored in the user.txt file.
# The passwords are stored in a passw variable by slicing the credentials variable starting at the second index position and
# stepping through every two elements to match the format the passwords are stored in the user.txt file.
with open('user.txt', 'r+') as f:
    for line in f:
        user += line
        user = user.replace('\n', ',')
        user = user.replace(' ', '')
    credentials = user.split(",") 
    user = credentials[0::2]
    passw = credentials[1::2]
 
 # This loop is used to repeatedly check whether the user has entered the correct username by comparing the user enters with what
 # is stored in the username variable. If they do not match the user is asked to try again.
while login:
    username = input("\nPlease enter your username: ")
    if username in user:
        print("Your username is correct")
        login = False
    else:
        login = True
        print("You username is incorrect, please try again.")

 # This loop is used to repeatedly check whether the user has entered the correct password by comparing what the user enters with what
 # is stored in the password variable. If they do not match the user is asked to try again.
login = True

while login:
    password = input("Please enter your password: ")
    if password in passw:
        print("Your password is correct")
        login = False
    else:
        print("Your password is incorrect")
        login = True

while True:
    if username == 'admin':
        # Presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        # A new menu option is added if the user has logged in as the admin user.
        menu = input('''\nSelect one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - View statictics
        e - Exit
        : ''').lower()
    
    else:
        # Presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        menu = input('''\nSelect one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    # If the user selects option r in the menu the username is checked. If the user is logged in as an admiin, the red_user()
    # function is called and the user is prompted to add a new user.
    # If the user is not logged in as an admin they are shown an error message and returned to the main menu.
    if menu == 'r':
        if username != 'admin':
            print("Sorry you must be logged in as admin to complete this action.")
            continue
        
        else:
            reg_user()
            
    # If the user selects option a in the menu, the add_task() function is called and the user is prompted to add a new task.
    elif menu == 'a':
        add_task()

    # If the user selects option va in the menu, the view_all() function is called and the user is shown all the tasks on the file.
    elif menu == 'va':
        view_all()

    # If the user selects option vm in the menu, the view_mine() function is called and the user is shown all the tasks assigned to 
    # them from the file
    elif menu == 'vm':
        view_mine()

    # If the user selects option gr in the menu, the generate_reports() function is called. Two files are generated and populated with
    # the relevant information.
    elif menu == 'gr' and username == 'admin':
        generate_reports()
    
    # If the admin selects option s in the menu, the view_stats() function is called and the user is shown the count of all 
    # users and all tasks
    elif menu == 'ds'and username == 'admin':
        view_stats()

    # If the user selects option e in the menu the goodbye message is displayed and the program ends
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If at the selection stage the user hasn't selected an option from the menu but entered something else they are prompted
    # to try again and the loop interates
    else:
        print("You have made a wrong choice, Please Try again")