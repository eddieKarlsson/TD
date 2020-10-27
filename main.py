import tkinter as tk
from ui import GenUI
from settings import Settings

"""Top-level script to call the UI and handle program flow"""

# Instanciate settings
s = Settings()

# Call UI
root = tk.Tk()
ui_app = GenUI(master=root)
ui_app.mainloop()

# when app exits save user Settings
user_settings = ui_app.get_user_settings()
s.store_user_settings(user_settings)
