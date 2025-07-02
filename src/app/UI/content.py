import customtkinter as ctk
import tkinter as tk
from PIL import Image
import app.logics.logics as lg
import os
import app.settings.settings as s

class main_app(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(sticky="nsew")
        self.logo_path = "./app/UI/assets/icons/icon256x256.png"

# May be removed
        self.tabview = None
        self.table_frame = None

        self.display()

    def display(self):
        self.clear()

        if not s.db_instance: 
            self.show_logo()
        else:
#             self.show_ui()
            self.show_tabs() # Will probably be removed

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_logo(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        logo = ctk.CTkImage(light_image=Image.open(self.logo_path), size=(256, 256))
        label = ctk.CTkLabel(frame, text="", image=logo)
        label.grid(row=0, column=0, padx=10, pady=10)
    
    def show_ui(self):
# Show action bar: new db, open db, save, export, undo, redo, new inventory, edit inventory props, new component, delete component
# Build paned window: vertical split
# Build paned left window: horizontal split
### Top split: tabs and tabs content
### Bottom split: default empty and doesn't show
# Build right panel: default empty and doesn't show
        pass







#TO DO: COMPLETE REWORK    
    def show_tabs(self):
        self.tabbar_frame = ctk.CTkFrame(self)    
        self.tabbar_frame.pack(fill="x", padx=10, pady=(10, 0))
        self.tabview = ctk.CTkTabview(self.tabbar_frame)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)
        self.tab_content_frame = ctk.CTkFrame(self)
        self.tab_content_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        if not len(s.db.inventories)==0:
            for ivt in s.db.inventories:
                tab = self.tabview.add(ivt)
                self.build_table(tab, s.db.inventories[ivt])
        else:
            print("Empty Database")

    def build_table(self, parent, current_ivt):
        self.table_frame = ctk.CTkFrame(parent)
        self.table_frame.pack(expand=True, fill="both")
        rows=current_ivt.items.copy()
        cols = current_ivt.properties['fields'].copy()
        print(len(rows))
        if not len(rows)==0:
            i=0
            for r in rows:
                j=0
                for c in cols:
                    value = r.properties[c] if c in r.properties else ""
                    entry = ctk.CTkEntry(self.table_frame, width=100)
                    entry.insert(0, value)
                    entry.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                    j+=1
                i+=1
                if i>len(rows):
                    break
        else:
            print("Empty inventory")
#END TO DO
