from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('ToDoList')
ws.config(bg = '#2A52BE')
ws.resizable(width = False, height = False)

frame = Frame(ws)
frame.pack(pady = 10)

lb = Listbox(frame, width = 25, height = 8, font =('Helvetica', 15), bd = 0, fg = '#464646',
             highlightthickness = 0, selectbackground = '#a6a6a6', activestyle = "none",)

lb.pack(side = LEFT, fill = BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side = RIGHT, fill = BOTH)

lb.config(yscrollcommand = sb.set)
sb.config(command = lb.yview)

my_entry = Entry(ws, font = ('Helvetica', 14))

my_entry.pack(pady = 20)

button_frame = Frame(ws)
button_frame.pack(pady = 20)

addTask_btn = Button(button_frame, text = 'Add Task', font = ('Helvetica 14'),
    bg = '#c5f776', padx = 20, pady = 10, command = newTask)

addTask_btn.pack(fill = BOTH, expand = True, side = LEFT)

delTask_btn = Button(button_frame, text = 'Delete Task', font=('Helvetica 14'),
    bg='#ff8b61', padx = 20, pady = 10, command = deleteTask)

delTask_btn.pack(fill = BOTH, expand = True, side = LEFT)


ws.mainloop()
