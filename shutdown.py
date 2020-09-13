import os, datetime

hour = int(input('Enter hour:'))
minute =  int(input('Enter min:'))

command = f'shutdown {hour}:{minute}'

os.system(command)#Bash/Terminal commands





