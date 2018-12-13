import os
import subprocess
from tkinter import *
from tkinter import messagebox

def ccleaner():
    '''
    print("C Cleaner")
    aa = ("C:\Windows\Temp")
    bb= "del /q/f/s %TEMP%\*"
    #cc= ("C:\Windows\$RECYCLE.BIN")
    #c:\$RECYCLE.BIN\
    returned_value = os.system("del " + '"' + aa + bb + '"' + " /f")
    print('returned value:', returned_value)
    '''

    
    del_dir = r'c:\windows\temp'
    pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
    rTup = pObj.communicate()
    rCod = pObj.returncode
    if rCod == 0:
        print ("Success: Cleaned Windows Temp Folder")
    else:
        print ("Fail: Unable to Clean Windows Temp Folder")