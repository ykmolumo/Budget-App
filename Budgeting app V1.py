import tkinter as tk

class BudgetApp:
    def __init__(self, master):
        self.master = master
        master.title("Budget App")

        # Income Label and Entry
        self.income_label = tk.Label(master, text="Income:")
        self.income_label.grid(row=0, column=0)
        self.income_entry = tk.Entry(master)
        self.income_entry.grid(row=0, column=1)

        # Expenses Label and Entry
        self.expenses_label = tk.Label(master, text="Expenses:")
        self.expenses_label.grid(row=1, column=0)
        self.expenses_entry = tk.Entry(master)
        self.expenses_entry.grid(row=1, column=1)

        # Calculate Budget Button
        self.calculate_button = tk.Button(master, text="Calculate Budget", command=self.calculate_budget)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        # Remaining Budget Label
        self.budget_label = tk.Label(master, text="Remaining Budget:")
        self.budget_label.grid(row=3, column=0)
        self.budget_result = tk.Label(master, text="")
        self.budget_result.grid(row=3, column=1)

    def calculate_budget(self):
        income = int(self.income_entry.get())
        expenses = int(self.expenses_entry.get())
        remaining_budget = income - expenses
        self.budget_result.configure(text=remaining_budget)

root = tk.Tk()
budget_app = BudgetApp(root)
root.mainloop()
