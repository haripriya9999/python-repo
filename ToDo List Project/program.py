import os
from colorama import init, Fore

def main():
    status = True
    while status:
        os.system('cls')
        print('============Your awesome TODO list buddy==================')
        print(Fore.LIGHTYELLOW_EX)
        glanceMessage(howMany())
        print(Fore.RESET + 'Options:')
        print('\t1. Add new to do lists')
        print('\t2. View all your to do lists')
        print('\t3. Delete message...')
        print('\t4. Archieve message...')
        print('\t5. Exit program...')

        print()
        print('Please enter your choice (1-5) and press ENTER:')
        respond = int(input(Fore.LIGHTCYAN_EX + '> '))
        print(Fore.RESET)

        while respond < 1 or respond > 5:
            print(Fore.LIGHTRED_EX + 'Your input is invalid!')
            print(Fore.RESET + 'Please re-enter')

            respond = int(input(Fore.LIGHTCYAN_EX + '> '))
            print(Fore.RESET)
        
        # no switch in python?

        if respond == 1:
            addNewList()
        elif respond == 2:
            showLists()
        elif respond == 3:
            deleteMessage()
        elif respond == 4:
            archieveMessage()
        else:
            status = exitProgram()

def exitProgram():
    os.system('cls')
    print('Are you sure you want to quit? (Y/N)')
    respond = input(Fore.LIGHTCYAN_EX + '> ')
    print()

    respond = respond.strip().upper()
    
    if respond == 'Y':
        print('Goodbye :(')
        return False
    elif respond == 'N':
        print('Returning to main menu :)')
        return True

def addNewList():
    os.system('cls')
    print('-----------------Add New List--------------------')
    print()
    data = open('TodoList.txt', 'a')
    dataTags = open('TodoListTags.txt', 'a')
    print('Enter the message you want to add to the list')
    text = input(Fore.LIGHTCYAN_EX + "You can cancel adding by entering digit '0'\n\n> ")
    
    if text != '0':
        data.writelines(text + '\n')
        print(Fore.LIGHTYELLOW_EX)
        print('\tAssign tags to your notes: 1) Urgent! 2) Important! 3) Bussiness 4) Personal 5) Others')
        optTags = int(input(Fore.LIGHTCYAN_EX + '\t> '))
        while optTags < 1 or optTags > 5:
            print('\tOut of range!')
            optTags = int(input(Fore.LIGHTCYAN_EX + '\tPlease re-enter: '))

        if optTags == 1:
            dataTags.writelines('Urgent!\n')
        elif optTags == 2:
            dataTags.writelines('Important!\n')
        elif optTags == 3:
            dataTags.writelines('Bussiness\n')
        elif optTags == 4:
            dataTags.writelines('Personal\n')
        else:
            dataTags.writelines('Others\n')
        
        print(Fore.LIGHTGREEN_EX + 'Message successfully saved!')
    
    data.close()
    dataTags.close()

    print('\n')
    input(Fore.GREEN + 'Hit ENTER to return to main menu')

def showLists():
    os.system('cls')
    # one for message and one for tags
    data = open('ToDoList.txt', 'r')
    dataTags = open('TodoListTags.txt', 'r')
    contentTags = dataTags.readlines()
    content = data.readlines()
    data.close()
    dataTags.close()

    if len(content) > 0:
        print('-----------Your To-Do Lists--------------')
        print('No.\t  Your To-Do \t\t\t\t\t  Tags')
        print()

        for message in range(len(content)):
            print('{0}. {1:<50} {2:>12}'.format(message+1, content[message].strip('\n'), contentTags[message]), end='')
    else:
        print('Seem empty :(')
        print('Nothing to show')

    print('\n')
    input(Fore.GREEN + 'Press ENTER key to return to main menu...')

def howMany():
    count = open('TodoList.txt', 'r')
    content = count.readlines()
    count.close()

    return len(content)

def glanceMessage(x):
    if x == 0:
	    print(':) Add some notes to your list')
    elif x == 1:
        print(f'Currently you has {x} thing to do!')
    else:
	    print(f'Currently you have {x} things to do!')

    print()

