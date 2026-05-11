from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("demonisation counter")
root.geometry("300x250")
Label(root,text="Enter Amount").pack()
e=Entry(root)
e.pack()
res = {2000: StringVar(), 500: StringVar(), 100: StringVar()}
def calc():
    try:
       amt=int(e.get())
       for note in res:
         res[note].set(amt//note)
         amt%=note
    except:
       messagebox.showerror("error","invalid input")
Button(root,text="calculator",command=calc).pack(pady=5)
for n in res:
   Label(root,text=str(n)).pack()
   Entry(root,textvariable=res[n]).pack()
root.mainloop()