from tkinter import *
root = Tk()
root.title("Colorful Calculator")
root.configure(bg="#333333")  # Set background color of the root window

e = Entry(root, width=14, borderwidth=5, font=('Helvetica', 24), fg="white", bg="#444444", justify='right')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "add"
    f_num = float(first_num)
    e.delete(0, END)

def equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + float(second_num))
    elif math == "sub":
        e.insert(0, f_num - float(second_num))
    elif math == "mul":
        e.insert(0, f_num * float(second_num))
    elif math == "div":
        if float(second_num) == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, f_num / float(second_num))
    elif math == "pow":
        e.insert(0, f_num ** float(second_num))

def sub():
    first_num = e.get()
    global f_num
    global math
    math = "sub"
    f_num = float(first_num)
    e.delete(0, END)

def mul():
    first_num = e.get()
    global f_num
    global math
    math = "mul"
    f_num = float(first_num)
    e.delete(0, END)

def div():
    first_num = e.get()
    global f_num
    global math
    math = "div"
    f_num = float(first_num)
    e.delete(0, END)

def pow():
    first_num = e.get()
    global f_num
    global math
    math = "pow"
    f_num = float(first_num)
    e.delete(0, END)

def square():
    num = float(e.get())
    e.delete(0, END)
    e.insert(0, num ** 2)

def cube():
    num = float(e.get())
    e.delete(0, END)
    e.insert(0, num ** 3)

button_colors = {
    "number": "#4CAF50",
    "operator": "#FF5722",
    "equal": "#FFC107",
    "clear": "#f44336",
    "bg": "#333333",
    "fg": "white"
}

button_config = {
    "font": ('Helvetica', 18),
    "padx": 20,
    "pady": 20,
    "bd": 0,
    "highlightthickness": 0,
    "activebackground": "#555555"
}

buttons = [
    ('7', 1, 0, "number"), ('8', 1, 1, "number"), ('9', 1, 2, "number"),
    ('4', 2, 0, "number"), ('5', 2, 1, "number"), ('6', 2, 2, "number"),
    ('1', 3, 0, "number"), ('2', 3, 1, "number"), ('3', 3, 2, "number"),
    ('0', 4, 0, "number"), ('+', 4, 1, "operator"), ('-', 4, 2, "operator"),
    ('*', 5, 0, "operator"), ('/', 5, 1, "operator"), ('=', 5, 2, "equal"),
    ('C', 6, 0, "clear"), ('^', 6, 1, "operator"), ('Square', 6, 2, "operator"),
    ('Cube', 6, 3, "operator"), ('Exit', 7, 3, "clear")
]

for (text, row, col, btype) in buttons:
    if text.isdigit():
        action = lambda x=text: button_click(x)
    elif text == '+':
        action = button_add
    elif text == '-':
        action = sub
    elif text == '*':
        action = mul
    elif text == '/':
        action = div
    elif text == '=':
        action = equal
    elif text == 'C':
        action = clear
    elif text == '^':
        action = pow
    elif text == 'Square':
        action = square
    elif text == 'Cube':
        action = cube
    elif text == 'Exit':
        action = root.quit

    button = Button(root, text=text, command=action, bg=button_colors[btype], fg=button_colors['fg'], **button_config)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
