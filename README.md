# 📘 Chapter 13: Graphical User Interfaces
### *Starting Out with Python — Textbook Companion & Practice Guide*

---

## 📚 Table of Contents

1. [Graphical User Interfaces](#1-graphical-user-interfaces)
2. [GUI Programs Are Event-Driven](#2-gui-programs-are-event-driven)
3. [Using the tkinter Module](#3-using-the-tkinter-module)
4. [The Main Window](#4-the-main-window)
5. [Label Widgets](#5-label-widgets)
6. [Padding and Borders](#6-padding-and-borders)
7. [Organizing Widgets with Frames](#7-organizing-widgets-with-frames)
8. [Button Widgets and Dialog Boxes](#8-button-widgets-and-dialog-boxes)
9. [The Entry Widget](#9-the-entry-widget)
10. [Using Labels as Output Fields](#10-using-labels-as-output-fields)
11. [Radio Buttons](#11-radio-buttons)
12. [Check Buttons](#12-check-buttons)
13. [Listbox Widgets](#13-listbox-widgets)
14. [Drawing Shapes with the Canvas Widget](#14-drawing-shapes-with-the-canvas-widget)

---

## 1. Graphical User Interfaces

A **user interface** is the part of a program that the user interacts with. There are two major types:

- **Command line interface (CLI):** displays a text prompt; the user types commands that execute in a fixed order defined by the program
- **Graphical user interface (GUI):** allows the user to interact with the program through visual elements — buttons, text fields, menus, and dialog boxes — on the screen

GUIs are built around **dialog boxes**: small windows that display information and allow the user to perform actions. Users interact with **graphical elements** such as icons, buttons, and sliders rather than typed commands.

**Quick Check:**

<details>
<summary>What is the difference between a CLI and a GUI?</summary>

A **command line interface** is text-based. The program dictates the flow — the user responds to prompts in a fixed order:

```
Enter your name: Alex
Enter your age: 20
```

A **graphical user interface** gives the user visual elements to interact with. The user decides what to click and when — filling a form, selecting from a menu, or pressing a button in any order they choose.

GUIs are more intuitive for end users but require more code to build. CLIs are simpler to write and common in developer tools and scripting.

</details>

---

## 2. GUI Programs Are Event-Driven

Traditional text-based programs control the flow — the program determines what happens and when. GUI programs work differently: they are **event-driven**.

- The user causes **events** — clicking a button, typing in a field, selecting an item
- The program **responds** to those events by executing callback functions
- The program does not dictate order; the user does

This is a fundamental shift from the procedural programs written in earlier chapters. Instead of a top-to-bottom flow, a GUI program sits in a **main loop** waiting for events, then fires the appropriate response.

**Quick Check:**

<details>
<summary>What does "event-driven" mean in the context of GUI programming?</summary>

In an event-driven program, code does not run in a fixed sequence. Instead, the program enters a loop that continuously watches for **events** — user actions like mouse clicks, key presses, or button selections.

When an event occurs, the program calls the **callback function** (also called an event handler) that was registered for that event:

```python
def btn_clicked(self):          # This is the callback function
    print('Button was clicked!')

self.button = tkinter.Button(
    self.main_window,
    text='Click Me',
    command=self.btn_clicked    # Registered here — runs when clicked
)
```

Nothing in `btn_clicked` runs until the user actually clicks the button.

</details>

---

## 3. Using the tkinter Module

Python does not have GUI features built in. The **tkinter module** provides a set of tools for creating simple GUI programs. It comes pre-installed with Python and does not require a separate download.

### Widgets

A **widget** is a graphical element that the user can view or interact with. tkinter provides many widget types:

| Widget | Description |
|--------|-------------|
| `Label` | Displays a single line of text or an image |
| `Button` | A clickable button that triggers a callback function |
| `Entry` | A single-line text input field |
| `Frame` | A container that holds and organizes other widgets |
| `Radiobutton` | A circular button for selecting one option from a group |
| `Checkbutton` | A checkbox for selecting any number of options |
| `Listbox` | A scrollable list of selectable items |
| `Canvas` | A blank area for drawing 2D shapes and text |
| `Scrollbar` | Provides scrolling for other widgets |
| `Message` | Displays multiple lines of text |

> 💡 **Important:** GUI programs using tkinter do not always run reliably inside IDLE. For best results, run them from the **operating system command line** (terminal / command prompt).

**Quick Check:**

<details>
<summary>What is a widget and how is it different from a regular Python object?</summary>

A **widget** is a visual, interactive element in a GUI window — a button you can click, a text field you can type in, or a label that displays information. Every visible element in a tkinter window is a widget.

Like regular Python objects, widgets are created as instances of a class:

```python
import tkinter

# A Label widget — displays text
my_label = tkinter.Label(parent_window, text='Hello!')

# A Button widget — triggers an action when clicked
my_button = tkinter.Button(parent_window, text='OK', command=some_function)
```

The key difference is that widgets render visually on screen and respond to user interaction, whereas plain Python objects exist only in memory.

</details>

---

## 4. The Main Window

Every tkinter program starts by creating a **main window** — the root container that holds all other widgets. Most tkinter programs use an **object-oriented structure** where the `__init__` method builds the GUI.

```python
import tkinter

class MyGUI:
    def __init__(self):
        # 1. Create the main window
        self.main_window = tkinter.Tk()

        # 2. Set the title bar text
        self.main_window.title('My First GUI')

        # 3. Start the event loop — keeps the window open
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
```

### Key elements

- **`tkinter.Tk()`** — creates the main window object
- **`.title()`** — sets the text shown in the window's title bar
- **`tkinter.mainloop()`** — starts the event loop; the program stays open and responsive until the window is closed
- **`if __name__ == '__main__'`** — ensures the GUI only launches when the file is run directly, not when it is imported

**Quick Check:**

<details>
<summary>What does tkinter.mainloop() do and why is it required?</summary>

`tkinter.mainloop()` starts the **event loop** — an ongoing cycle where tkinter watches for user events (clicks, key presses, etc.) and responds to them. Without it, the window would flash open and immediately close because the program would reach the end of `__init__` and exit.

```python
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Test')
        # Without mainloop(), the window closes immediately
        tkinter.mainloop()   # Keeps the window open and responsive
```

Always place `mainloop()` as the **last line** inside `__init__`, after all widgets have been created and packed.

</details>

<details>
<summary>Why use if __name__ == '__main__' to create the instance?</summary>

When Python runs a file directly, it sets the special variable `__name__` to `'__main__'`. When a file is imported as a module by another file, `__name__` is set to the file's name instead.

```python
if __name__ == '__main__':
    my_gui = MyGUI()   # Only runs when this file is executed directly
```

Without this guard, creating a `MyGUI` instance would run automatically whenever another program imported this file — opening an unwanted window. This is a standard Python best practice for any file that can be both run directly and imported.

</details>

---

## 5. Label Widgets

A **Label widget** displays a single line of text (or an image) inside a window. It is the most basic widget for showing information to the user.

### Creating a Label

```python
self.label = tkinter.Label(self.main_window, text='Hello, World!')
```

- First argument: the **parent widget** (the window or frame the label belongs to)
- `text=` : the string to display

### The `pack()` Method

After creating a widget, call `.pack()` to position it and make it visible:

```python
self.label.pack()
```

Multiple labels are stacked vertically by default. Use `side='left'` or `side='right'` to arrange them horizontally:

```python
self.label1.pack(side='left')
self.label2.pack(side='left')
```

**Quick Check:**

<details>
<summary>What does pack() do and what happens if you forget it?</summary>

`pack()` tells tkinter where to place the widget inside its parent container and makes it **visible**. Without calling `pack()`, the widget is created in memory but never appears on screen.

```python
self.label = tkinter.Label(self.main_window, text='Hello!')
# Without pack(), this label is invisible:
self.label.pack()   # Now it appears
```

The order you call `pack()` determines the order widgets appear. Widgets packed first appear at the top (or left, depending on `side=`).

</details>

---

## 6. Padding and Borders

### Borders

Use `borderwidth` and `relief` to add a visible border around a Label:

```python
self.label = tkinter.Label(self.main_window,
                           text='Hello',
                           borderwidth=2,
                           relief='solid')
```

| `relief` value | Appearance |
|----------------|------------|
| `'flat'`   | Border hidden, no 3D effect |
| `'solid'`  | Solid line border |
| `'raised'` | Widget appears raised (3D) |
| `'sunken'` | Widget appears pressed in (3D) |
| `'ridge'`  | Border has a raised ridge |
| `'groove'` | Border appears as a groove |

### Padding

**Internal padding** (`ipadx`, `ipady`) adds space **inside** the widget border:

```python
self.label.pack(ipadx=20, ipady=20)
```

**External padding** (`padx`, `pady`) adds space **outside** the widget border, separating it from neighboring widgets:

```python
self.label.pack(padx=20, pady=20)
```

Both can be combined:

```python
self.label.pack(ipadx=10, ipady=10, padx=20, pady=20)
```

**Quick Check:**

<details>
<summary>What is the difference between ipadx and padx?</summary>

- **`ipadx` / `ipady`** — *internal* padding: space between the widget's content and its own border. Makes the widget itself larger.
- **`padx` / `pady`** — *external* padding: space between the widget's border and surrounding widgets. Creates breathing room between elements.

```python
# Internal — expands the label box itself
self.label.pack(ipadx=20, ipady=20)

# External — adds space around the label
self.label.pack(padx=20, pady=20)

# Both together
self.label.pack(ipadx=10, ipady=10, padx=20, pady=20)
```

Think of it like CSS: `ipadx`/`ipady` = `padding`, `padx`/`pady` = `margin`.

</details>

---

## 7. Organizing Widgets with Frames

A **Frame widget** is an invisible container that holds and organizes other widgets. Frames let you group related widgets and control their layout independently from the rest of the window.

```python
# Create a frame inside the main window
self.top_frame = tkinter.Frame(self.main_window)
self.top_frame.pack()

# Add labels to the frame — NOT directly to main_window
self.label1 = tkinter.Label(self.top_frame, text='Winken')
self.label2 = tkinter.Label(self.top_frame, text='Blinken')
self.label3 = tkinter.Label(self.top_frame, text='Nod')

self.label1.pack(side='left')
self.label2.pack(side='left')
self.label3.pack(side='left')
```

By using separate frames, you can stack one group of widgets vertically while arranging another group horizontally — all inside the same window.

**Quick Check:**

<details>
<summary>Why would you use a Frame instead of just adding all widgets to the main window?</summary>

Frames let you create **independent layout zones** within the same window. Without frames, all widgets share the same packing rules and can't be arranged in mixed directions easily.

```python
# Top frame — labels arranged left-to-right
self.top_frame = tkinter.Frame(self.main_window)
self.top_frame.pack()
tkinter.Label(self.top_frame, text='A').pack(side='left')
tkinter.Label(self.top_frame, text='B').pack(side='left')

# Bottom frame — buttons stacked top-to-bottom
self.bottom_frame = tkinter.Frame(self.main_window)
self.bottom_frame.pack()
tkinter.Button(self.bottom_frame, text='OK').pack()
tkinter.Button(self.bottom_frame, text='Cancel').pack()
```

Frames are essential for building well-organized GUIs with complex layouts.

</details>

---

## 8. Button Widgets and Dialog Boxes

### Button Widgets

A **Button widget** triggers a **callback function** when clicked. The callback is set using the `command=` argument:

```python
self.my_btn = tkinter.Button(self.main_window,
                             text='Click Me',
                             command=self.btn_clicked)
self.my_btn.pack()
```

The callback method is defined separately inside the class:

```python
def btn_clicked(self):
    # Code that runs when the button is clicked
    pass
```

### Info Dialog Boxes

An **info dialog box** displays a message to the user. Import `tkinter.messagebox` and use `showinfo()`:

```python
import tkinter.messagebox

tkinter.messagebox.showinfo('Title', 'Message text here.')
```

### Quit Button

To close the window when a button is clicked, use `self.main_window.destroy` as the callback:

```python
self.quit_btn = tkinter.Button(self.main_window,
                               text='Quit',
                               command=self.main_window.destroy)
```

**Quick Check:**

<details>
<summary>What is a callback function and how do you connect one to a button?</summary>

A **callback function** (also called an event handler) is a method that runs automatically when an event occurs — like a button click. You connect it to a button using the `command=` argument.

```python
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.btn = tkinter.Button(self.main_window,
                                  text='Say Hello',
                                  command=self.say_hello)  # Connected here
        self.btn.pack()
        tkinter.mainloop()

    def say_hello(self):                # This runs when button is clicked
        tkinter.messagebox.showinfo('Hi', 'Hello!')
```

Notice: `command=self.say_hello` — no parentheses. Writing `self.say_hello()` would call the method immediately when the GUI builds, not when the button is clicked.

</details>

---

## 9. The Entry Widget

An **Entry widget** provides a rectangular text input field where the user can type a single line of input. Use the `.get()` method to retrieve whatever the user typed — it always returns a **string**.

```python
# Create the Entry widget
self.name_entry = tkinter.Entry(self.main_window)
self.name_entry.pack()
```

Retrieve the input inside a callback method:

```python
def process_input(self):
    user_text = self.name_entry.get()   # Returns a string
    # Convert to number if needed:
    number = float(user_text)
```

The typical pattern is:

1. Label explaining what to enter
2. Entry widget for input
3. Button that triggers the callback
4. Callback retrieves the Entry value with `.get()` and processes it

**Quick Check:**

<details>
<summary>What does the Entry widget's get() method return?</summary>

`get()` always returns a **string**, regardless of what was typed. If you need a number, you must convert it:

```python
def convert(self):
    raw = self.celsius_entry.get()   # Returns '100' as a string
    celsius = float(raw)             # Convert to float for math
    fahrenheit = (celsius * 9/5) + 32
```

If the user typed something that can't be converted (like `'abc'`), `float()` will raise a `ValueError`. In production code you'd wrap this in a `try/except`, but for practice the input is assumed to be valid.

</details>

---

## 10. Using Labels as Output Fields

Instead of always showing results in a dialog box, you can use a **Label widget linked to a StringVar** to display output directly in the window. When the `StringVar` changes, the label updates automatically.

### StringVar

`StringVar` is a tkinter class that acts as a variable container linked to a widget. Changing the `StringVar` immediately updates any widget connected to it.

```python
# 1. Create the StringVar
self.result_var = tkinter.StringVar()

# 2. Create a Label connected to it via textvariable=
self.output_label = tkinter.Label(self.main_window,
                                  textvariable=self.result_var)
self.output_label.pack()

# 3. In your callback, update the StringVar to update the label
def convert(self):
    result = 42.0
    self.result_var.set('Result: ' + str(result))
```

> ⚠️ Use `textvariable=self.result_var` — **not** `text=self.result_var`. Using `text=` sets a static string and the label will never update.

**Quick Check:**

<details>
<summary>What is the difference between text= and textvariable= on a Label?</summary>

- **`text='Hello'`** — sets a **static** string. The label always shows that exact text and never changes.
- **`textvariable=self.result_var`** — **links** the label to a `StringVar`. Whenever the `StringVar` changes via `.set()`, the label automatically updates to show the new value.

```python
# Static label — never changes
self.label = tkinter.Label(self.main_window, text='Hello')

# Dynamic label — updates when result_var changes
self.result_var = tkinter.StringVar()
self.label = tkinter.Label(self.main_window, textvariable=self.result_var)

# Later, in a callback:
self.result_var.set('New text!')   # Label now shows 'New text!'
```

</details>

---

## 11. Radio Buttons

**Radiobutton widgets** let the user select exactly one option from a group. They are mutually exclusive — selecting one automatically deselects all others in the same group.

### IntVar

All radio buttons in a group share the same **IntVar** object. Each button is assigned a unique integer `value`. When a button is selected, its integer is stored in the `IntVar`.

```python
# 1. Create the shared IntVar
self.size_var = tkinter.IntVar()

# 2. Create Radiobuttons — all share the same variable
self.small_btn = tkinter.Radiobutton(self.main_window,
                                     text='Small',
                                     variable=self.size_var,
                                     value=1)
self.medium_btn = tkinter.Radiobutton(self.main_window,
                                      text='Medium',
                                      variable=self.size_var,
                                      value=2)
self.large_btn = tkinter.Radiobutton(self.main_window,
                                     text='Large',
                                     variable=self.size_var,
                                     value=3)

self.small_btn.pack()
self.medium_btn.pack()
self.large_btn.pack()

# 3. Read the selection in a callback
def show_selection(self):
    selected = self.size_var.get()   # Returns 1, 2, or 3
```

You can also use `command=self.some_method` directly on the Radiobutton so the callback fires the moment a button is selected — without needing a separate OK button.

**Quick Check:**

<details>
<summary>Why do all Radiobuttons in a group share the same IntVar?</summary>

Sharing the same `IntVar` is what makes radio buttons **mutually exclusive**. tkinter uses the shared variable to track which button is currently selected — when one button is clicked, its value is stored in the `IntVar` and all other buttons in the group automatically deselect.

```python
self.choice = tkinter.IntVar()

self.rb1 = tkinter.Radiobutton(..., variable=self.choice, value=1)
self.rb2 = tkinter.Radiobutton(..., variable=self.choice, value=2)
self.rb3 = tkinter.Radiobutton(..., variable=self.choice, value=3)
```

If you accidentally gave each Radiobutton a *different* `IntVar`, they would behave independently — all three could be selected at once, which defeats the purpose.

</details>

---

## 12. Check Buttons

**Checkbutton widgets** let the user toggle options on or off independently. Unlike radio buttons, any number of check buttons can be selected at the same time.

Each Checkbutton gets its **own IntVar**. When checked, the IntVar stores `1`; when unchecked, it stores `0`.

```python
# Each check button has its own IntVar
self.pepperoni_var = tkinter.IntVar()
self.mushroom_var  = tkinter.IntVar()
self.onion_var     = tkinter.IntVar()

self.pepperoni_cb = tkinter.Checkbutton(self.main_window,
                                        text='Pepperoni',
                                        variable=self.pepperoni_var)
self.mushroom_cb  = tkinter.Checkbutton(self.main_window,
                                        text='Mushrooms',
                                        variable=self.mushroom_var)
self.onion_cb     = tkinter.Checkbutton(self.main_window,
                                        text='Onions',
                                        variable=self.onion_var)

self.pepperoni_cb.pack()
self.mushroom_cb.pack()
self.onion_cb.pack()

# Check which boxes are selected in a callback
def show_order(self):
    if self.pepperoni_var.get() == 1:
        print('Pepperoni selected')
```

**Quick Check:**

<details>
<summary>What is the difference between Radiobuttons and Checkbuttons?</summary>

| Feature | Radiobutton | Checkbutton |
|---------|------------|-------------|
| Selection | One at a time (mutually exclusive) | Any number at once |
| Shared variable? | Yes — all share one `IntVar` | No — each has its own `IntVar` |
| Use case | "Pick one size" | "Pick any toppings" |

```python
# Radiobutton — only one can be selected
self.size_var = tkinter.IntVar()
tkinter.Radiobutton(..., variable=self.size_var, value=1)
tkinter.Radiobutton(..., variable=self.size_var, value=2)

# Checkbutton — each is independent
self.extra_cheese = tkinter.IntVar()
self.mushrooms    = tkinter.IntVar()
tkinter.Checkbutton(..., variable=self.extra_cheese)
tkinter.Checkbutton(..., variable=self.mushrooms)
```

</details>

---

## 13. Listbox Widgets

A **Listbox widget** displays a scrollable list of items from which the user can select one or more.

### Creating and Populating a Listbox

```python
self.listbox = tkinter.Listbox(self.main_window, height=0, width=0)
self.listbox.pack(padx=10, pady=10)

# Insert items using tkinter.END to always add to the bottom
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    self.listbox.insert(tkinter.END, day)
```

### Retrieving the Selected Item

```python
def show_selection(self, event):
    index = self.listbox.curselection()   # Returns a tuple of selected indexes
    item  = self.listbox.get(index)       # Gets the item at that index
    tkinter.messagebox.showinfo('Selected', item)
```

Bind a callback so it fires when the user clicks an item:

```python
self.listbox.bind('<<ListboxSelect>>', self.show_selection)
```

### Selection Modes

| Mode | Behavior |
|------|----------|
| `tkinter.BROWSE` | One item at a time (default) |
| `tkinter.SINGLE` | One item at a time, no drag-select |
| `tkinter.MULTIPLE` | Any items, click to toggle |
| `tkinter.EXTENDED` | Range selection with click-drag |

### Adding a Scrollbar

```python
self.frame = tkinter.Frame(self.main_window)
self.frame.pack()

self.listbox   = tkinter.Listbox(self.frame, height=6, width=0)
self.listbox.pack(side='left')

self.scrollbar = tkinter.Scrollbar(self.frame, orient=tkinter.VERTICAL)
self.scrollbar.pack(side='right', fill=tkinter.Y)

self.scrollbar.config(command=self.listbox.yview)
self.listbox.config(yscrollcommand=self.scrollbar.set)
```

**Quick Check:**

<details>
<summary>How do you retrieve the item a user selected from a Listbox?</summary>

Use `curselection()` to get the index of the selected item, then pass that index to `get()`:

```python
def show_item(self, event):
    index = self.listbox.curselection()   # e.g. (2,) — a tuple
    item  = self.listbox.get(index)       # e.g. 'Wednesday'
    tkinter.messagebox.showinfo('You selected', item)
```

`curselection()` returns a **tuple** — even when only one item is selected. If nothing is selected, it returns an empty tuple `()`.

The `event` parameter is required when the callback is bound with `.bind()` — tkinter passes an event object automatically even though you may not use it.

</details>

---

## 14. Drawing Shapes with the Canvas Widget

The **Canvas widget** is a blank rectangular area where you can draw 2D graphics programmatically.

### Coordinate System

Canvas uses a screen coordinate system where `(0, 0)` is the **upper-left corner**. X increases to the right; Y increases **downward**.

### Creating a Canvas

```python
self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
self.canvas.pack()
```

### Drawing Methods

| Method | Description |
|--------|-------------|
| `create_line(x1, y1, x2, y2)` | Draws a line from point 1 to point 2 |
| `create_rectangle(x1, y1, x2, y2)` | Draws a rectangle (upper-left to lower-right) |
| `create_oval(x1, y1, x2, y2)` | Draws an oval inside a bounding rectangle |
| `create_arc(x1, y1, x2, y2, start=, extent=)` | Draws an arc (pie slice shape) |
| `create_polygon(x1, y1, x2, y2, ...)` | Draws a filled polygon from a list of vertices |
| `create_text(x, y, text=)` | Draws text centered at the given coordinates |

### Examples

```python
# Draw two diagonal lines forming an X
self.canvas.create_line(0, 0, 199, 199)
self.canvas.create_line(199, 0, 0, 199)

# Draw a rectangle
self.canvas.create_rectangle(50, 50, 150, 150)

# Draw a circle (oval with equal bounding box)
self.canvas.create_oval(20, 20, 100, 100)

# Draw an arc (pie slice starting at 45°, spanning 90°)
self.canvas.create_arc(10, 10, 190, 190, start=45, extent=90)

# Display text
self.canvas.create_text(100, 100, text='Hello World')
```

**Quick Check:**

<details>
<summary>How does the Canvas coordinate system work?</summary>

The Canvas uses a 2D grid where `(0, 0)` is the **upper-left corner** of the canvas. X values increase going right; Y values increase going **down** (the opposite of a standard math graph).

```
(0,0) ──────────────► X
  │
  │    (50, 30) ← 50 pixels right, 30 pixels down
  │
  ▼
  Y
```

For drawing methods that take two coordinate pairs (like `create_rectangle`), the first pair is the **upper-left corner** and the second is the **lower-right corner**:

```python
# Rectangle from (20,20) to (180,180)
self.canvas.create_rectangle(20, 20, 180, 180)
```

For ovals and arcs, the two coordinate pairs define the **bounding rectangle** — the oval is drawn to fit inside it.

</details>

<details>
<summary>What is the difference between create_oval and create_arc?</summary>

- **`create_oval`** draws a complete ellipse (or circle) inside its bounding rectangle.
- **`create_arc`** draws a **portion** of an ellipse — a pie-slice shape — defined by a starting angle and an extent (how many degrees to sweep counterclockwise).

```python
# Full oval
self.canvas.create_oval(20, 20, 100, 100)

# Arc starting at 45°, sweeping 90° counterclockwise
self.canvas.create_arc(20, 20, 100, 100, start=45, extent=90)
```

`start=0` points to the right (3 o'clock position). Angles increase counterclockwise. `extent=360` would draw a full circle.

</details>

---

## 📝 Key Terms Summary

| Term | Definition |
|------|------------|
| **GUI** | Graphical User Interface — a visual interface using buttons, fields, and windows |
| **CLI** | Command Line Interface — a text-based interface where users type commands |
| **Event-driven** | A programming style where code runs in response to user actions (events) |
| **Widget** | A graphical element in a GUI — button, label, entry field, etc. |
| **tkinter** | Python's built-in module for creating GUI programs |
| **`mainloop()`** | Starts the tkinter event loop; keeps the window open and responsive |
| **`pack()`** | Positions a widget inside its parent container and makes it visible |
| **Callback function** | A method that executes automatically when an event occurs (e.g., button click) |
| **`Label`** | Widget that displays static or dynamic text |
| **`Button`** | Widget that triggers a callback when clicked |
| **`Entry`** | Single-line text input widget; `.get()` retrieves the typed value |
| **`StringVar`** | A tkinter variable class linked to a widget; updating it updates the widget |
| **`textvariable=`** | Argument that links a Label to a `StringVar` for dynamic display |
| **`Frame`** | Invisible container widget used to group and organize other widgets |
| **`Radiobutton`** | Mutually exclusive selection widget; all in a group share one `IntVar` |
| **`Checkbutton`** | Independent toggle widget; each has its own `IntVar` |
| **`IntVar`** | A tkinter variable class that holds an integer; used with radio/check buttons |
| **`Listbox`** | Widget that displays a scrollable list; `.curselection()` returns selected index |
| **`Canvas`** | Widget for drawing 2D graphics; coordinate origin is the upper-left corner |
| **Internal padding** | Space inside a widget's border (`ipadx`, `ipady`) |
| **External padding** | Space outside a widget's border (`padx`, `pady`) |

---

*Chapter 13 — Starting Out with Python, Fifth Edition by Tony Gaddis*
