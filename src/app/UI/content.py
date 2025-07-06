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
        self.active_windows={}
        #Content
        self.top_bar=None
        self.right_frame=None
        self.left_bottom=None
        self.splitted_window = None
        self.tabview = None
        #Local save to conserve panels sizes
        self.previous_height=0
        self.previous_width=0

        self.grid_rowconfigure(0, weight=0, minsize=0)
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

    def update_visibility(self):
        if self.left_bottom:
            if len(self.left_bottom.winfo_children()) == 0:
                self.left_paned.forget(self.left_bottom)
            elif self.left_bottom not in self.left_paned.panes():
                self.left_paned.add(self.left_bottom)
        if self.right_frame:
            if len(self.right_frame.winfo_children()) == 0:
                if self.right_frame in self.splitted_window.panes():
                    self.splitted_window.forget(self.right_frame)
            elif self.right_frame not in self.splitted_window.panes():
                self.splitted_window.add(self.right_frame)

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
    def show_ui(self):
        self.top_bar = ctk.CTkFrame(self)
        new_db_btn = ctk.CTkButton(self.top_bar, text="Test")
        new_db_btn.pack(side="left")
        self.top_bar.grid_propagate(True)
        self.top_bar.grid(row=0, column=0, sticky="nsew")

        self.splitted_window = tk.PanedWindow(self, orient="horizontal")
        
        self.left_frame = ctk.CTkFrame(self.splitted_window)
        self.left_paned = tk.PanedWindow(self.left_frame, orient="vertical")

        self.left_top = ctk.CTkFrame(self.left_paned)
        self.tabview = Tabs(self.left_top)
        self.tabview.pack(fill="both", expand=True)

        self.left_paned.add(self.left_top)

        self.left_bottom = ctk.CTkFrame(self.left_paned)
        self.left_paned.add(self.left_bottom)

        self.left_paned.pack(expand=True, fill='both')

        self.right_frame = ctk.CTkFrame(self.splitted_window)

        self.splitted_window.add(self.left_frame)
        self.splitted_window.add(self.right_frame)
        self.splitted_window.grid(row=1, column=0, sticky="nsew")

        self.after(100, self.adjust_sashes)

    def adjust_sashes(self):
        self.left_paned.update_idletasks()
        height = self.left_paned.winfo_height()

        if height != self.previous_height:
            self.previous_height = height
            top_height = int(height * 0.7)
            self.left_paned.sash_place(0, 0, top_height)

        self.splitted_window.update_idletasks()
        width = self.splitted_window.winfo_width()

        if width != self.previous_width:
            self.previous_width = width
            left_width = int(width * 0.7)
            self.splitted_window.sash_place(0, left_width, 0)

        self.update_visibility()

        self.after(100, self.adjust_sashes)
