from app.UI.ui import window
import customtkinter as ctk
# import tkinter as tk

if __name__=="__main__":
    ctk.set_appearance_mode("light") # System, light, dark
    ctk.set_default_color_theme("blue")
    app = window()
    app.mainloop()