import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import subprocess

window = Tk()
window.title('PYoneer - IDE V1.0') 
window.geometry('1280x720+150+80') # Window size when opened up
window.configure(bg='#333333')
window.resizable(False,False) # Stops it from resizing

#File Path
file_path = ''


#Functions
def set_file_path(path):
    global file_path
    file_path = path

def run_code():
    if file_path=='':
        messagebox.showerror('PYoneer - Error', 'Please save your code') # Stops user from running code that isn't saved.
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END) # Cleares Terminal when new code is run.
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
    


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        code_input.delete('1.0', END)
        code_input.insert('1.0', code)
        set_file_path(path)

def save_file():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    
    with open(path, 'w') as file:
        code = code_input.get('1.0', END)
        file.write(code)
        set_file_path(path)


# Central Window Icon:
icon = PhotoImage(file="pythonicon.png")
window.iconphoto(False, icon)

# Main Area for writing code.
code_input = Text(window, font='cosolas 18',bg='#cfcfce', fg='black')
code_input.place(x=180,y=0,width=680,height=720)

# Terminal 
code_output = Text(window, font='consolas 15', bg='#333333', fg='lightgreen')
code_output.place(x=860,y=0,width=420,height=720)

# Buttons
run_icon=PhotoImage(file='run.png')
open_icon=PhotoImage(file='open.png')
save_icon=PhotoImage(file='save.png')

Button(window, image=run_icon, bg='#333333', bd=0, activebackground='#333333', command=run_code).place(x=35,y=30)
Button(window, image=open_icon, bg='#333333', bd=0, activebackground='#333333', command=open_file).place(x=35,y=145)
Button(window, image=save_icon, bg='#333333', bd=0, activebackground='#333333', command=save_file).place(x=35,y=260)

window.mainloop()