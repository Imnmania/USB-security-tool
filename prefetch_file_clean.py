import os

def prefetch_file():

    asd=("C:\WINDOWS\Prefetch")
    returned_value = os.system("del " + '"' + asd + '"' + " /f")
    print("Prefetch Cleaning Complete= ",returned_value)