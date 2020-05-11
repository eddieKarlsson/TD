import tkinter as tk
from tkinter import filedialog
import pickle
from os import path

# load user data if it exists, otherwise create dict
if path.exists('user_data.pickle'):
    with open('user_data.pickle', 'rb') as f:
        user_data = pickle.load(f)
        print("loaded")
else:
    user_data = {
        'excel_path': 'no file loaded',
        'gen_valve': True,
        'gen_motor': True,
        'gen_ai': True,
        'gen_ao': True,
        'gen_di': True,
        'gen_do': True
    }


# constants
height = 300
width = 500
frameColor = "#2b2b2b"
button_bg = "#2b2b2b"
button_fg = "#D5D5D5"  # text color
fontSize = 10

print((user_data['excel_path']))

class TD_UI:
    def __init__(self, master):
        """Create window"""
        canvas = tk.Canvas(root, height=height, width=width)
        canvas.pack()
        frame = tk.Frame(root, bg=frameColor)
        frame.place(relwidth=1, relheight=1)

        """Create window contents"""
        # Excel button
        self.excelButton = tk.Button(root, text="Select Excel TD", bg=button_bg, fg=button_fg, command=self.browseExcel)
        self.excelButton.place(relx=0.05, rely=0.1, relheight=0.08)
        # Excel path label
        self.excelLabel = tk.Label(frame, bg=button_bg, fg=button_fg, text=(user_data['excel_path']))
        self.excelLabel.place(relx=0.28, rely=0.1, relheight=0.08)

    def browseExcel(self):
        excelPath = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        # Write to user_data dictionary, to save it for later.
        user_data['excel_path'] = excelPath
        # Update label
        self.excelLabel.config(text=excelPath)

        print(user_data['excel_path'])



# Call
root = tk.Tk()
root.title('MC TD Gen')
b = TD_UI(root)
root.mainloop()

# dump user data
with open('user_data.pickle', 'wb') as f:
    pickle.dump(user_data, f)
    print("dump")