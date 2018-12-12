from tkinter import *
import os
import tkinter.filedialog as filedialog


def shortcut():
    print("Shortcut Removed")
    #cmd = "attrib -h -r -s /s /d D:\\.............new\\Documents\\Shortcut remover\\files\\*.*- Shortcut"
    #returned_value = os.system("del /f D:\\.............new\\Documents\\Shortcut remover\\files\\*.*- Shortcut")
    #back = "attrib -h -r -s /s /d E:\*.*"
    asd = filedialog.askdirectory()
    returned_value = os.system("del " + '"' + asd + "\*.lnk" + '"' + " /f")
    print("return value: ", returned_value())
