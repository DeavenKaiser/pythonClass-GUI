# --------------------------------------------
# Name: ANSWER KEY
# Date:
# Program: Chapter 13 Practice - Answer Key
# Description:
# Complete each section by following the
# directions in the comments.
# Run from the command line for best results.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Labels and a Window
# ------------------------------------------------
# TODO:
# 1. Import the tkinter module
# 2. Define a class named MyGUI with an __init__ method
# 3. Inside __init__, create the main window using
#    tkinter.Tk() and store it as self.main_window
# 4. Set the window title to 'My First GUI'
# 5. Create two Label widgets attached to main_window:
#    - First label:  'CIS 115 - Python Programming'
#    - Second label: 'Chapter 13: GUI Practice'
# 6. Pack both labels with pady=5
# 7. Call tkinter.mainloop()
# 8. Outside the class, use the if __name__ == '__main__'
#    block to create an instance of MyGUI

import tkinter                                          # 1.

class MyGUI:
    def __init__(self):                                 # 2.
        self.main_window = tkinter.Tk()                 # 3.
        self.main_window.title('My First GUI')          # 4.

        self.label1 = tkinter.Label(self.main_window,   # 5.
                                    text='CIS 115 - Python Programming')
        self.label2 = tkinter.Label(self.main_window,
                                    text='Chapter 13: GUI Practice')

        self.label1.pack(pady=5)                        # 6.
        self.label2.pack(pady=5)

        tkinter.mainloop()                              # 7.

if __name__ == '__main__':                              # 8.
    my_gui = MyGUI()

# ------------------------------------------------
# Practice 2: Button and Message Box
# ------------------------------------------------
# TODO:
# 1. Import tkinter and tkinter.messagebox
# 2. Define a class named ButtonGUI with an __init__ method
# 3. Create the main window and set the title to
#    'Button Practice'
# 4. Create a Button widget with the text 'Click Me'
#    and set its command to a method named self.btn_clicked
# 5. Pack the button with padx=20, pady=20
# 6. Define the btn_clicked method that shows an info
#    dialog box with:
#    - title:   'Response'
#    - message: 'You clicked the button!'
# 7. Create a second Button with the text 'Quit'
#    and set its command to self.main_window.destroy
# 8. Pack the Quit button below the Click Me button
# 9. Call tkinter.mainloop()
# 10. Create an instance in a if __name__ == '__main__' block

import tkinter
import tkinter.messagebox                               # 1.

class ButtonGUI:
    def __init__(self):                                 # 2.
        self.main_window = tkinter.Tk()                 # 3.
        self.main_window.title('Button Practice')

        self.click_btn = tkinter.Button(                # 4.
            self.main_window,
            text='Click Me',
            command=self.btn_clicked)
        self.click_btn.pack(padx=20, pady=20)           # 5.

        self.quit_btn = tkinter.Button(                 # 7.
            self.main_window,
            text='Quit',
            command=self.main_window.destroy)
        self.quit_btn.pack(pady=5)                      # 8.

        tkinter.mainloop()                              # 9.

    def btn_clicked(self):                              # 6.
        tkinter.messagebox.showinfo('Response',
                                    'You clicked the button!')

if __name__ == '__main__':                              # 10.
    app = ButtonGUI()

# ------------------------------------------------
# Practice 3: Entry Widget and Label Output
# ------------------------------------------------
# TODO:
# 1. Import tkinter
# 2. Define a class named ConverterGUI
# 3. Create the main window titled 'Celsius to Fahrenheit'
# 4. Create a Label: 'Enter temperature in Celsius:'
#    and pack it
# 5. Create an Entry widget stored as self.celsius_entry
#    and pack it
# 6. Create a StringVar stored as self.result_var
# 7. Create a Label associated with self.result_var
#    using textvariable=self.result_var and pack it
# 8. Create a Button labeled 'Convert' whose command
#    calls self.convert
# 9. Pack the button
# 10. Define the convert method that:
#     a. Gets the value from self.celsius_entry using get()
#     b. Converts it to a float
#     c. Calculates Fahrenheit: (celsius * 9/5) + 32
#     d. Stores the result in self.result_var using
#        self.result_var.set('Result: ' + str(round(f, 2)) + ' F')
# 11. Call tkinter.mainloop()
# 12. Create an instance in a if __name__ == '__main__' block

import tkinter                                          # 1.

