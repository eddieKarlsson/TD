import tkinter as tk
from tkinter import filedialog

# constants
height = 400
width = 400
frameColor = "#2b2b2b"
button_bg = "#2b2b2b"
button_fg = "#D5D5D5"  # text color
fontSize = 8


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

        # self.printButton = Button(frame, text='Eddie printed', command=self.printMessage)
        # self.printButton.pack(side=LEFT)

        # self.quitButton = Button(frame, text='Quit', command=frame.quit)
        # self.quitButton.pack(side=LEFT)

    def browseExcel(self):
        excelPath = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))


# Call
root = tk.Tk()
root.title('MC TD Gen')
b = TD_UI(root)
root.mainloop()
