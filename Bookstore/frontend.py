
from tkinter import *
from backend import *

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in search(title_terxt.get(),author_terxt.get(),year_terxt.get(),isbn_terxt.get()):
        list1.insert(END,row)

def add_command():
    insert(title_terxt.get(), author_terxt.get(), year_terxt.get(), isbn_terxt.get())
    list1.delete(0, END)
    list1.insert(END,(title_terxt.get(), author_terxt.get(), year_terxt.get(), isbn_terxt.get()))

def delete_command():
    delete(selected_tuple[0])

def update_command():
    update(selected_tuple[0],title_terxt.get(),author_terxt.get(),year_terxt.get(),isbn_terxt.get())

def close_command():
    close()

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_terxt = StringVar()
e1 = Entry(window,textvariable=title_terxt)
e1.grid(row=0,column=1)

author_terxt = StringVar()
e2 = Entry(window,textvariable=author_terxt)
e2.grid(row=0,column=3)

year_terxt = StringVar()
e3 = Entry(window,textvariable=year_terxt)
e3.grid(row=1,column=1)

isbn_terxt = StringVar()
e4 = Entry(window,textvariable=isbn_terxt)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="view all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="close",width=12,command=close)
b6.grid(row=7,column=3)

window.mainloop()
