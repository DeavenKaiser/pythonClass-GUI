# --------------------------------------------
# Name:
# Date:
# Program: Chapter 13 Practice - Week 1
# Description:
# Complete each section by following the
# directions in the comments.
# Run from the command line for best results.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Your First Window with Labels
# ------------------------------------------------
# TODO:
# 1. Import the tkinter module
# 2. Define a class named MyGUI with an __init__ method
# 3. Create the main window using tkinter.Tk() and
#    store it as self.main_window
# 4. Set the window title to 'My First GUI'
# 5. Create two Label widgets attached to self.main_window:
#    - First label:  'CIS 120 - Python Programming'
#    - Second label: 'Chapter 13: GUI Practice'
# 6. Pack both labels with pady=5
# 7. Call tkinter.mainloop()
# 8. Create an instance in an if __name__ == '__main__' block
print()

# ------------------------------------------------
# Practice 2: Button and Message Box
# ------------------------------------------------
# TODO:
# 1. Import tkinter and tkinter.messagebox
# 2. Define a class named ButtonGUI
# 3. Create the main window titled 'Button Practice'
# 4. Create a Button with text 'Click Me' whose command
#    calls self.btn_clicked
# 5. Pack the button with padx=20, pady=20
# 6. Create a second Button with text 'Quit' whose command
#    is self.main_window.destroy
# 7. Pack the Quit button with pady=5
# 8. Define btn_clicked to show an info dialog box with:
#    - title:   'Hello!'
#    - message: 'You clicked the button!'
# 9. Call tkinter.mainloop()
# 10. Create an instance in an if __name__ == '__main__' block
print()

# ------------------------------------------------
# Practice 3: Debug the GUI
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Display a window with an Entry field and a button
# - When the button is clicked, read the name entered
#   and display 'Hello, <name>!' in a label
#
# There are 3 errors in this code.
# Fix them so the program works correctly.
'''
import tkinter

class GreeterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Greeter')

        self.name_label = tkinter.Label(self.main_window,
                                        text='Enter your name:')
        self.name_label.pack(pady=5)

        self.name_entry = tkinter.Entry(self.main_window)
        self.name_entry.pack()

        self.result_var = tkinter.StringVar()
        self.output_label = tkinter.Label(self.main_window,
                                          text=self.result_var)
        self.output_label.pack(pady=5)

        self.greet_btn = tkinter.Button(self.main_window,
                                        text='Greet',
                                        command=self.greet)
        self.greet_btn.pack()

        tkinter.mainloop()

    def greet(self):
        name = self.name_entry.Get()
        self.result_var.set('Hello, ' + name + '!')

if __name__ == '__main__':
    app = GreeterGUI

'''
