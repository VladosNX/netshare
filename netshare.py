from os import system
import platform
import sys
try:
    from termcolor import colored
except ModuleNotFoundError:
    print('Program cannot be started! Missing required module.')
    fixOrNo = input('Fix it now? [Y/N] ').lower()
    if fixOrNo == 'y':
        system('pip install termcolor')
        from termcolor import colored
    else:
        print('Canceled')
        exit()
        

installedOs = platform.system()
if installedOs == 'Windows':
    system('cls')
elif installedOs == 'Linux':
    system('clear')

print(colored(text='NetShare v1.0.1',color='blue'))
print('Main menu')
print('1. Send file')
print('2. Receive file')
try:
    action = input('> ')
except KeyboardInterrupt:
    exit()
if action == '1':
    import sendfile
elif action == '2':
    import client
else:
    print(colored(text='Unknown action',color='red'))
