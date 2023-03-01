import os

# Function doesn't receive parameters
# Cleans the terminal
# Function doesn't return value
def clear():
    os.system('cls')


# Function doesn't receive parameters
# Show the initial menu
# Function return the value from the selection of the menu
def menu():
    clear()
    print('='*10)
    print('1 - Adm \n2 - Client \n0 - Exit')
    print('='*10)

    try:
        selection = int(input('-> '))
    except:
        clear()
        return menu()
    
    if(selection == 1) or (selection == 2) or (selection == 0):
        return selection
    else:
        clear()
        return menu()

# Function doesn't receive parameters
# Show the adm menu
# Function return the value from the selection of the adm menu 
def adm_menu():
    clear()
    print('='*19)
    print('1 - Change password \n2 - List clients \n3 - Register client \n4 - Remove client \n0 - Exit')
    print('='*19)

    try:
        selection = int(input('-> '))
    except:
        clear()
        return menu()
    
    if(selection == 1) or (selection == 2) or (selection == 3) or (selection == 4) or (selection == 0):
        return selection
    else:
        clear()
        return menu()

# Function doesn't receive parameters
# Show the client menu
# Function return the value from the selection of the client menu
def client_menu():
    clear()
    print('='*19)
    print('1 - Account data \n2 - Change password \n3 - Withdraw \n4 - Deposit \n0 - Exit')
    print('='*19)

    try:
        selection = int(input('-> '))
    except:
        clear()
        return menu()
    
    if(selection == 1) or (selection == 2) or (selection == 3) or (selection == 4) or (selection == 0):
        return selection
    else:
        clear()
        return menu()

# Function doesn't receive parameters
# login section of the adm, it read from a file an archive with the password if the archive doesn't exist the function create
# "adm_password.txt" with the default password "0000", the function compare the password with the input from the user
# Function return 1 if the password typed by the user is correct
# else it return 0
def adm_login():
    clear()
    try:
        file = open('adm_password.txt','r')
    except:
        file = open('adm_password.txt','w')
        file.write('0000')
        file.close()
        file = open('adm_password.txt','r')  

    password = file.readlines()
    file.close()

    print('='*15)
    print('insert password')
    print('='*15)
    type = input('-> ')
    if type == password[0]:
        print('Valid input')
        a = input('press enter to continue... ')
        return 1
    else:
        print('Invalid input')
        a = input('press enter to continue... ')
        return 0

# Function doesn't receive parameters
# Ask for the users the actual adm password, then ask for the new adm password and then do the replacement
# Function doesn't return value
def adm_change_password():
    clear()
    file = open('adm_password.txt','r')
    old = file.readlines()
    file.close()
    print('='*22)
    print('insert actual password')
    print('='*22)
    type = input('-> ')
    if type == old[0]:
        file = open('adm_password.txt','w')
        new = input('Insert new password: ')
        file.write(new)
        print('Password changed successfully')
        a = input('press enter to continue... ')
    else:
        print('Invalid input')
        a = input('press enter to continue... ')
    file.close()

# Function receive as parameters, a string that is a line from the file of the clients data
# and a variable that select a instruction for the function
# Each data from a line in the file "client_data" is separated by a coma, the selection determine wich data it will return
# Function return a string with the data from the determinated selection, or it will return 0 if the selection is unavailable
def pick_client_data(line, sel):
    coma_counter = 0
    data = ''
    if sel == 0:
        for i in line:
            if i == ',':
                coma_counter += 1
            if (coma_counter == 0) and (i != ','):
                data = data + i
        return data
    elif sel == 1:
        for i in line:
            if i == ',':
                coma_counter += 1
            if (coma_counter == 1) and (i != ','):
                data = data + i
        return data
    elif sel == 2:
        for i in line:
            if i == ',':
                coma_counter += 1
            if (coma_counter == 2) and (i != ','):
                data = data + i
        return data
    elif sel == 3:
        for i in line:
            if i == ',':
                coma_counter += 1
            if (coma_counter == 3) and (i != ',') and (i != '\n'):
                data = data + i
        return data
    else:
        return 0

