from tkinter import*
from datetime import date
root=Tk()
root.title("getting started with widgets")
root.geometry("400x300")
l=Label(text="hey there",fg="white",bg="green")
name_l=Label(text="full name",bg="pink")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcom te the application todays date is:"
    greet="hello "+name
    x.insert(END,greet)
    x.insert(END,message)
    x.insert(END,date.today())
x=Text(height=3)
btn=Button(text="begin",command=display,bg="yellow")
l.pack()
name_l.pack()
name_entry.pack()
btn.pack()
x.pack()
root.mainloop()
