# Imports necessary GUI library
from tkinter import *


class WindowMenu(object):
    def __init__(self, parent):
        #Addresses root as the parent
        self.root = parent
        # Disables modifying window properties, to remove window-size dependancy of the widgets
        root.resizable(0,0)
        # Alternatively: self.overrideredirect(1) - but removes entire top bar
        root.attributes("-toolwindow", 1)
        #Obtains the coordinates of the user's centre of the screen
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        # Places the main window at the centre (coordinates x and y)
        root.geometry("+%d+%d" % (x, y))
        # Sets the title of the window
        root.title("Latin²")
        #self.frame becomes part a child of root
        self.frame = Frame(parent)
        self.frame.pack()
        # Displays a welcome message
        label_welcome = Label(self.frame, text = "Welcome to Latin²")
        label_welcome.pack(pady=10, padx=15)
        # Buttons which direct user to corresponding games
        button_opt1 = Button(self.frame, width=15,text="Standard Sudoku", command=self.call_opt1)
        button_opt1.pack(pady=(0,10))
        button_opt2 = Button(self.frame, width=15, text="Other Games", command=self.call_opt2)
        button_opt2.pack(pady=(0,10))

    def call_opt1(self):
        print("OPTION 1 SELECTED")
        self.root.withdraw()
        print("Destroyed and new")

    def call_opt2(self):
        print("OPTION 2 SELECTED")
        self.root.withdraw()


# Create a window (root)and calls class MainMenu
root = Tk()
window_main = WindowMenu(root)
root.mainloop()