# Function doesn't receive parameters
# Reads the file with the data of the client, then list all the data in a formatted table
# Function doesn't return value
def adm_list_clients():
    clear()
    try:
        file = open('client_data.txt')
    except:
        print('There are any client registered')
        a = input('press enter to continue... ')
    else:
        clients = file.readlines()
        print('Code |Username' + ' '*22 + '|Password' + ' '*12 + '|Balance ')
        for i in clients:
            code = pick_client_data(i,0)
            username = pick_client_data(i,1)
            password = pick_client_data(i,2)
            balance = pick_client_data(i,3)
            print(f'{code}|{username}' + ((30 - len(username)) * ' ') + f'|{password}' + ((20 - len(password)) * ' ') + f'|{balance}')
        a = input('press enter to continue... ')


# Function doesn't receive parameters
# It add's a new client to the system, it ask for the username and password for the new client and generates automatically a new code for the account
# Function doesn't return value
def adm_add_client():
    clear()
    counter = 0
    try:
        file = open('client_data.txt','r+')
    except:
        file = open('client_data.txt','w')
        file.close()
        file = open('client_data.txt','r+')  
    print('='*22)
    print('insert the username')
    print('='*22)
    while 1:
        username = input('-> ')
        if (len(username) <= 30) and (username != ''):
            break

    codes = file.readlines()
    try:
        counter = pick_client_data(codes[-1],0)
    except:
        counter = '00000'

    counter = int(counter)
    counter += 1
    counter = str(counter)
    code = (5 - len(str(counter))) * '0' + f'{str(counter)}' 
    
    print('='*22)
    print('insert the password')
    print('='*22)
    while 1:
        password = input('-> ')
        if (len(password) <= 30) and (password != ''):
            break

    clear()
    print('='*len('Username: ' + username))
    print(f'Username: {username} \nCode: {code} \nPassword: {password}')
    print('1 - confirm \n0 - cancel')
    print('='*len('Username: ' + username))
    while 1:
        try:
            sel = int(input('-> '))
        except:
            print('invalid selection')
        else:
            if (sel == 1) or (sel == 0):
                break
            else:
                print('invalid selection')
    
    if sel == 1:
        client = code + ',' + username + ',' + password + ',' +'0.0' + '\n'
        file.write(client)
        print('Client added')
        a = input('press enter to continue... ')
    else:
        print('Client cancelled')
        a = input('press enter to continue... ')
    
    file.close()

#Function doesn't receive parameters
#Ask the user of the client that the adm want to remove, then remove it from de file "client_data.txt"
#Function doesn't return value
def adm_remove_client():
    clear()
    try:
        file = open('client_data.txt','r')
    except:
        print('There are any client registered')
        a = input('press enter to continue... ')
    else:
        found = 0
        lines = file.readlines()
        codes = []
        for i in lines:
            codes.append(pick_client_data(i,0))
        print('='*39)
        print('insert the code of the client to remove')
        print('='*39)
        remove = input('-> ')

        for i in codes:
            if i == remove:
                found = 1
                break
        
        if found == 1:
            for i in lines:
                if remove == pick_client_data(i,0):
                    line_remove = i
                    break
            c = pick_client_data(line_remove,0)
            u = pick_client_data(line_remove,1)
            p = pick_client_data(line_remove,2)
            b = pick_client_data(line_remove,3)

            print('Client to be removed')
            print('='*len('Username: ' + u))
            print(f'Username: {u} \nCode: {c} \nPassword: {p} \nBalance: {b}')
            print('1 - confirm \n0 - cancel')
            print('='*len('Username: ' + u))
            while 1:
                try:
                    sel = int(input('-> '))
                except:
                    print('invalid selection')
                else:
                    if (sel == 1) or (sel == 0):
                        break
                    else:
                        print('invalid selection')
        
            if sel == 1:
                counter = 0
                for i in lines:
                    counter += 1
                    if i == line_remove:
                        break
                lines.pop(counter - 1)

                file.close()
                file = open('client_data.txt','w')
                file.close()
                file = open('client_data.txt','a')
                for i in lines:
                    file.write(i)
                print('Client removed')
                a = input('press enter to continue... ')
            else:
                print('Client keeped')
                a = input('press enter to continue... ') 

        else:
            print('Inexistent code')
            a = input('press enter to continue... ')
        file.close()

