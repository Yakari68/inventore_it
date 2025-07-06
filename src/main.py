from app.UI.ui import window
import customtkinter as ctk
# import tkinter as tk

def test_display_on_right_frame(app):
    if hasattr(app.main_frame, 'right_frame') and app.main_frame.right_frame:
        label = ctk.CTkLabel(app.main_frame.right_frame, text="Testing")
        label.pack(padx=10, pady=10)
    else:
        app.after(1000, lambda: test_display_on_right_frame(app))

def test_display_on_left_bottom(app):
    if hasattr(app.main_frame, 'left_bottom') and app.main_frame.left_bottom:
        label = ctk.CTkLabel(app.main_frame.left_bottom, text="Testing too")
        label.pack(padx=10, pady=10)
    else:
        app.after(1000, lambda: test_display_on_left_bottom(app))

if __name__=="__main__":
    ctk.set_appearance_mode("light") # System, light, dark
    ctk.set_default_color_theme("blue")
    app = window()
#     app.after(1000, lambda: test_display_on_right_frame(app))
#     app.after(1000, lambda: test_display_on_left_bottom(app))
    app.mainloop()