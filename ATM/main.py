import func

while 1:
    sel = func.menu()
    if sel == 1:
        a = func.adm_login()
        if a == 1:
            while 1:
                adm_sel = func.adm_menu()
                if adm_sel == 1:
                    func.adm_change_password()
                elif adm_sel == 2:
                    func.adm_list_clients()
                elif adm_sel == 3:
                    func.adm_add_client()
                elif adm_sel == 4:
                    func.adm_remove_client()
                elif adm_sel == 0:
                    break
    elif sel == 2:
        b = func.client_login()
        if b != 0:
            line = str(b)
            while 1:
                client_sel = func.client_menu()
                if client_sel == 1:
                    func.client_show_data(line)
                elif client_sel == 2:
                    line = func.client_change_password(line)
                elif client_sel == 3:
                    line = func.client_withdraw(line)
                elif client_sel == 4:
                    line = func.client_deposit(line)
                elif client_sel == 0:
                    break                
    elif sel == 0:
        break

func.clear()
print('='*13)
print('Program ended')
print('='*13)

