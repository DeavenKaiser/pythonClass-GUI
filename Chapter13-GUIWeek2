# --------------------------------------------
# Name:
# Date:
# Program: Chapter 13 Practice - Week 2
# Description:
# Complete each section by following the
# directions in the comments.
# Run from the command line for best results.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Pizza Order with Check Buttons
# ------------------------------------------------
# TODO:
# 1. Import tkinter and tkinter.messagebox
# 2. Define a class named PizzaOrder
# 3. Create the main window titled 'Pizza Order'
# 4. Create a Label: 'Select your toppings:' and pack
#    it with pady=(10, 5)
# 5. Create an IntVar for each topping stored as:
#    self.pepperoni_var, self.mushroom_var, self.onion_var
# 6. Create a Checkbutton for each topping linked to
#    its IntVar and pack each one
# 7. Create a Button labeled 'Place Order' whose command
#    calls self.place_order and pack it with pady=10
# 8. Create a Button labeled 'Quit' whose command is
#    self.main_window.destroy and pack it
# 9. Define place_order that:
#    a. Builds a list of selected toppings by checking
#       each IntVar -- if .get() == 1 the box is checked
#    b. If the list is empty, show a messagebox warning:
#       title: 'No Toppings'
#       message: 'Please select at least one topping.'
#    c. Otherwise show an info messagebox:
#       title: 'Order Placed'
#       message: 'Your toppings:\n' + ', '.join(toppings)
# 10. Call tkinter.mainloop()
# 11. Create an instance in an if __name__ == '__main__' block
print()

# ------------------------------------------------
# Practice 2: Radio Buttons
# ------------------------------------------------
# TODO:
# 1. Import tkinter and tkinter.messagebox
# 2. Define a class named SizeSelector
# 3. Create the main window titled 'Select a Size'
# 4. Create a Label: 'Choose your size:' and pack it
#    with pady=(10, 5)
# 5. Create an IntVar stored as self.size_var
# 6. Create three Radiobutton widgets all linked to
#    self.size_var with these text and values:
#    - 'Small'  value=1
#    - 'Medium' value=2
#    - 'Large'  value=3
# 7. Pack all three radio buttons
# 8. Create a Button labeled 'OK' whose command calls
#    self.show_choice and pack it with pady=10
# 9. Define show_choice that reads self.size_var.get()
#    and shows a messagebox with the size name:
#    title: 'Your Selection'
#    message: 'You chose: Small' (or Medium or Large)
#    If nothing is selected (value is 0) show:
#    message: 'Please select a size.'
# 10. Call tkinter.mainloop()
# 11. Create an instance in an if __name__ == '__main__' block
print()

# ------------------------------------------------
# Practice 3: Debug the Advanced GUI
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Show radio buttons for shirt size
# - Show check buttons for shirt color
# - When 'Submit' is clicked, open a second Toplevel
#   window displaying the chosen size and colors
#
# There are 3 errors in this code.
# Fix them so the program works correctly.

'''
import tkinter

class ShirtOrder:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Shirt Order')

        size_label = tkinter.Label(self.main_window,
                                   text='Select size:')
        size_label.pack(pady=(10, 2))

        self.size_var = tkinter.IntVar()

        self.small_rb  = tkinter.Radiobutton(self.main_window,
                                              text='Small',
                                              variable=self.size_var,
                                              value=1)
        self.medium_rb = tkinter.Radiobutton(self.main_window,
                                              text='Medium',
                                              variable=self.size_var,
                                              value=2)
        self.large_rb  = tkinter.Radiobutton(self.main_window,
                                              text='Large',
                                              variable=self.size_var,
                                              value=3)
        self.small_rb.pack()
        self.medium_rb.pack()
        self.large_rb.pack()

        color_label = tkinter.Label(self.main_window,
                                    text='Select colors:')
        color_label.pack(pady=(10, 2))

        self.red_var   = tkinter.IntVar()
        self.blue_var  = tkinter.IntVar()
        self.green_var = tkinter.IntVar()

        self.red_cb   = tkinter.Checkbutton(self.main_window,
                                             text='Red',
                                             variables=self.red_var)
        self.blue_cb  = tkinter.Checkbutton(self.main_window,
                                             text='Blue',
                                             variable=self.blue_var)
        self.green_cb = tkinter.Checkbutton(self.main_window,
                                             text='Green',
                                             variable=self.green_var)
        self.red_cb.pack()
        self.blue_cb.pack()
        self.green_cb.pack()

        self.submit_btn = tkinter.Button(self.main_window,
                                         text='Submit',
                                         command=self.show_summary)
        self.submit_btn.pack(pady=10)

        tkinter.mainloop()

    def show_summary(self):
        sizes = {1: 'Small', 2: 'Medium', 3: 'Large'}
        size = sizes.get(self.size_var.get(), 'None selected')

        colors = []
        if self.red_var.get()   == 1: colors.append('Red')
        if self.blue_var.get()  == 1: colors.append('Blue')
        if self.green_var.get() == 1: colors.append('Green')
        color_text = ', '.join(colors) if colors else 'None selected'

        self.summary_win = tkinter.Toplevel(self.main_window)
        self.summary_win.title = 'Order Summary'

        tkinter.Label(self.summary_win,
                      text='Size: '   + size).pack(pady=(20, 5))
        tkinter.Label(self.summary_win,
                      text='Colors: ' + color_text).pack(pady=5)
        tkinter.Button(self.summary_win,
                       text='Close',
                       command=self.summary_win.destroy).pack(pady=10)

if __name__ == '__main__':
    app = ShirtOrder

'''
