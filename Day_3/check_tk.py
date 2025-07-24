#checkbuttons 
from tkinter import *
from tkinter import messagebox
top = Tk()
#window dimensions
top.geometry("400x300")
top.title("Checkbutton Example")
top['bg'] = '#51E1Dc'  # Set background color
def fun():
    str = ""
    if chk1.get() == 1:
        str = str+"Appple"
    if chk2.get() == 1:
        str = str+" Mango"
    if chk3.get() == 1:
        str = str+" Orange"
    messagebox.showinfo("Selected Fruits", f"You selected: {str}")
#creating checkbuttons  
chk1 = IntVar()
chk2 = IntVar()
chk3 = IntVar()
check1 = Checkbutton(top, text="Apple", variable=chk1, onvalue=1, offvalue=0).place(x=50, y=50)
check2 = Checkbutton(top, text="Mango", variable=chk2, onvalue=1, offvalue=0).place(x=50, y=80) 
check3 = Checkbutton(top, text="Orange", variable=chk3, onvalue=1, offvalue=0).place(x=50, y=110)   
#creating a button to show selected fruits
button = Button(top, text="Show Selected Fruits", command=fun, bg='green', fg='white').place(x=50, y=150)
top.mainloop()  # Start the GUI event loop