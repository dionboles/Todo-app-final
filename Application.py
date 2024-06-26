import tkinter as tk
from TodoListScreen import ToDoList
from LoginScreen import LoginScreen
from ttkbootstrap import Style

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.style = Style(theme='cosmo')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.passFrame = None
        self.create_frames()

    def create_frames(self):
            for Page in (LoginScreen, ToDoList):
                page_name = Page.__name__
                frame = Page(parent=self, controller=self)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(LoginScreen)

         
    def show_frame(self, frame_class):
            frame_name = frame_class.__name__
            
            if self.passFrame is not None:
                if frame_name != self.passFrame:
                    old_frame = self.frames[self.passFrame]
                    old_frame.pack_propagate(False)
                    new_frame = frame_class(parent=self, controller=self)
                    self.frames[frame_name] = new_frame
                    new_frame.grid(row=0, column=0, sticky="nsew")
                    new_frame.pack_propagate(False)
                    new_frame.tkraise()
                    self.passFrame = frame_name
            else:
                self.passFrame = frame_name
                frame = self.frames[frame_name]
                frame.tkraise()