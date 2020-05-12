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
    user_data = {
        'excel_path': 'no file loaded',
        'output_path': 'no path selected',
        'gen_valve': True,
        'gen_motor': True,
        'gen_ai': True,
        'gen_ao': True,
        'gen_di': True,
        'gen_do': True
    }


class TD_UI:
    def __init__(self, master):
        """Constants"""
        self.height = 300
        self.width = 500
        self.frameColor = "#2b2b2b"
        self.buttonWidth = 0.18
        self.button_bg = "#2b2b2b"
        self.button_fg = "#FFFFFF"  # text color
        self.fontSize = 10
        self.buttonYSpacing = 0.12

        """Create drop-down menu"""
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # file submenu
        self.subMenu = tk.Menu(self.menu)
        self.subMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=master.quit)

        # view submenu
        self.viewSubMenu = tk.Menu(self.menu)
        self.viewSubMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=self.viewSubMenu)
        self.viewSubMenu.add_command(label="Log file", command=self.openLogFile)

        """Create window"""
        canvas = tk.Canvas(root, height=self.height, width=self.width)
        canvas.pack()
        frame = tk.Frame(root, bg=self.frameColor)
        frame.place(relwidth=1, relheight=1)

        """Create window contents"""
        # Excel button
        self.excelButton = tk.Button(root, text="Select Excel...", bg=self.button_bg, fg=self.button_fg, command=self.browseExcel)
        self.excelButton.place(relx=0.03, rely=0.07, relheight=0.08, relwidth=self.buttonWidth)
        # Excel path label
        self.excelLabel = tk.Label(frame, bg=self.button_bg, fg=self.button_fg, text=(user_data['excel_path']))
        self.excelLabel.place(relx=0.23, rely=0.07, relheight=0.08)

        # Output path button
        self.outpathButton = tk.Button(root, text="Output path...", bg=self.button_bg, fg=self.button_fg, command=self.outputPath)
        self.outpathButton.place(relx=0.03, rely=0.07 + self.buttonYSpacing, relheight=0.08, relwidth=self.buttonWidth)
        # Output path label
        self.outpathLabel = tk.Label(frame, bg=self.button_bg, fg=self.button_fg, text=(user_data['output_path']))
        self.outpathLabel.place(relx=0.23, rely=0.07 + self.buttonYSpacing, relheight=0.08)

    def browseExcel(self):
        excelPath = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        # Write to user_data dictionary, to save it for later.
        user_data['excel_path'] = excelPath
        # Update label
        self.excelLabel.config(text=excelPath)

    def outputPath(self):
        output_path = filedialog.askdirectory()
        # Write to user_data dictionary, to save it for later.
        user_data['output_path'] = output_path
        # Update label
        self.outpathLabel.config(text=output_path)

    def openLogFile(self):
        os.system('log.log')

    def doNothing(self):
        print('did nothing')




# Calls
root = tk.Tk()
root.title('MC TD Gen')
b = TD_UI(root)
root.mainloop()

# dump user data
with open('user_data.pickle', 'wb') as f:
    pickle.dump(user_data, f)
    print("dump")