# Function doesn't receive parameters
# Login section of the user, that ask's for the code and the password of the user
# Function return a string that contains the line of the user if the user inserted the correct credentials
# else if anything goes wrong during he login, it will return 0
def client_login():
    clear()
    try:
        file = open('client_data.txt','r')
    except:
        print('There are any client registered')
        a = input('press enter to continue... ')
        return 0
    else:
        found = 0
        lines = file.readlines()
        
        print('='*20)
        print('Insert your code')
        print('='*20)
        code = input('-> ')

        for i in lines:
            if code == pick_client_data(i,0):
                client_line = i
                found = 1
                break
        
        if found == 1:
            print('='*20)
            print('Insert your password')
            print('='*20)
            password = input('-> ')

            if password == pick_client_data(client_line,2):
                file.close()
                return(client_line)
            else:
                print('Wrong password')
                a = input('press enter to continue... ')
                file.close()
                return 0
        else:
            print('Inexistent code')
            a = input('press enter to continue... ')
            file.close()
            return 0

# Function receive as a parameter a string that is a line that represents the data from the user
# Show the data of the user]
# Function doesn't return value
def client_show_data(line):
    clear()
    code = pick_client_data(line,0)
    username = pick_client_data(line,1)
    balance = pick_client_data(line,3)

    print('='*len(username))
    print(f'{username}\n{code}\n\n$ {balance}') 
    print('='*len(username))
    a = input('\npress enter to continue... ')

# Function receive as a parameter a string that is a line that represents the alterated data of the user
# Register in the file the modification of the data of the user
# Function doesn't return value
def register_client_mod(line):
    file = open('client_data.txt','r')
    lines = file.readlines()
    counter = 0
    found = 0

    for i in lines:
        counter += 1
        if pick_client_data(i,0) == pick_client_data(line,0):
            lines[counter - 1] = line
            found = 1
            break
    
    file.close()
    if found == 1:
        file = open('client_data.txt','w')
        for i in lines:
            file.write(i) 
        file.close()

# Function receive as a parameter a string that is a line that represents the data from the user
# Ask's the user for the password then if it is correct ask's for the new password
# Function doesn't return value
def client_change_password(line):
    clear()
    password = pick_client_data(line,2)
    print('='*22)
    print('insert actual password')
    print('='*22)
    type = input('-> ')
    if type == password:
        print('Insert new password')
        new_password = input('-> ')

        code = pick_client_data(line,0)
        username = pick_client_data(line,1)
        balance = pick_client_data(line,3)

        line = code + ',' + username + ',' + new_password + ',' + balance + '\n'
        register_client_mod(line)

        print('Password changed successfully')
        a = input('press enter to continue... ')
    else:
        print('Invalid input')
        a = input('press enter to continue... ')
    
    return line

# Function receive as a parameter a string that is a line that represents the data from the user
# Ask's to the user how much it is to deposit in the account
# Function doesn't return value
def client_deposit(line):
    clear()
    balance = pick_client_data(line,3)

    print('='*27)
    print(f'Balance: $ {balance}')
    print('insert the value to deposit')
    print('='*27)

    balance = float(balance)
    try:
        deposit = float(input('-> '))
    except:
        print('Invalid deposit')
        a = input('press enter to continue... ')
    else:
        new_balance = balance + deposit
        new_balance = str(new_balance)
        
        code = pick_client_data(line,0)
        username = pick_client_data(line,1)
        password = pick_client_data(line,2)

        line = code + ',' + username + ',' + password + ',' + new_balance + '\n'
        register_client_mod(line)

        print('Confirmed deposit')
        a = input('press enter to continue... ')
    
    return line

# Function receive as a parameter a string that is a line that represents the data from the user
# Ask's to the user how much it is to withdraw from the account, just do it if the user have the sufficient balance
# Function doesn't return value
def client_withdraw(line):
    clear()
    balance = pick_client_data(line,3)

    print('='*28)
    print(f'Balance: $ {balance}')
    print('insert the value to withdraw')
    print('='*28)

    balance = float(balance)
    try:
        withdraw = float(input('-> '))
    except:
        print('Invalid withdraw')
        a = input('press enter to continue... ')
    else:
        if withdraw <= balance:
            new_balance = balance - withdraw
            new_balance = str(new_balance)
            
            code = pick_client_data(line,0)
            username = pick_client_data(line,1)
            password = pick_client_data(line,2)

            line = code + ',' + username + ',' + password + ',' + new_balance + '\n'
            register_client_mod(line)

            print('Confirmed withdraw')
            a = input('press enter to continue... ')
        else:
            print('Invalid withdraw')
            a = input('press enter to continue... ')
    
    return line


    


            




        

        
    
            
    
    
    


    
    
