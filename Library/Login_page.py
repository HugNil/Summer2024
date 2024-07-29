import customtkinter as ctk


class Login_page:
    def __init__(self, root, logclass, return_function, user):
        self.root = root
        self.logclass = logclass
        self.return_function = return_function
        self.user = user

        self.create_frames()

    def create_frames(self):
        self.login_frame = ctk.CTkFrame(
            master=self.root,
            fg_color='black'
        )
        self.login_frame.configure(
            width=500,
            height=300
        )

    def clear(self):
        self.login_frame.pack_forget()

    def open(self):
        self.login_frame_open()

    def login_frame_open(self):
        self.login_frame.pack(
            fill=ctk.BOTH,
            expand=True
        )
        username_entry = ctk.CTkEntry(
            master=self.login_frame,
            fg_color='black',
            bg_color='white',
            font=('Arial', 12),
            width=200,
            height=30,
            placeholder_text='Username'
        )
        username_entry.grid(
            row=1,
            column=4
        )

        password_entry = ctk.CTkEntry(
            master=self.login_frame,
            fg_color='black',
            bg_color='white',
            font=('Arial', 12),
            width=200,
            height=30,
            show='*',
            placeholder_text='Password'
        )
        password_entry.grid(
            row=1,
            column=6,
        )

        login_button = ctk.CTkButton(
            master=self.login_frame,
            text='Login',
            command=lambda: self.login_button_clicked(
                username_entry.get(),
                password_entry.get()
            ),
            width=100,
            height=30
        )
        login_button.grid(
            row=1,
            column=8
        )

    def login_button_clicked(self, username, password):
        if username == 'admin' and password == 'admin':
            self.logclass.log('Admin Login successful')
            self.return_function('self.login_page.clear()',
                                 'self.main_lib.open()',
                                 self.user)
        else:
            self.logclass.log('Login failed')
            self.root.destroy()
