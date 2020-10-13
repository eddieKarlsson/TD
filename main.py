import tkinter as tk
from ui import TdUI
from settings import Settings

# Instanciate settings
s = Settings()

# Call UI
root = tk.Tk()
ui_app = TdUI(master=root)
ui_app.mainloop()

# when app exits save user Settings
user_settings = ui_app.get_user_settings()
s.store_user_settings(user_settings)
