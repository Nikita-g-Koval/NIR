from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from decimal import Decimal
import chart
import function

class MasterWindow:
    """Класс MasterWindow - инициализирует главное окно программы."""
    def __init__(self):
        """Устанавливает все необходимые атрибуты для объекта MasterWindow."""

        self.master_window = Tk()
        self.master_window.title("Работа с функцией")
        self.master_window.geometry('925x350')
        self.master_window.resizable(True, True)

        self.values = None

        self.period_label = Label(self.master_window, text='Период')
        self.period_label.grid(row=0, column=0)
        self.period_entry = Entry(self.master_window, width=30)
        self.period_entry.grid(row=1, column=0)

        self.left_bound_label = Label(self.master_window, text='Левая граница')
        self.left_bound_label.grid(row=0, column=1)
        self.left_bound_entry = Entry(self.master_window, width=30)
        self.left_bound_entry.grid(row=1, column=1)

        self.right_bound_label = Label(self.master_window, text='Правая граница')
        self.right_bound_label.grid(row=0, column=2)
        self.right_bound_entry = Entry(self.master_window, width=30)
        self.right_bound_entry.grid(row=1, column=2)

        self.step_label = Label(self.master_window, text='Шаг')
        self.step_label.grid(row=0, column=3)
        self.step_entry = Entry(self.master_window, width=30)
        self.step_entry.grid(row=1, column=3)

        self.margin_of_error_label = Label(self.master_window, text='Погрешность')
        self.margin_of_error_label.grid(row=0, column=4)
        self.margin_of_error_entry = Entry(self.master_window, width=30)
        self.margin_of_error_entry.grid(row=1, column=4)

        self.columns = ("x", "f(x)")

        self.tree = ttk.Treeview(self.master_window, columns=self.columns, show="headings")
        self.tree.grid(row=3, column=0, sticky=NSEW, columnspan=5)

        self.tree.heading("x", text="x", anchor=W)
        self.tree.heading("f(x)", text="f(x)", anchor=W)

        self.scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=3, column=4, sticky="nse")

        self.chart_btn = Button(self.master_window, text='График', command=chart.show_chart)
        self.chart_btn.grid(row=4, column=0, sticky=NSEW)

        self.show_spreadsheet_btn = Button(self.master_window, text='Рассчитать значения', command=self.show_values)
        self.show_spreadsheet_btn.grid(row=4, column=1, sticky=NSEW)

        self.save_file_btn = Button(self.master_window, text='Сохранить', command=self.save_file)
        self.save_file_btn.ёgrid(row=4, column=2, sticky=NSEW)

        self.master_window.mainloop()

    def show_values(self):
        if not str.isdigit(self.period_entry.get()):
            messagebox.showwarning(message="Период должен быть числом!", title="Предупреждение")
            return
        if not str.isdigit(self.margin_of_error_entry.get()):
            messagebox.showwarning(message="Погрешность должна быть числом!", title="Предупреждение")
            return

        margin_of_error = int(self.margin_of_error_entry.get())

        try:
            step = Decimal(self.step_entry.get())
            left_bound = Decimal(self.left_bound_entry.get())
            right_bound = Decimal(self.right_bound_entry.get())
        except Exception as _ex:
            messagebox.showwarning(message="Шаг и границы должны быть числом!", title="Предупреждение")
            return

        self.values = function.get_values(left_bound, right_bound, step, margin_of_error)

        for value in self.values:
            self.tree.insert("", END, values=value)

    def save_file(self):
        if self.values is None:
            messagebox.showwarning(message="Сначала рассчитайте значения!", title="Предупреждение")
            return

        path = filedialog.asksaveasfilename(defaultextension="csv", initialfile="Table1.csv")

        if path == "":
            messagebox.showwarning(message="Путь к файлу не был указан!", title="Предупреждение")
            return

        text = ""
        for value in self.values:
            text += f"{value[0]}, {value[1]}\n"

        with open(path, "w") as file:
            file.write(text)

        messagebox.showinfo(message="Файл успешно сохранён.", title="Уведомление")




