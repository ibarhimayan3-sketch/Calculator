import customtkinter as ctk

# ==========================================
# Calculator v2.0
# Part 1
# ==========================================

# ------------------------------------------
# Window
# ------------------------------------------
app = ctk.CTk()
app.title("Calculator v2.0")
app.geometry("900x650")
app.minsize(900, 650)

# ------------------------------------------
# Calculator Memory
# ------------------------------------------
first_number = None
operation = None
history_visible = False
# ------------------------------------------
# History Panel
# ------------------------------------------

history_frame = ctk.CTkFrame(
    app,
    width=250,
    height=500
)

history_label = ctk.CTkLabel(
    history_frame,
    text="History",
    font=("Arial", 22, "bold")
)
history_label.pack(pady=15)

history = ctk.CTkTextbox(
    history_frame,
    width=220,
    height=350
)

history.pack(pady=10)

history.configure(state="disabled")

# ------------------------------------------
# Main Calculator Frame
# ------------------------------------------
frame = ctk.CTkFrame(app)
frame.place(relx=0.5, rely=0.5, anchor="center")

# ------------------------------------------
# Display
# ------------------------------------------
entry = ctk.CTkEntry(
    frame,
    width=300,
    height=45,
    font=("Arial", 22),
    state="readonly"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=15
)

# ==========================================
# FUNCTIONS
# ==========================================

def unlock_display():
    entry.configure(state="normal")


def lock_display():
    entry.configure(state="readonly")


def clear_display():
    unlock_display()
    entry.delete(0, "end")
    lock_display()


def add_number(number):
    unlock_display()
    entry.insert("end", number)
    lock_display()


def plus():
    global first_number
    global operation

    first_number = entry.get()
    operation = "+"
    clear_display()


def minus():
    global first_number
    global operation

    first_number = entry.get()
    operation = "-"
    clear_display()


def multiply():
    global first_number
    global operation

    first_number = entry.get()
    operation = "*"
    clear_display()


def divide():
    global first_number
    global operation

    first_number = entry.get()
    operation = "/"
    clear_display()

def clear_history():

    history.configure(state="normal")

    history.delete("1.0", "end")

    history.configure(state="disabled")

def toggle_history():

    global history_visible

    if history_visible:

        history_frame.place_forget()

        history_visible = False

    else:

        history_frame.place(
            relx=0.17,
            rely=0.5,
            anchor="center"
        )

        history_visible = True

def equals():

    global first_number
    global operation

    if first_number is None:
        return

    second_number = entry.get()

    if second_number == "":
        return

    num1 = float(first_number)
    num2 = float(second_number)

    if operation == "+":
        answer = num1 + num2

    elif operation == "-":
        answer = num1 - num2

    elif operation == "*":
        answer = num1 * num2

    elif operation == "/":

        if num2 == 0:
            clear_display()
            unlock_display()
            entry.insert(0, "Cannot divide by 0")
            lock_display()
            return

        answer = num1 / num2

    clear_display()

    unlock_display()
    entry.insert(0, str(answer))
    lock_display()

    history.configure(state="normal")

    history.insert(
        "end",
        f"{num1} {operation} {num2} = {answer}\n"
    )

    history.see("end")

    history.configure(state="disabled")

def change_button_color(color):

    for button in all_buttons:

        button.configure(
            fg_color=color
        )
# ------------------------------------------
# Save to History
# ------------------------------------------


history.configure(state="disabled")
# ------------------------------------------
# Save to History
# ------------------------------------------


# ==========================================
# NUMBER BUTTONS
# ==========================================

# -------- Row 1 --------
button7 = ctk.CTkButton(frame, text="7", width=70, command=lambda: add_number("7"))
button7.grid(row=1, column=0, padx=8, pady=8)

button8 = ctk.CTkButton(frame, text="8", width=70, command=lambda: add_number("8"))
button8.grid(row=1, column=1, padx=8, pady=8)

button9 = ctk.CTkButton(frame, text="9", width=70, command=lambda: add_number("9"))
button9.grid(row=1, column=2, padx=8, pady=8)

plus_button = ctk.CTkButton(frame, text="+", width=70, command=plus)
plus_button.grid(row=1, column=3, padx=8, pady=8)

# -------- Row 2 --------
button4 = ctk.CTkButton(frame, text="4", width=70, command=lambda: add_number("4"))
button4.grid(row=2, column=0, padx=8, pady=8)

button5 = ctk.CTkButton(frame, text="5", width=70, command=lambda: add_number("5"))
button5.grid(row=2, column=1, padx=8, pady=8)

button6 = ctk.CTkButton(frame, text="6", width=70, command=lambda: add_number("6"))
button6.grid(row=2, column=2, padx=8, pady=8)

minus_button = ctk.CTkButton(frame, text="-", width=70, command=minus)
minus_button.grid(row=2, column=3, padx=8, pady=8)

# -------- Row 3 --------
button1 = ctk.CTkButton(frame, text="1", width=70, command=lambda: add_number("1"))
button1.grid(row=3, column=0, padx=8, pady=8)

button2 = ctk.CTkButton(frame, text="2", width=70, command=lambda: add_number("2"))
button2.grid(row=3, column=1, padx=8, pady=8)

button3 = ctk.CTkButton(frame, text="3", width=70, command=lambda: add_number("3"))
button3.grid(row=3, column=2, padx=8, pady=8)

multiply_button = ctk.CTkButton(frame, text="×", width=70, command=multiply)
multiply_button.grid(row=3, column=3, padx=8, pady=8)

# -------- Row 4 --------
button0 = ctk.CTkButton(frame, text="0", width=70, command=lambda: add_number("0"))
button0.grid(row=4, column=0, padx=8, pady=8)

equals_button = ctk.CTkButton(frame, text="=", width=70, command=equals)
equals_button.grid(row=4, column=1, padx=8, pady=8)

clear_button = ctk.CTkButton(frame, text="AC", width=70, command=clear_display)
clear_button.grid(row=4, column=2, padx=8, pady=8)

divide_button = ctk.CTkButton(frame, text="÷", width=70, command=divide)
divide_button.grid(row=4, column=3, padx=8, pady=8)
# ------------------------------------------
# Save to History
# ------------------------------------------


# ------------------------------------------
# History Button
# ------------------------------------------

history_button = ctk.CTkButton(
    app,
    text="📜 History",
    width=120,
    command=toggle_history
)

history_button.place(
    relx=0.5,
    rely=0.87,
    anchor="center"
)


#theme_button.place(
 #   relx=0.5,
 #   rely=0.94,
 #   anchor="center"
#)

all_buttons = [
    button0,
    button1,
    button2,
    button3,
    button4,
    button5,
    button6,
    button7,
    button8,
    button9,

    plus_button,
    minus_button,
    multiply_button,
    divide_button,

    equals_button,

    clear_button
]
# ------------------------------------------
# Run
# ------------------------------------------
app.mainloop()