def deleteMessage():
    os.system('cls')
    print('--------------Delete message in your list----------------------')
    print("Once deleted, its gone forever. You can also choose 'archieve' feature in main menu\n\n") # I use "" because this string has ''
    data1 = open('TodoList.txt', 'r') # open for reading
    dataTags = open('TodoListTags.txt', 'r')
    contentTags = dataTags.readlines()
    content = data1.readlines()
    data1.close()
    dataTags.close()

    print()
    print('--------Glance to your To-Do Lists--------')
    print('No.\t  Your To-Do')
    print()

    length = 15

    for message in range(len(content)):
        if len(content[message]) <= length:
            print('{0}.   {1}'.format(message+1, content[message]), end='') # don't want to include '\n' which make newline
        else:
            print('{0}.   {1}...'.format(message+1, content[message][:length]))

    print('\n')

    if int(len(content)) > 0: # if there is a message inside txt file, run the statement below, else, just skipped
        choices = int(input(Fore.LIGHTCYAN_EX + 'Enter which number you want to delete its message: ')) # minus 1 because to match up with the array/list
        # print(f'Choices is {choices}')

        while choices < 1 or choices > len(content):
            print(Fore.LIGHTRED_EX)
            print(f'You entered number {choices} which mismatch any message')
            choices = int(input(Fore.LIGHTCYAN_EX + 'Please re-enter which number you want to delete its message: '))
        
        choices -= 1
        print('Are you sure you want to proceed? Your chosen message will deleted and no way to recover it! (Y/N)')
        confirmation = input(Fore.LIGHTCYAN_EX + '> ')

        confirmation = confirmation.strip().upper()

        if confirmation == 'Y':
            data2 = open('ToDoList.txt', 'w')
            data3 = open('TodoListTags.txt', 'w') # tags
            for i in range(len(content)):
                # print(f'i is {i}')
                if i != choices:
                    # print(content[i], end='')
                    data2.write(content[i])
                    data3.write(contentTags[i])
            data2.close()
            data3.close()
            
            print()
            print('Selected message successfully deleted')
        else:
            print('Nothing deleted. Enjoy your day :)')

    else:
        print('\tThere is no message in your toDo List right now.')
        print('\tNothing to delete')
        
    print()
    input(Fore.GREEN + 'Hit ENTER to return to main menu.')

def archieveMessage():
    os.system('cls')
    print("--------------Move to archieve----------------------")
    print("Message from your main list will be move to text file in your hard disk.\n")
    print("To permanently remove your message, choose 'Delete' feature in main menu instead\n\n")
    # combine delete feature and moving to new txt file

    data1 = open('TodoList.txt', 'r') # open for reading
    content = data1.readlines()
    data1.close()
    dataTags = open('TodoListTags.txt', 'r')
    contentTags = dataTags.readlines()
    dataTags.close()

    print()
    print('--------Glance to your To-Do Lists--------')
    print('No.\t  Your To-Do')
    print()

    length = 15

    for message in range(len(content)):
        if len(content[message]) <= length:
            print('{0}.   {1}'.format(message+1, content[message]), end='')
        else:
            print('{0}.   {1}...'.format(message+1, content[message][:length]))

    print('\n')

    if int(len(content)) > 0: # if there is a message inside txt file, run the statement below, else, just skipped
        data2 = open('ToDoList.txt', 'w')
        data3 = open('ToDoArchives.txt', 'a') # create new file / append if it already available
        data4 = open('TodoListTags.txt', 'w')
        choices = int(input(Fore.LIGHTCYAN_EX + 'Enter which number you want to archive its message: '))

        while choices < 1 or choices > len(content):
            print(f'You entered number {choices} which mismatch any message')
            choices = int(input(Fore.LIGHTCYAN_EX + 'Please re-nter which number you want to archieve its message: '))
        
        choices -= 1 # minus 1 because to match up with the array/list

        for i in range(len(content)):
            if i != choices: #delete
                data2.write(content[i])
                data4.write(contentTags[i])
            else: #archieve
                data3.write('--> '+ content[i])
        data2.close()
        data3.close()
        data4.close()
        
        print()
        print(Fore.LIGHTGREEN_EX + 'Selected message successfully removed to archive text file')

    else:
        print(Fore.LIGHTMAGENTA_EX + 'There is no message in your toDo List right now.')
        print('Nothing to archieve')
        
    print()
    input(Fore.GREEN + 'Hit ENTER to return to main menu.')

# def debug():
#     data = open('ToDoList.txt')
#     content = data.readlines()

#     print(len(content))

#     data.close()

# todo (sungguh ironi ye haahhaha)
# confirmation on deletion
# venv bagai colorama

if __name__ == "__main__":
    main()