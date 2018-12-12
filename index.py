import os
from tkinter import *
from tkinter import messagebox
import subprocess
from shortcut_clean import shortcut
from cclean import ccleaner
from prefetch_file_clean import prefetch_file
from malware_clean import malware
from registry_clean import registryClear
import tkinter.filedialog as filedialog


main_window = Tk()
main_window.geometry("750x600")
main_window.configure(background="#474747")
main_window.title("USB SECURITY TOOL")


popup = Tk()
popup.eval('tk::PlaceWindow %s center' % popup.winfo_toplevel())
popup.withdraw()
#messagebox.showinfo('Output', 'Success !!!')
popup.deiconify()
popup.destroy()
popup.quit()



label_1 = Label(main_window, 
        text="USB SECURITY TOOL",
        bg="#474747" ,
        font=("corbel",35,"bold"),
        fg='#FFFFFF').place(x=160,y=85)



def Shortcut():
    print('returned value:', shortcut())
butn_1=Button(main_window, 
            text="Shortcut Remove",
            bg="#F7F0F0" ,
            font=("corbel",15,"bold"),
            borderwidth=3,
            height="2",
            width="15",
            command=Shortcut).place(x=280,y=170)


def CCleaner():
    
    print('returned value:', ccleaner())
butn_2=Button(main_window,
             text="C Cleaner",
             bg="#F7F0F0" ,
             font=("corbel",15,"bold"),
             borderwidth=3,
             height="2",
             width="15",
             command=CCleaner).place(x=280,y=240)
    


def registryClear():
    print("Registry Cleaning Complete= ",registryClear)
butn_3=Button(main_window,
                text="Registery Clean",
                bg="#F7F0F0" ,
                font=("corbel",
                15,"bold"),
                borderwidth=3,
                height="2",
                width="15",
                command=registryClear).place(x=280,y=310)


def Malware():
    p = print('returned value:', malware())
butn_4=Button(main_window, 
            text="Malware Remove",
            bg="#F7F0F0" ,
            font=("corbel",15,"bold"),
            borderwidth=3,
            height="2",
            width="15",
            command=Malware).place(x=280,y=380)



def Prefetch_clean():
    print('returned value:', prefetch_file())
butn_5=Button(main_window, 
            text="Prefetch Clean",
            bg="#F7F0F0" ,
            font=("corbel",15,"bold"),
            borderwidth=3,
            height="2",
            width="15",
            command=Prefetch_clean).place(x=280,y=450)


main_window.resizable(0,0)
main_window.mainloop()
