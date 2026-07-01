import tkinter as tk
from tkinter import ttk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Calculator")
        self.resizable(False, False)

        # Styles
        self.configure(bg="#1e1e1e")
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 12), padding=8)
        style.map("TButton", foreground=[("pressed", "white"), ("active", "white")])

        # State
        self.expression = tk.StringVar(value="")
        self.result_shown = False

        # Layout
        self._build_display()
        self._build_buttons()
        self._bind_keys()

    def _build_display(self):
        display_frame = ttk.Frame(self, padding=10)
        display_frame.grid(row=0, column=0, sticky="nsew")
        self.entry = ttk.Entry(
            display_frame,
            textvariable=self.expression,
            font=("Consolas", 18),
            justify="right"
        )
        self.entry.grid(row=0, column=0, sticky="nsew")
        self.entry.focus()

    def _build_buttons(self):
        btn_frame = ttk.Frame(self, padding=(10, 0, 10, 10))
        btn_frame.grid(row=1, column=0, sticky="nsew")

        buttons = [
            ("C", self.clear), ("⌫", self.backspace), ("(", self.insert_char), (")", self.insert_char),
            ("7", self.insert_char), ("8", self.insert_char), ("9", self.insert_char), ("/", self.insert_char),
            ("4", self.insert_char), ("5", self.insert_char), ("6", self.insert_char), ("*", self.insert_char),
            ("1", self.insert_char), ("2", self.insert_char), ("3", self.insert_char), ("-", self.insert_char),
            ("0", self.insert_char), (".", self.insert_char), ("=", self.evaluate), ("+", self.insert_char),
        ]

        # Grid configuration: 5 rows x 4 columns
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        r, c = 0, 0
        for text, cmd in buttons:
            action = (lambda t=text: cmd(t)) if cmd in (self.insert_char,) else cmd
            btn = ttk.Button(btn_frame, text=text, command=action)
            btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
            c += 1
            if c == 4:
                c = 0
                r += 1

    def _bind_keys(self):
        self.bind("<Key>", self._on_key)
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<KP_Enter>", lambda e: self.evaluate())
        self.bind("<Escape>", lambda e: self.clear())
        self.bind("<BackSpace>", lambda e: self.backspace())

    # Actions
    def insert_char(self, ch):
        if self.result_shown:
            # If a result was just shown, start a new expression when typing a number/paren/decimal
            if ch.isdigit() or ch in "().":
                self.expression.set("")
            self.result_shown = False
        self.expression.set(self.expression.get() + ch)

    def clear(self, *_):
        self.expression.set("")
        self.result_shown = False

    def backspace(self, *_):
        expr = self.expression.get()
        if expr:
            self.expression.set(expr[:-1])

    def evaluate(self, *_):
        expr = self.expression.get()
        if not expr.strip():
            return
        try:
            # Safe evaluation: allow only numbers and operators
            safe_expr = self._sanitize(expr)
            result = eval(safe_expr, {"__builtins__": None}, self._allowed_funcs())
            # Format: remove trailing .0 for integers
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression.set(str(result))
            self.result_shown = True
        except Exception:
            self.expression.set("Error")
            self.result_shown = True

    def _on_key(self, event):
        ch = event.char
        allowed = "0123456789+-*/()."
        if ch in allowed:
            self.insert_char(ch)

    def _sanitize(self, expr):
        # Replace common unicode chars if present, normalize
        expr = expr.replace("×", "*").replace("÷", "/")
        return expr

    def _allowed_funcs(self):
        # Extend with safe math functions if needed
        return {
            "abs": abs,
            "round": round,
            "pow": pow,
            "math": math
        }

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()