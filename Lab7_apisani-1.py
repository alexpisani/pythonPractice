# Lab7_apisani-1.py
# Alex Pisani
# June 24 2024
# takes a username and case-sensitive password as input and either rejects or accepts and assigns a security level


emp_login = {'john': 'heLLo2','jane': 'heLLo3','steve': 'heLLo4','sue': 'heLLo5','guest': 'guest'}
sec_level = {'john': 1, 'jane': 2, 'steve': 3, 'sue': 3, 'guest': 4}
user = input('Please enter username: ')
if user.lower() not in emp_login:
    print ('That is not an active username. Goodbye.')
else:
    password = input('Please enter password: ')
    
    while emp_login.get(user.lower()) == password:
        if sec_level.get(user.lower()) == 1:
            print (f'Welcome {user.capitalize()}. You are logged in as the Administrator.')
        elif sec_level.get(user.lower()) == 2:
            print (f'Welcome {user.capitalize()}. You are logged in as a manager.')
        elif sec_level.get(user.lower()) == 3:
            print (f'Welcome {user.capitalize()}. You are logged in as an employee.')
        elif sec_level.get(user.lower()) == 4:
            print (f'Welcome {user.capitalize()}. You are logged in as a guest.')
        break
    else:
        print ('Wrong password. Goodbye.')