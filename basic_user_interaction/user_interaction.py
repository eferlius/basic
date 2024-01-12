# -*- coding: utf-8 -*-
import keyboard

def chose_option_list(listOfOptions):
    ''' Given a list of options, displays them and asks for the index of the corresponding one'''
    for i, opt in zip(range(len(listOfOptions)), listOfOptions):
        print('{:02d} - {}'.format(i, opt))
    print('{:02d} - {}'.format(-1, 'None')) 
    while True:
        ans = input('choice: ')
        try:
            ans = int(ans)
            if ans <= len(listOfOptions) and ans >= 0:
                choice = listOfOptions[ans]
            elif ans == -1:
                choice = None
            print('[{}] was chosen'.format(choice))
            return choice
        except:
            pass
        print('not valid input')

def chose_TF(question = 'True or False?'):    
    while True:
        ans = input('{} [f, n, 0] or [t, y, 1]: '.format(question))
        try:
            if ans.lower() in ['t', 'true', 'y', 'yes', '1']:
                return True
            elif ans.lower() in ['f', 'false', 'n', 'no', '0']:
                return False
            elif ans == '-1':
                return None
        except:
            pass
        print('not valid input')
        
def chose_TF_keyboard(question = 'True or False?'):  
    print('{} [f, n, 0] or [t, y, 1]: '.format(question))
    while True:
        print('waiting for keyboard input...')
        ans = keyboard.read_hotkey(suppress=False)
        print('['+ ans+'] pressed')
        if ans.lower() in ['t', 'y', '1']:
            return True
        elif ans.lower() in ['f', 'n', '0']:
            return False
        if ans == 'esc':
            return None
        else:
            print('not valid input')