class ConverterGUI:                                     # 2.
    def __init__(self):
        self.main_window = tkinter.Tk()                 # 3.
        self.main_window.title('Celsius to Fahrenheit')

        self.input_label = tkinter.Label(               # 4.
            self.main_window,
            text='Enter temperature in Celsius:')
        self.input_label.pack()

        self.celsius_entry = tkinter.Entry(             # 5.
            self.main_window)
        self.celsius_entry.pack()

        self.result_var = tkinter.StringVar()           # 6.

        self.output_label = tkinter.Label(              # 7.
            self.main_window,
            textvariable=self.result_var)
        self.output_label.pack()

        self.convert_btn = tkinter.Button(              # 8.
            self.main_window,
            text='Convert',
            command=self.convert)
        self.convert_btn.pack(pady=10)                  # 9.

        tkinter.mainloop()                              # 11.

    def convert(self):                                  # 10.
        celsius = float(self.celsius_entry.get())       # a. & b.
        fahrenheit = (celsius * 9/5) + 32              # c.
        self.result_var.set(                            # d.
            'Result: ' + str(round(fahrenheit, 2)) + ' F')

if __name__ == '__main__':                              # 12.
    app = ConverterGUI()

# ------------------------------------------------
# Practice 4: Radio Buttons
# ------------------------------------------------
# TODO:
# 1. Import tkinter and tkinter.messagebox
# 2. Define a class named RadioGUI
# 3. Create the main window titled 'Pizza Size'
# 4. Create a Label: 'Select a pizza size:' and pack it
# 5. Create an IntVar stored as self.size_var
# 6. Create three Radiobutton widgets, all associated
#    with self.size_var, with the following text and values:
#    - 'Small'  value=1
#    - 'Medium' value=2
#    - 'Large'  value=3
# 7. Pack all three radio buttons
# 8. Create a Button labeled 'OK' whose command
#    calls self.show_selection
# 9. Pack the button with pady=10
# 10. Define show_selection that reads self.size_var.get()
#     and shows a messagebox with the selected size name
#     (e.g. 'You selected: Medium')
# 11. Call tkinter.mainloop()
# 12. Create an instance in a if __name__ == '__main__' block

import tkinter
import tkinter.messagebox                               # 1.

class RadioGUI:                                         # 2.
    def __init__(self):
        self.main_window = tkinter.Tk()                 # 3.
        self.main_window.title('Pizza Size')

        self.size_label = tkinter.Label(                # 4.
            self.main_window,
            text='Select a pizza size:')
        self.size_label.pack()

        self.size_var = tkinter.IntVar()                # 5.

        self.small_btn = tkinter.Radiobutton(           # 6.
            self.main_window,
            text='Small',
            variable=self.size_var,
            value=1)

        self.medium_btn = tkinter.Radiobutton(
            self.main_window,
            text='Medium',
            variable=self.size_var,
            value=2)

        self.large_btn = tkinter.Radiobutton(
            self.main_window,
            text='Large',
            variable=self.size_var,
            value=3)

        self.small_btn.pack()                           # 7.
        self.medium_btn.pack()
        self.large_btn.pack()

        self.ok_btn = tkinter.Button(                   # 8.
            self.main_window,
            text='OK',
            command=self.show_selection)
        self.ok_btn.pack(pady=10)                       # 9.

        tkinter.mainloop()                              # 11.

    def show_selection(self):                           # 10.
        selection = self.size_var.get()
        if selection == 1:
            size = 'Small'
        elif selection == 2:
            size = 'Medium'
        else:
            size = 'Large'
        tkinter.messagebox.showinfo('Selection',
                                    'You selected: ' + size)

if __name__ == '__main__':                              # 12.
    app = RadioGUI()

# ------------------------------------------------
# Practice 5: Debug the GUI Program - FIXED
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Display a window with an Entry field and a Label
# - When the button is clicked, read the name entered
#   and display 'Hello, <name>!' in the label
#
# There are 3 errors in this code.
# Fix them so the program works correctly.
#
# Bug 1: textvariable= is missing on the output Label
#         text=self.result_var  -->  textvariable=self.result_var
#         Using text= sets a static string — the label never updates
# Bug 2: self.result_var is a StringVar, not a string
#         The Label needs textvariable= to stay linked to the StringVar
#         (same fix as Bug 1 — the keyword argument is wrong)
# Bug 3: GreeterGUI is not called with ()
#         app = GreeterGUI  -->  app = GreeterGUI()
#         Without parentheses, no instance is created and the GUI never opens

import tkinter

class GreeterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Greeter')

        self.name_label = tkinter.Label(self.main_window,
                                        text='Enter your name:')
        self.name_label.pack()

        self.name_entry = tkinter.Entry(self.main_window)
        self.name_entry.pack()

        self.result_var = tkinter.StringVar()
        self.output_label = tkinter.Label(
            self.main_window,
            textvariable=self.result_var)   # Fix 1 & 2: text= -> textvariable=
        self.output_label.pack()

        self.greet_btn = tkinter.Button(self.main_window,
                                        text='Greet',
                                        command=self.greet)
        self.greet_btn.pack()

        tkinter.mainloop()

    def greet(self):
        name = self.name_entry.get()
        self.result_var.set('Hello, ' + name + '!')

if __name__ == '__main__':
    app = GreeterGUI()                      # Fix 3: GreeterGUI -> GreeterGUI()
