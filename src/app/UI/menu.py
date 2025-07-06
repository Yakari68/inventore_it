import app.settings.settings as s
import app.logics.logics as lg
import customtkinter as ctk
import tkinter as tk
from PIL import Image,ImageTk
from sys import platform
import os

def global_menu(window):
    gm=tk.Menu()

    def clique():
        print("cliqué!")
    def exit_app():
        window.destroy()

    def center_window(parent, window):
        window.update_idletasks()
        x = parent.winfo_x() + parent.winfo_width() // 2 - window.winfo_width() // 2
        y = parent.winfo_y() + parent.winfo_height() // 2 - window.winfo_height() // 2
        window.geometry(f"+{x}+{y}")

    def about_window():
        if getattr(window, "active_windows", None) is None:
            window.active_windows = {}
        if "about" in window.active_windows and window.active_windows["about"].winfo_exists():
            window.active_windows["about"].lift()
            window.active_windows["about"].focus()
            return

        about_tl = ctk.CTkToplevel(window)
        about_tl.title("About")
        about_tl.geometry('268x420')
        about_tl.resizable(False, False)
        about_tl.wm_attributes('-toolwindow', True)
        window.active_windows["about"] = about_tl
        frame = ctk.CTkFrame(master=about_tl)
        frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        icon_path = os.path.join("app", "UI", "assets", "icons", "icon256x256.png")
        app_icon = ctk.CTkImage(light_image=Image.open(icon_path), size=(256, 256))
        icon_label = ctk.CTkLabel(frame, text="", image=app_icon)
        icon_label.grid(row=0, padx=5, pady=5)
        version_label = ctk.CTkLabel(
            frame,
            text=(
                "Made with love by Yakari_68\n"
                "for MBOT (ENSISA, Mulhouse, France)\n\n"
                f"Python v.{s.pyversion}\n"
                f"CTK v.{s.ctkversion}\n\n"
                "Licensed under Apache 2.0\n"
                "Copyright 2025 Yakari_68\n"
            )
        )
        version_label.grid(row=1, padx=5, pady=20)
        center_window(window, about_tl)
        about_tl.grab_set()
        about_tl.after(50, about_tl.lift())

    def new_database():
        if getattr(window, "active_windows", None) is None:
            window.active_windows = {}
        
        if "new_database" in window.active_windows and window.active_windows["new_database"].winfo_exists():
            window.active_windows["new_database"].lift()
            window.active_windows["new_database"].focus()
            return

        inventory_widget = []
        newdb_window = ctk.CTkToplevel(window)
        newdb_window.title("New Database")
        newdb_window.geometry('600x600')
        window.active_windows["new_database"] = newdb_window
        db_name_entry = ctk.CTkEntry(newdb_window, placeholder_text="DB Name")
        db_path_entry = ctk.CTkEntry(
            newdb_window,
            placeholder_text="DB Location",
            textvariable=tk.StringVar(newdb_window, os.getcwd())
        )
        db_type_label = ctk.CTkLabel(newdb_window, text="Database Type:")
        db_format_menu = ctk.CTkOptionMenu(newdb_window, values=s.formats)
        newdb_window.grid_columnconfigure((0, 3), weight=0)
        newdb_window.grid_columnconfigure((1, 2), weight=1)
        newdb_window.grid_rowconfigure(2, weight=1)
        db_name_entry.grid(row=0, column=1, padx=(80, 5), pady=15, sticky="we")
        db_path_entry.grid(row=0, column=2, padx=(5, 80), pady=15, sticky="we")
        db_type_label.grid(row=1, column=1, padx=(80, 5), pady=15, sticky="we")
        db_format_menu.grid(row=1, column=2, padx=(5, 80), pady=15, sticky="we")
        inventory_frame = ctk.CTkScrollableFrame(newdb_window)
        inventory_frame.grid(row=2, column=1, columnspan=2, padx=80, pady=15, sticky="nsew")

        def add_column(inventory_data, column_frame):
            index = len(inventory_data["columns"])
            entry = ctk.CTkEntry(column_frame, placeholder_text=f"Column {index + 1}")
            row, col = divmod(index, 2)
            entry.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            inventory_data["columns"].append(entry)

        def new_inventory():
            inventory_data = {"name": None, "columns": []}
            frame = ctk.CTkFrame(inventory_frame)
            frame.pack(pady=10, anchor="center")
            name_entry = ctk.CTkEntry(frame, placeholder_text="Inventory name")
            name_entry.pack(padx=30, pady=5, fill="x")
            inventory_data["name"] = name_entry
            column_frame = ctk.CTkFrame(frame)
            column_frame.pack(pady=2, padx=10, fill="x")
            inventory_data["column_frame"] = column_frame
            add_btn = ctk.CTkButton(frame, text="+", width=30, command=lambda: add_column(inventory_data, column_frame))
            add_btn.pack(pady=2)
            inventory_widget.append(inventory_data)
        new_inventory()

        def prepare_db():
            name = db_name_entry.get()
            path = db_path_entry.get()
            db_format = db_format_menu.get()

            inventories = {}
            for inv in inventory_widget:
                ivt_name = inv["name"].get()
                columns = [col.get() for col in inv["columns"]]
                if ivt_name:
                    inventories[ivt_name] = columns

            lg.create_database(name, path, db_format, inventories)
            newdb_window.destroy()

        add_inv_btn = ctk.CTkButton(newdb_window, text="Add Inventory", command=new_inventory)
        add_inv_btn.grid(row=3, column=1, padx=(80, 5), pady=15, sticky="we")

        create_btn = ctk.CTkButton(newdb_window, text="Create Database", command=prepare_db)
        create_btn.grid(row=3, column=2, padx=(5, 80), pady=15, sticky="we")

        center_window(window, newdb_window)
        newdb_window.grab_set()
        newdb_window.after(50, newdb_window.lift())

