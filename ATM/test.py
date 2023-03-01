import func    
line = '00002,Jao,0,50.0\n'

balance = func.pick_client_data(line,3)

print('='*22)
print(f'Balance: $ {balance}')
print('insert the value to withdraw')
print('='*22)

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
        
        code = func.pick_client_data(line,0)
        username = func.pick_client_data(line,1)
        password = func.pick_client_data(line,2)

        line = code + ',' + username + ',' + password + ',' + new_balance + '\n'
        func.register_client_mod(line)

        print('Confirmed withdraw')
        a = input('press enter to continue... ')
    else:
        print('Invalid withdraw')
        a = input('press enter to continue... ')