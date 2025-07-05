import customtkinter as ctk
import app.settings.settings as s

class Tabs(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.tabs_dict = {}
        self.db_tabs()

        for tab_class in self.tabs_dict:
            for ivt_key, tab_data in self.tabs_dict[tab_class].items():
                tab_name = tab_data["name"]
                tab_content = tab_data["content"]

                tab = self.add(tab_name)

                table_frame = self.table_builder(tab, tab_name, tab_content)
                table_frame.pack(expand=True, fill="both")

    def db_tabs(self):
        self.tabs_dict['Inventories'] = {}
        for ivt_key, ivt in s.db.inventories.items():
            print("properties:",ivt.properties)
            tab_name = ivt.properties['name']
            print('Tab Name:', tab_name)
            self.tabs_dict['Inventories'][ivt_key] = {
                'name': tab_name,
                'content': ivt  #class Iventory
            }

    def table_builder(self, master, name, content):
        table_frame = ctk.CTkFrame(master)
        table_frame.grid_rowconfigure(0, weight=0)
        table_frame.grid_rowconfigure(1, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.pack(expand=True, fill='both')

        table_head = ctk.CTkFrame(table_frame)
        table_head.grid(row=0, column=0, sticky="ew")

        table = ctk.CTkScrollableFrame(table_frame)
        table.grid(row=1, column=0, sticky="nsew")

        fields = content.properties.get("fields", [])

        for col_index, col_name in enumerate(fields):
            header = ctk.CTkLabel(table_head, text=col_name, anchor="center")
            header.grid(row=0, column=col_index, padx=5, pady=5, sticky="nsew")
            table_head.grid_columnconfigure(col_index, weight=1)

        for row_index, item in enumerate(content.items):
            print(f"Item ID: {item.properties.get('id', 'Unknown')}")
            for col_index, col_name in enumerate(fields):
                value = item.properties.get(col_name, "")
                entry = ctk.CTkEntry(table)
                entry.insert(0, str(value))
                entry.grid(row=row_index, column=col_index, padx=2, pady=2, sticky="nsew")
                table.grid_columnconfigure(col_index, weight=1)

        return table_frame
