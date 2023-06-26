from tkinter import messagebox, Entry, Button, Toplevel
from customtkinter import CTkButton, CTkLabel, CTkFont
from employee_window import EmployeeWindow
from admin_window import AdminWindow
from admin_login import AdminLogin

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create the UI elements for the main window
        self.welcomeLabel = CTkLabel(self.master, text='WELCOME', font=CTkFont(size=20, weight="bold"), width=30, height=2)
        self.welcomeLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.employee_button = CTkButton(self.master, text='Employee Window', command=self.employee_window)
        self.employee_button.grid(row=1, column=0, padx=10, pady=10)

        self.admin_button = CTkButton(self.master, text='Admin Window', command=self.admin_window)
        self.admin_button.grid(row=1, column=1, padx=10, pady=10)

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

    def employee_window(self):
        empwind = Toplevel(self.master)
        emp_window = EmployeeWindow(empwind, self.master)

    def admin_window(self):
        adlog_wind = Toplevel(self.master)
        admin_login = AdminLogin(adlog_wind, self.master)

    def close_window(self):
        confirmed = messagebox.askyesno("Exit", "Are you sure you want to close the application?")
        if confirmed:
            self.master.destroy()
            self.main_window.destroy()

        self.master.protocol("WM_DELETE_WINDOW", self.master.close_window)

