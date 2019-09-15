from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox

employees = []

def update6():
    b6['state'] = DISABLED
    b7['state'] = NORMAL
    b2['state'] = DISABLED
    e1.insert(0,emp.getFirstname())
    e2.insert(0,emp.getLastname())
    e4.insert(0,emp.getDepartment())
    e5.insert(0,emp.getPosition())
    e6.insert(0,emp.getContact())
def update7():
    b6['state'] = NORMAL
    b7['state'] = DISABLED

    MsgBox = messagebox.askquestion ('Update Entry','Are you sure you want to Update an Entry',icon = 'warning')
    if MsgBox == 'yes':
        selected_item = tv.selection()[0]
        tv.item(selected_item, text=e1.get(),values=(e2.get(),self_gender.get(),e4.get(),e5.get(),e6.get()))
        e1.delete(0, END)
        e2.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        
    else:
        print("returning...")

    
    

        

def add_to_list():
    global emp
    
    print("Name: " + " " + e1.get(), e2.get() + "  " + "Gender: " + " " + self_gender.get()+ "  " +"Department: " + " " + e4.get()+ "  " +"Position: " + " " + e5.get()+ "  " + "Contact: " + " " + e6.get())
    emp = Employee(e1.get(), e2.get(),self_gender.get(),e4.get(),e5.get(),e6.get())
    a = e1.get()
    b = e2.get()
    c = self_gender.get()
    d = e4.get()
    e = e5.get()
    f = e6.get()
    employees.append(Employee(a,b,c,d,e,f))
    employees.append(emp)
    messagebox.showinfo("Dialog box", "Added On List")
    e1.delete(0, END)
    e2.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    b2['state'] = NORMAL



    

def read_list():
    tv.insert('','end', text=emp.getName(),values=(emp.getGender(),emp.getDepartment(), emp.getPosition(), emp.getContact()))
    window.i = window.i + 1
    b2['state'] = DISABLED





def exit_prog():
    MsgBox = messagebox.askquestion ('Exit ','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        print("welcome back!")




       
def delete_to_list():
        MsgBox = messagebox.askquestion ('Delete Entry','Are you sure you want to Delete an Entry',icon = 'warning')
        if MsgBox == 'yes':
            selected_item = tv.selection()
            remove_emp = tv.detach(selected_item)
            e1.delete(0, END)
            e2.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
        else:
            messagebox.showinfo('Return','You will now return to the application screen')


  
class Employee:
    def __init__(self, first_name, last_name, gender, department, position, contact):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.department = department
        self.position = position
        self.contact = contact
        
    def getName(self):
        return self.first_name + " " + self.last_name
    def getGender(self):
        self_gender.get()
        return self.gender
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position

    def getFirstname(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
    
    def getContact(self):
        return self.contact

window = Tk()
window.resizable(0, 0)
window.i = 0
self_gender = StringVar()




window.title("Character Registry")
Label(window, text="Name: ").grid(row=0, column=0, padx=10, pady=5)
Label(window, text="Race: ").grid(row=1, column=0, padx=10, pady=5)
r1 = Radiobutton(window, text="Male", value = "Male", variable=self_gender).grid(row = 2, column=0, padx=10, pady=5)
r2 = Radiobutton(window, text="Female", value = "Female",variable=self_gender).grid(row= 2, column=1, padx=10, pady=5)
Label(window, text="Clan: ").grid(row=3, column=0, padx=10, pady=5)
Label(window, text="Class: ").grid(row=4, column=0, padx=10, pady=5)
Label(window, text="Element: ").grid(row=0, column=2, padx=10, pady=5)



e1 = Entry(window, width=30)

e2 = Entry(window, width=30)
e4 = Entry(window, width=30)

e5 = Entry(window, width=30)

e6 = Entry(window, width=15)

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e4.grid(row=3, column=1, padx=10, pady=5)
e5.grid(row=4, column=1, padx=10, pady=5)
e6.grid(row=0, column=3, padx=10, pady=5)



b1 = Button(window, text="        Add        ", bg="orange", command=add_to_list)
b1.grid(row=0, column=4, padx=10, pady=5,columnspan=4)

b2 = Button(window, text="       Read       ",bg="red", command=read_list)
b2.grid(row=1, column=4, padx=10, pady=5,columnspan=4)


b4 = Button(window, text="      Delete      ",bg="green", command=delete_to_list)
b4.grid(row=2, column=4, padx=10, pady=5,columnspan=4)

b6 = Button(window, text="     Update     ",state=NORMAL, command=update6)
b6.grid(row=3, column=4 ,padx=10, pady=5, columnspan=4)



b5 = Button(window, text="        Exit         ",bg="yellow", command=exit_prog)
b5.grid(row=4, column=4 ,padx=10, pady=5,columnspan=4)

b7 = Button(window, text="     Update     ",bg="pink",state=DISABLED, command=update7)
b7.grid(row=6, column=4 ,padx=10, pady=5,columnspan=4)




tv = ttk.Treeview(window, height=15,columns=('gender','Department','Position','contact'))

tv.grid(row=5, column=0 , columnspan=6)

tv.heading('#0', text="Name",anchor=W)
tv.heading('#1', text="Character Gender")
tv.heading('#2', text="Clan")
tv.heading('#3', text="Class")
tv.heading('#4', text="Element")


window.mainloop()
