#TKINTER
import tkinter
top = tkinter.Tk()
top.title("Login Window")  
top.geometry("400x300")
top['bg'] = 'lightblue'  # Set background color
uname = tkinter.Label(top, text="Username:").place(x=50, y=50)
password_label = tkinter.Label(top, text="Password:").place(x=50, y=80)
username_entry = tkinter.Entry(top).place(x=150, y=50)
password_entry = tkinter.Entry(top, show='*').place(x=150, y=80)
#ent =tkinter.Entry(top).place(x=150, y=50)
btn = tkinter.Button(top, text="Login", bg='green', fg='white', command=lambda: print("Submitted..!!")).place(x=150, y=120)
top.mainloop()  # Start the GUI event loop
# This code creates a simple GUI window with a label and a button using Tkinter.