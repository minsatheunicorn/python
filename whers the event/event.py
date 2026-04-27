from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("alert","stop visus found")
button=Button(text="scan for virus",command=msg)
button.pack()
root.mainloop()