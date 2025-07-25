#Listbox
from tkinter import *
top= Tk()
#Window dimensions
top.geometry("300x150")
top.title("Listbox Example")
top['bg'] = '#51E1Dc'  # Set background color
Label(top, text="Select your favorite fruits:", bg='#51E1Dc').pack()
listbox =Listbox(top ,height="20")
listbox.insert(1, "Apple")
listbox.insert(2, "Mango")  
listbox.insert(3, "Orange")
listbox.insert(4, "Banana")
listbox.insert(5, "Grapes")
listbox.insert(6, "Pineapple")
listbox.insert(7, "Strawberry") 
listbox.insert(8, "Watermelon")
listbox.insert(9, "Peach")
listbox.insert(10, "Kiwi")
listbox.insert(11, "Blueberry")
listbox.insert(12, "Raspberry")
listbox.insert(13, "Papaya")
listbox.insert(14, "Cherry")
listbox.insert(15, "Plum")
listbox.insert(16, "Coconut")
listbox.insert(17, "Lemon") 
listbox.pack()
top.mainloop()  # Start the GUI event loop
# This code creates a simple GUI window with a listbox containing fruit names.
