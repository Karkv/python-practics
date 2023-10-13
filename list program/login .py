from tkinter import *
def main_screen():
    mainscreen = Tk()
    mainscreen.geometry("800x800")
    mainscreen.title(" Login Page ")
    Label(text="Please enter login details", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="Username * ").pack()
    username_entry = Entry(mainscreen)
    username_entry.pack()
    Label(text="").pack()
    Label(text="Password * ").pack()
    password_entry = Entry(mainscreen, show='*')
    password_entry.pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30").pack()
    mainscreen.mainloop()

main_screen()