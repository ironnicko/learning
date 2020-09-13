import os

cwd = os.getcwd()#current dir

os.mkdir(f'{input('Name of Directory:')}')
os.rmdir(f'{input('Name:')}')

os.remove(f'{input('Name of file to remove:')}')

os.chdir(f'{input('Change Directory:')}')
os.listdir(f'{input('Path:')}')
           
os.system(f'{input('The terminal command')}')
