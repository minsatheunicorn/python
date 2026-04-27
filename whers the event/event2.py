from tkinter import*
windo=Tk()
windo.title("event handler")
windo.geometry("200x200")
def handle_click(event):
    print("mooty unicon is a unicorn:)")
btn=Button(text="click mee!")
btn.pack()
btn.bind("<Button-1>",handle_click)
windo.mainloop()