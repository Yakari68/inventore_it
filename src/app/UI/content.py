import customtkinter as ctk
import tkinter as tk
from PIL import Image
import app.logics.logics as lg
import os
import app.settings.settings as s
from .tabs import Tabs

class main_app(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(sticky="nsew")
        self.logo_path = "./app/UI/assets/icons/icon256x256.png"
        self.right_frame=None
        self.left_bottom=None
        self.splitted_window = None
        self.tabview = None
        self.previous_height=0
        self.previous_width=0

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.display()

    def display(self):
        self.clear()

        if not s.db_instance: 
            self.show_logo()
        else:
            self.show_ui()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_logo(self):
        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew", rowspan=2)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        logo = ctk.CTkImage(light_image=Image.open(self.logo_path), size=(256, 256))
        label = ctk.CTkLabel(frame, text="", image=logo)
        label.grid(row=0, column=0, padx=10, pady=10)
    

# Show action bar: new db, open db, save, export, undo, redo, new inventory, edit inventory props, new component, delete component
# Build paned window: vertical split
# Build paned left window: horizontal split
### Top split: tabs and tabs content
### Bottom split: default empty and doesn't show
# Build right panel: default empty and doesn't show
        pass

    def show_ui(self):
        self.top_bar=ctk.CTkFrame(self)
        self.top_bar.grid(sticky="nsew", row=0)
        
        self.splitted_window = tk.PanedWindow(self, orient="horizontal")
        
        left_frame = ctk.CTkFrame(self.splitted_window)
        left_paned = tk.PanedWindow(left_frame, orient="vertical")
        left_top = ctk.CTkFrame(left_paned)
        
        self.tabview = Tabs(left_top)
        self.tabview.pack(fill="both", expand=True)
        
        left_paned.add(left_top)
        
        
        self.left_bottom = ctk.CTkFrame(left_paned)
        left_paned.add(self.left_bottom)
        left_paned.pack(expand=True, fill='both')
        
        
        self.right_frame = ctk.CTkFrame(self.splitted_window)
        self.splitted_window.add(left_frame)
        self.splitted_window.add(self.right_frame)
        self.splitted_window.grid(sticky="nsew", row=1)
        self.after(100, self.adjust_sashes, left_paned, self.splitted_window)

    def adjust_sashes(self, left_paned, main_paned):
        left_paned.update_idletasks()
        height = left_paned.winfo_height()
        
        if not height==self.previous_height:
            self.previous_height=height
            top_height = int(height * 0.7)
            left_paned.sash_place(0, 0, top_height)

        main_paned.update_idletasks()
        width = main_paned.winfo_width()
        if not width==self.previous_width:
            self.previous_width=width
            left_width = int(width * 0.7)
            main_paned.sash_place(0, left_width, 0)
    
        self.after(100, self.adjust_sashes, left_paned, self.splitted_window)