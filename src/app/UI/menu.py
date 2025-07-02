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

    def about_window():
        try:
            print(window.about_window_tl.winfo_exists())
        except:
            about_window_tl = ctk.CTkToplevel(window)

            about_window_tl.title("About")
            about_window_tl.geometry('268x390')
            about_window_tl.resizable(False,False)
            about_window_tl.wm_attributes('-toolwindow', True)
            
            frame = ctk.CTkFrame(master=about_window_tl)
            app_icon = ctk.CTkImage(light_image=Image.open("./app/UI/assets/icons/icon256x256.png"),size=(256,256))
            frame.app_icon_label = ctk.CTkLabel(frame, text="", image=app_icon)
            frame.about_label = ctk.CTkLabel(frame, text=f"Made with love by Yakari_68\nfor MBOT (ENSISA, Mulhouse, France)\n\nPython v.{s.pyversion}\nCTK v.{s.ctkversion}\n")
            about_window_tl.grid_columnconfigure(0, weight=1)
            frame.app_icon_label.grid(row=0, padx=5, pady=5)
            frame.about_label.grid(row=1, padx=5, pady=20)
            frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
            
            x = window.winfo_x() + window.winfo_width()//2 - about_window_tl.winfo_width()//2
            y = window.winfo_y() + window.winfo_height()//2 - about_window_tl.winfo_height()//2
            about_window_tl.geometry(f"+{x}+{y}")
        about_window_tl.grab_set()
        about_window_tl.after(50,about_window_tl.lift())



    def new_database():
        try:
            print(window.newdb_window_tl.winfo_exists())
        except:
            inventory_widget = []

            newdb_window_tl = ctk.CTkToplevel(window)
            newdb_window_tl.title("New Database")
            newdb_window_tl.geometry('600x600')

            db_name_field=ctk.CTkEntry(newdb_window_tl, placeholder_text="DB Name")
            db_path_field=ctk.CTkEntry(
                newdb_window_tl,
                placeholder_text="DB Location",
                textvariable=tk.StringVar(newdb_window_tl,os.getcwd()))
            db_formats_label=ctk.CTkLabel(newdb_window_tl, text="Database Type:")
            db_formats = s.formats
            formats = ctk.CTkOptionMenu(newdb_window_tl, values=db_formats)

            newdb_window_tl.grid_columnconfigure(0, weight=0)
            newdb_window_tl.grid_columnconfigure(1, weight=1)
            newdb_window_tl.grid_columnconfigure(2, weight=1)
            newdb_window_tl.grid_columnconfigure(3, weight=0)

            newdb_window_tl.grid_rowconfigure(0, weight=0)
            newdb_window_tl.grid_rowconfigure(1, weight=0)
            newdb_window_tl.grid_rowconfigure(2, weight=1)
            newdb_window_tl.grid_rowconfigure(3, weight=0)
            
            db_name_field.grid(column=1, row=0, padx=(80,5), pady=15, sticky="we")
            db_path_field.grid(column=2, row=0, padx=(5,80), pady=15, sticky="we")
            db_formats_label.grid(column=1, row=1, padx=(80,5), pady=15, sticky="we")
            formats.grid(column=2, row=1, padx=(5,80), pady=15, sticky="we")

            inventory_frame = ctk.CTkScrollableFrame(newdb_window_tl)
            inventory_frame.grid(column=1, row=2, padx=80, pady=15, sticky="nswe", columnspan=2, )

            def add_column(inventory_data, column_frame):
                index = len(inventory_data["columns"])
                entry = ctk.CTkEntry(column_frame,
                                     placeholder_text=f"Column {index+1}")
                row = index // 2
                column = index % 2
                entry.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
                inventory_data["columns"].append(entry)

            def new_inventory():
                newdb_window_tl.update()
                inventory_data = {"name": None, "columns": []}

                frame = ctk.CTkFrame(inventory_frame)
                frame.pack(pady=10, anchor="center")

                name_entry = ctk.CTkEntry(frame ,placeholder_text="Inventory name")
                name_entry.pack(padx=30, pady=5, fill="x")
                inventory_data["name"] = name_entry

                column_frame = ctk.CTkFrame(frame)
                column_frame.pack(pady=2, padx=10, fill="x")
                add_column_button = ctk.CTkButton(frame, text="+", width=30, command=lambda: add_column(inventory_data, column_frame))
                add_column_button.pack(pady=2)

                inventory_data["column_frame"] = column_frame
                inventory_widget.append(inventory_data)

            new_inventory()
            new_inv_btn = ctk.CTkButton(newdb_window_tl, text="Add inventory", command=new_inventory)
            new_inv_btn.grid(column=1, row=3, padx=(80,5), pady=15, sticky="we")

            def prepare_db():
                name=db_name_field.get()
                path=db_path_field.get()
                db_format=formats.get()
                inventories={}
                for inventory in inventory_widget:
                    ivt_name = inventory["name"].get()
                    columns = [entry.get() for entry in inventory["columns"]]
                    inventories[ivt_name]=columns
                lg.create_database(name,path,db_format,inventories)
                newdb_window_tl.destroy()

            button_create_db=ctk.CTkButton(newdb_window_tl,text="Create Database", command=prepare_db)
            button_create_db.grid(column=2,row=3, padx=(5,80), pady=15, sticky="we")

            x = window.winfo_x() + window.winfo_width()//2 - newdb_window_tl.winfo_width()//2
            y = window.winfo_y() + window.winfo_height()//2 - newdb_window_tl.winfo_height()//2
            newdb_window_tl.geometry(f"+{x}+{y}")

        newdb_window_tl.grab_set()
        newdb_window_tl.after(50,newdb_window_tl.lift())

# Not good looking but works, don't touch
    def properties_window():
        try:
            print(window.props_window_tl.winfo_exists())
        except:
            props_window_tl = ctk.CTkToplevel(window)

            props_window_tl.title("Database Properties")
            props_window_tl.geometry('268x390')
            props_window_tl.resizable(False,False)
            props_window_tl.wm_attributes('-toolwindow', True)
            
            frame = ctk.CTkFrame(master=props_window_tl)
            props_window_tl.grid_columnconfigure(0, weight=1)
            i=0
            for p in s.db.properties:
                current_prop=ctk.CTkLabel(frame,text=p[0].upper()+p[1:].lower())
                current_prop.grid(row=i,column=1,padx=5,pady=5)
                if not (p=="created" or p=="updated"):
                    value=s.db.properties[p]
                else:
                    value=lg.format_date(lg.convert_date(s.db.properties[p]),s.time_format)
                prop_value=ctk.CTkLabel(frame,text=value)
                prop_value.grid(row=i,column=2,padx=5,pady=5)
                i+=1
            frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
            x = window.winfo_x() + window.winfo_width()//2 - props_window_tl.winfo_width()//2
            y = window.winfo_y() + window.winfo_height()//2 - props_window_tl.winfo_height()//2
            props_window_tl.geometry(f"+{x}+{y}")
        props_window_tl.grab_set()
        props_window_tl.after(50,props_window_tl.lift())
        
    
    
    
    
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