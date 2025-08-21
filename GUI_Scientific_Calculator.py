#Features:
   # Basic Ops → +, -, *, /, %, ^
   # Scientific → sqrt, sin, cos, tan, log, exp, factorial
   # Constants → π, e
   # Brackets supported → ( and )

#Example:
   # sin(pi/2) → 1.0
   # log(100) → natural log (ln) = 4.605...
   # log(100,10) → works if you manually type in entry
   # 5! → press ! then enter number → math.factorial(5)

import tkinter as tk
import math

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        expression = expression.replace("^", "**")  # power operator

        # Evaluate safely with math functions
        result = str(eval(expression, {"__builtins__": None}, vars(math)))
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scientific Calculator")
    root.geometry("480x700")
    root.resizable(False, False)

    expression = ""
    equation = tk.StringVar()

    # === Display with scrollable Entry ===
    display_frame = tk.Frame(root, bd=5, relief="ridge")
    display_frame.grid(row=0, column=0, columnspan=5, sticky="nsew")

    input_field = tk.Entry(display_frame, textvariable=equation,
                           font=("Arial", 28, "bold"), bd=5, relief="sunken",
                           justify="right")
    input_field.pack(fill="both", expand=True, ipadx=8, ipady=25)

    # Enable horizontal scrolling (so long inputs are visible)
    input_field.config(xscrollcommand=True)

    # === Buttons Layout ===
    buttons = [
        ["7", "8", "9", "/", "sqrt("],
        ["4", "5", "6", "*", "log("],
        ["1", "2", "3", "-", "sin("],
        ["0", ".", "^", "+", "cos("],
        ["(", ")", "pi", "tan(", "exp("],
        ["C", "=", "e", "factorial(", "%"]
    ]

    # Create Buttons
    for i, row in enumerate(buttons):
        for j, text in enumerate(row):
            if text == "C":
                action = clear
            elif text == "=":
                action = equalpress
            elif text == "pi":
                action = lambda t=math.pi: press(t)
            elif text == "e":
                action = lambda t=math.e: press(t)
            else:
                action = lambda t=text: press(t)

            tk.Button(root, text=text, padx=20, pady=20,
                      font=("Arial", 16, "bold"),
                      command=action, bg="#f0f0f0").grid(row=i + 1, column=j, sticky="nsew")

    # Adjust Grid weights
    for i in range(6):
        root.grid_rowconfigure(i+1, weight=1)
    for j in range(5):
        root.grid_columnconfigure(j, weight=1)

    root.mainloop()