# Not good looking but works, don't touch
    def properties_window():
        if getattr(window, "active_windows", None) is None:
            window.active_windows = {}

        if "properties" in window.active_windows and window.active_windows["properties"].winfo_exists():
            window.active_windows["properties"].lift()
            window.active_windows["properties"].focus()
            return

        props_window = ctk.CTkToplevel(window)
        props_window.title("Database Properties")
        props_window.geometry('350x400')
        props_window.resizable(False, False)
        props_window.wm_attributes('-toolwindow', True)
        window.active_windows["properties"] = props_window

        frame = ctk.CTkFrame(props_window)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        props_window.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=2)

        for i, prop in enumerate(s.db.properties):
            if prop=="id":
                continue
            label_name = ctk.CTkLabel(frame, text=prop.capitalize() + ":", anchor="w")
            label_name.grid(row=i, column=0, sticky="w", padx=5, pady=4)

            # Format dates if needed
            if prop in ("created", "updated"):
                value = lg.format_date(lg.convert_date(s.db.properties[prop]), s.time_format)
            else:
                value = s.db.properties[prop]

            label_value = ctk.CTkLabel(frame, text=str(value), anchor="w", wraplength=200)
            label_value.grid(row=i, column=1, sticky="w", padx=5, pady=4)

        center_window(window, props_window)
        props_window.grab_set()
        props_window.after(50, props_window.lift())
        
    
    
    
    
# Todo: Filetypes should depend from settings.py, where all the supported formats are listed
    def load_file():
        file = tk.filedialog.askopenfilename(
            filetypes=[("Inventore It! Database", "*.ivtdb"),("Text file", "*.txt"),("","*")],
            title="Choose a database"
        )
        lg.open_database(file)


    def draw_db_menu(gm):
        db_menu=tk.Menu(gm,tearoff=0)
        db_menu.add_command(label="New Database", command=new_database)
        db_menu.add_command(label="Open", command=load_file)
        """
        recent_menu=tk.Menu(gm,tearoff=0)
        for name in (lastfile):
            recent_menu.add_command(label=name, command=load_file(name))
        db_menu.add_cascade(label="Open recent", menu=recent_menu)
        """
        db_menu.add_separator()
        db_menu.add_command(label="Close", command=lg.close_database)
        db_menu.add_command(label="Save", command=clique)
        db_menu.add_command(label="Save as...", command=clique)
        export_menu=tk.Menu(gm,tearoff=0)
        """
        export_menu.add_command(label="PDF", command=db_to_pdf)
        export_menu.add_command(label="Excel(.xlsx)", command=db_to_xlsx)
        export_menu.add_command(label="LibreOffice(.ods)", command=db_to_ods)
        export_menu.add_command(label="csv", command=db_to_csv)
        """
        db_menu.add_cascade(label="Export as...", menu=export_menu)
        db_menu.add_separator()
        db_menu.add_command(label="Properties", command=properties_window)
        db_menu.add_separator()
        db_menu.add_command(label="Exit", command=exit_app)
        gm.add_cascade(label="Database", menu=db_menu)


    def draw_inventory_menu(gm):
        inventory_menu=tk.Menu(gm,tearoff=0)
        """
        inventory_menu.add_command(label="Undo", command=undo)
        inventory_menu.add_command(label="Redo", command=redo)
        inventory_menu.add_command(label="New Component", command=new_component)
        inventory_menu.add_command(label="Destroy Inventory", command=destroy_inventory)
        db_menu.add_separator()
        inventory_menu.add_command(label="New Inventory", command=new_inventory)
        """
        gm.add_cascade(label="Inventory", menu=inventory_menu)

    # def draw_file_menu(gm):
    def draw_help_menu(gm):
        help_menu=tk.Menu(gm,tearoff=0)
        help_menu.add_command(label="About", command=about_window)
        gm.add_cascade(label="Help", menu=help_menu)


    draw_db_menu(gm)
    draw_inventory_menu(gm)
#     draw_view_menu(gm)
    draw_help_menu(gm)
    window.configure(menu=gm)