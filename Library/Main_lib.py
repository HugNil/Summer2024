import customtkinter as ctk


class Main_lib:
    def __init__(self, root, logclass, return_function, user):
        self.root = root
        self.logclass = logclass
        self.return_function = return_function
        self.user = user

        self.create_frames()

    def create_frames(self):
        self.main_lib_frame = ctk.CTkFrame(
            master=self.root,
            fg_color='black'
        )
        self.main_lib_frame.configure(
            width=500,
            height=300
        )

    def clear(self):
        self.main_lib_frame.pack_forget()

    def open(self):
        self.main_lib_frame_open()

    def main_lib_frame_open(self):
        self.main_lib_frame.pack(
            fill=ctk.BOTH,
            expand=True
        )
