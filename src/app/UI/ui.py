from .menu import global_menu
from .content import main_app
import customtkinter as ctk
from PIL import ImageTk
import app.settings.settings as s

class window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.load_settings()
        self.iconpath = ImageTk.PhotoImage(file="./app/UI/assets/icons/icon40x40.png")
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)
        
        self.title("inventore It!")
        self.geometry("800x500")

# Can't remember why I put grids weights here, maybe so the
# dependant frames can take the whole place in the window...
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        global_menu(self)

        self.main_frame = main_app(master=self)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        self.listen(lambda: s.db_instance,self.main_frame.display)
    def load_settings(self):
        pass
        
    def listen(self, boolean_func, callback):
        self._last_state = None

        def check():
            current_state = boolean_func()
            if current_state != self._last_state:
                self._last_state = current_state
                callback()
            self.after(100, check)

        check()



