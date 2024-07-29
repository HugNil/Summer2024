import customtkinter as ctk
from Logger import Logger
from Login_page import Login_page
from User import User
from Main_lib import Main_lib


class GUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.logger = Logger()
        self.user = User()

        num_rows = 12
        num_columns = 4

        # Configure rows and columns
        for i in range(num_rows):
            root.grid_rowconfigure(i, weight=1)  # Adjust weight as needed
        for j in range(num_columns):
            root.grid_columnconfigure(j, weight=1)

            self.create_pages()

    def create_pages(self):
        self.login_page = Login_page(self.root,
                                     self.logger,
                                     self.return_function,
                                     self.user
                                     )
        self.main_lib = Main_lib(self.root,
                                 self.logger,
                                 self.return_function,
                                 self.user
                                 )
        self.login_page.open()

    def clear_frame(self, frame_to_clear):
        frame_to_clear.clear()

    def return_function(self, last_page, next_page, user):
        exec(last_page)
        exec(next_page)

    def run_app():
        root = ctk.CTk()
        GUI(root)
        root.mainloop()


if __name__ == "__main__":
    GUI.run_app()
