#take a input from user and print the sum of two numbers 
from tkinter import messagebox
from tkinter import *
top= Tk()
top.title("Sum Calculator")
top.geometry("300x180")
top['bg'] = 'lightblue'  # Set background color
def add():
    f = firstnum.get()
    s = secondnum.get()
    messagebox.showinfo("Sum", f"The sum of {f} and {s} is {int(f) + int(s)}")  
#declaring variables for first and second numbers  
firstnum = IntVar()
secondnum = IntVar()
#create Labels and entries for first and second numbers
first_label = Label(top, text="First Number:").place(x=20, y=20)
second_label = Label(top, text="Second Number:").place(x=20, y=60)

#create textboxes for user input
first_entry = Entry(top, textvariable=firstnum).place(x=150, y=20)
second_entry = Entry(top, textvariable=secondnum).place(x=150, y=60)

#Create a button to calculate the sum
calculate_button = Button(top, text=" Add",width="5",command= add, bg='green', fg='white').place(x=100, y=100)
top.mainloop()  # Start the GUI event loop
# This code creates a simple GUI window with labels, entries, and a button to calculate the