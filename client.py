import platform
from os import system
from termcolor import colored

code = input('Enter code to receive file: ')
saveAs = input('Save file as: ')
print('Receiving file...')
installedOs = platform.system()
if installedOs == 'Linux':
    system(f"wget -nv 192.168.100.{code.split('-')[0]}:{code.split('-')[1]}/{saveAs}")
    system('clear')
    print('File received')
elif installedOs == 'Windows':
    system(f"curl -O 192.168.100.{code.split('-')[0]}:{code.split('-')[1]}/{saveAs}")
    system('cls')
    print('File received')
else:
    print('Unknown operating system')
    print('NetShare can be used on Windows or Linux or Termux only')
