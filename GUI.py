import tkinter as tk
from tkinter import filedialog
import pickle
import os
from os import path

# load user data if it exists, otherwise create dict
if path.exists('user_data.pickle'):
    with open('user_data.pickle', 'rb') as f:
        user_data = pickle.load(f)
        print("loaded")
else:
    # if file doesn't exist initialize data to start-values
    user_data = {
        'excel_path': 'no file loaded',
        'output_path': 'no path selected',
    }

class TdUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Constants
        self.height = 300
        self.width = 500
        self.frameColor = "#2b2b2b"
        self.buttonWidth = 0.18
        self.button_bg = "#2b2b2b"
        self.button_fg = "#FFFFFF"  # text color
        self.fontSize = 10
        self.buttonYSpacing = 0.12
        self.checkbuttonYSpacing = 0.1

        # Call app
        self.create_window()
        self.create_window_contents()
        self.create_dropdown()

    def create_window(self):
        """Create window"""
        self.canvas = tk.Canvas(self.master, height=self.height, width=self.width)
        self.canvas.pack()
        self.frame = tk.Frame(self.master, bg=self.frameColor)
        self.frame.place(relwidth=1, relheight=1)

    def create_dropdown(self):
        """Create drop-down menu"""
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # file submenu
        self.subMenu = tk.Menu(self.menu)
        self.subMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.master.quit)

        # view submenu
        self.viewSubMenu = tk.Menu(self.menu)
        self.viewSubMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=self.viewSubMenu)
        self.viewSubMenu.add_command(label="Log file", command=self.open_logfile)
        self.viewSubMenu.add_command(label="Settings file", command=self.open_settings)


    def create_window_contents(self):
        """Create window contents"""
        # Excel button
        self.excelButton = tk.Button(self.master, text="Select Excel...", bg=self.button_bg, fg=self.button_fg,
                                     command=self.browse_excel)
        self.excelButton.place(relx=0.03, rely=0.07, relheight=0.08, relwidth=self.buttonWidth)
        # Excel path label
        self.excelLabel = tk.Label(self.frame, bg=self.button_bg, fg=self.button_fg, text=(user_data['excel_path']))
        self.excelLabel.place(relx=0.23, rely=0.07, relheight=0.08)

        # Output path button
        self.outpathButton = tk.Button(self.master, text="Output path...", bg=self.button_bg, fg=self.button_fg,
                                       command=self.output_path)
        self.outpathButton.place(relx=0.03, rely=0.07 + self.buttonYSpacing, relheight=0.08, relwidth=self.buttonWidth)
        # Output path label
        self.outpathLabel = tk.Label(self.frame, bg=self.button_bg, fg=self.button_fg, text=(user_data['output_path']))
        self.outpathLabel.place(relx=0.23, rely=0.07 + self.buttonYSpacing, relheight=0.08)

        # Run scripts
        self.run_program = tk.Button(self.master, text="Run script", bg=self.button_bg, fg=self.button_fg,
                                       command=self.run_python_windows_command)
        self.run_program.place(relx=0.03, rely=0.8, relheight=0.08, relwidth=self.buttonWidth)


    def browse_excel(self):
        excelPath = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        # Write to user_data dictionary, to save it for later.
        user_data['excel_path'] = excelPath
        # Update label
        self.excelLabel.config(text=excelPath)

    def output_path(self):
        output_path = filedialog.askdirectory()
        # Write to user_data dictionary, to save it for later.
        user_data['output_path'] = output_path
        # Update label
        self.outpathLabel.config(text=output_path)

    def open_logfile(self):
        os.system('log.log')

    def open_settings(self):
        os.system('settings.py')

    def run_python_windows_command(self):
        os.system('run.bat')



# Calls
root = tk.Tk()
root.title('MC TD Gen')
app = TdUI(master=root)
app.mainloop()

# dump user data
with open('user_data.pickle', 'wb') as f:
    pickle.dump(user_data, f)
    print("dump")
