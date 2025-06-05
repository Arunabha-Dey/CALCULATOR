import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.configure(bg="#1e1e1e")
        master.resizable(False, False)

        self.entry = tk.Entry(master, width=30, font=("Arial", 18), borderwidth=5, relief=tk.FLAT, bg="#2e2e2e", fg="white", insertbackground="white")
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

        self.create_buttons()

    def click(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + value)

    def clear(self):
        self.entry.delete(0, tk.END)

    def delete(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def evaluate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def scientific(self, func):
        try:
            value = float(self.entry.get())
            if func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            elif func == "log":
                result = math.log10(value)
            elif func == "ln":
                result = math.log(value)
            elif func == "sqrt":
                result = math.sqrt(value)
            elif func == "exp":
                result = math.exp(value)
            elif func == "factorial":
                result = math.factorial(int(value))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def create_buttons(self):
        btn_texts = [
            ('7', '8', '9', '/', 'sin', 'cos'),
            ('4', '5', '6', '*', 'tan', 'log'),
            ('1', '2', '3', '-', 'sqrt', 'ln'),
            ('0', '.', '=', '+', '(', ')'),
            ('pi', 'e', 'exp', 'x^y', 'C', '⌫'),
            ('!', '', '', '', '', '')
        ]

        for r, row in enumerate(btn_texts):
            for c, text in enumerate(row):
                if text == '':
                    continue
                if text == '=':
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=self.evaluate, bg="#4caf50", fg="white", font=("Arial", 12))
                elif text == 'C':
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=self.clear, bg="#f44336", fg="white", font=("Arial", 12))
                elif text == '⌫':
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=self.delete, bg="#ff9800", fg="white", font=("Arial", 12))
                elif text in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'exp', 'factorial', '!']:
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=lambda t=text: self.scientific('factorial' if t == '!' else t), bg="#03a9f4", fg="white", font=("Arial", 12))
                elif text == 'pi':
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=lambda: self.click(str(math.pi)), bg="#9c27b0", fg="white", font=("Arial", 12))
                elif text == 'e':
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=lambda: self.click(str(math.e)), bg="#9c27b0", fg="white", font=("Arial", 12))
                elif text == 'x^y':
                    btn = tk.Button(self.master, text='x^y', width=5, height=2, command=lambda: self.click('**'), bg="#673ab7", fg="white", font=("Arial", 12))
                else:
                    btn = tk.Button(self.master, text=text, width=5, height=2, command=lambda t=text: self.click(t), bg="#333", fg="white", font=("Arial", 12))
                btn.grid(row=r + 1, column=c, padx=3, pady=3)

# Run the calculator
root = tk.Tk()
calc = ScientificCalculator(root)
root.mainloop()
