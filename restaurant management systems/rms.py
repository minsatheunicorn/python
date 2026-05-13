import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("restaraunt")
menu={"burger":3,"pizza":4,"fries":2}
entrys={}
for item,price in menu.items():
    tk.Label(root,text=f"{item}${price}").pack()
    e=tk.Entry(root)
    e.pack()
    entrys[item]=e
def order():
    total=0
    for item,e in entrys.items():
        q=e.get()
        if q.isdigit():
            total+=int(q)*menu[item]
    messagebox.showinfo("totel",f"total=${total}")
tk.Button(root,text="order",command=order).pack()
root.mainloop()