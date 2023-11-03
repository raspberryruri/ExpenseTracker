import ttkbootstrap.validation as validate
from Theme import *


class Entry(Style):

    def __init__(self, root, *args):

        # Inherits Default Theme
        super().__init__()

        # Class Attributes
        self.username = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.email_error_message = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.password_error_message = tkinter.StringVar()
        self.image = tkinter.PhotoImage(file="Graphics/1.png")
        self.root = root

    def Validate_Email(self, event):

        if event.postchangetext == "":
            self.email_error_message.set("")
            return True

        elif re.match("^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$", event.postchangetext):
            self.email_error_message.set("")
            return True

        else:
            self.email_error_message.set("Invalid Email Format")
            return False

    def Validate_Password(self, event):

        if event.postchangetext == "":
            self.password_error_message.set("")
            return True

        elif len(event.postchangetext) < 8:
            self.password_error_message.set("Password must contain at least 8 characters")
            return False

        elif re.search("[^a-zA-Z0-9_]", event.postchangetext) is not None:
            self.password_error_message.set("Password may only contain alphanumeric characters")
            return False

        elif re.search("[a-zA-Z]+", event.postchangetext) is None:
            self.password_error_message.set("Password must contain an alphabet")
            return False

        elif re.search("[0-9]+", event.postchangetext) is None:
            self.password_error_message.set("Password must contain a number")
            return False

        else:
            self.password_error_message.set("")
            return True

    def Start_Login(self, u, e, p, window):
        u.delete(0, "end")
        e.delete(0, "end")
        p.delete(0, "end")
        window.destroy()
        self.Login()

    def Start_Register(self, u, p, window):
        u.delete(0, "end")
        p.delete(0, "end")
        window.destroy()
        self.Register()

    def Register(self):

        # Creates TopLevel
        TopLevel = tkinter.Toplevel(self.root)
        TopLevel.title("Lunar")
        TopLevel.columnconfigure(0, weight=1)
        TopLevel.rowconfigure(0, weight=1)

        # Creates Main Frame
        mainframe = ttk.Label(TopLevel)
        mainframe.grid(column=0, row=0, sticky="nwes")
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1, minsize=400)
        mainframe.rowconfigure(0, weight=1)

        # Creates Left Frame
        lFrame = ttk.Label(mainframe)
        lFrame.grid(column=0, row=0, sticky="nwes")

        # Creates Right Frame
        rFrame = ttk.Label(mainframe)
        rFrame.grid(column=1, row=0, sticky="nwes")

        # Create Left Widgets
        # Image
        ttk.Label(lFrame, anchor="center", image=self.image).grid(column=1, row=3, sticky="nwes")

        # Welcome Label
        ttk.Label(lFrame, text="Welcome To Lunar!", font=self.Header, foreground="Black",
                  anchor="center").grid(column=1, row=1, sticky="swe")

        # Text
        text = tkinter.Text(lFrame, autostyle=0, bg="white", highlightthickness=0, height=4, wrap="word",
                            font=self.Text, fg="black")
        text.tag_configure('tag-center', justify='center')
        text.insert("1.0", "We have freshly baked cookies for new visitors! ;>", "tag-center")
        text["state"] = "disabled"
        text.grid(column=1, row=4, sticky="nwe")

        # Left Frame Resizing
        lFrame.columnconfigure(1, weight=1)
        lFrame.rowconfigure(1, weight=1)
        lFrame.rowconfigure(2, weight=1)
        lFrame.rowconfigure(3, weight=1)
        lFrame.rowconfigure(4, weight=1)
        lFrame.rowconfigure(5, weight=1)

        # Create Right Widgets
        # Get Started (Label)
        ttk.Label(rFrame, text="Get Started", font=self.Header, foreground="black", anchor="center").grid(
            column=1, row=2, sticky="we")

        # Already Have an account? Sign In! (Frame/Label/Button)
        SmallFrame = ttk.Frame(rFrame)
        SmallFrame.grid(column=1, row=3, sticky="nwes")
        SmallFrame.columnconfigure(1, weight=1)
        SmallFrame.columnconfigure(2, weight=1)
        SmallFrame.rowconfigure(3, weight=1)

        ttk.Label(SmallFrame, text="Already have an account?", font=self.Text, anchor="e").grid(column=1, row=3,
                                                                                                sticky="nes")
        ttk.Button(SmallFrame, text="Sign In", bootstyle="info-link",
                   command=lambda: self.Start_Login(u, e, p, TopLevel)).grid(column=2, row=3, sticky="nws")

        # Username (Frame)
        Username_Frame = ttk.Frame(rFrame)
        Username_Frame.grid(column=1, row=4, sticky="nwes", padx=25)
        Username_Frame.columnconfigure(1, weight=1)
        Username_Frame.rowconfigure(1, weight=1)
        Username_Frame.rowconfigure(2, weight=0)
        Username_Frame.rowconfigure(3, weight=0)

        # Username (Label)
        ttk.Label(Username_Frame, text="Username", font=self.Text).grid(column=1, row=1, sticky="swe")

        # Username Box (Entry)
        u = ttk.Entry(Username_Frame, textvariable=self.username, font=self.Text,
                      foreground=self.Theme.colors.get("secondary"), bootstyle="success")
        u.insert(0, "Ruby Rose")
        u.grid(column=1, row=2, sticky="nwe")
        u.bind("<FocusIn>", lambda event, x=self.Theme: Keybind.Delete_Text(event, x))
        u.bind("<FocusOut>",
               lambda event, x=self.username, y="username", z=self.Theme: Keybind.Populate_Text(event, x, y, z))
        u.bind("<Return>", lambda event: e.focus())

        # Email (Frame)
        Email_Frame = ttk.Frame(rFrame)
        Email_Frame.grid(column=1, row=5, sticky="nwes", padx=25)
        Email_Frame.columnconfigure(1, weight=1)
        Email_Frame.rowconfigure(1, weight=1)
        Email_Frame.rowconfigure(2, weight=0)
        Email_Frame.rowconfigure(3, weight=0)

        # Email (Label)
        ttk.Label(Email_Frame, text="Email", font=self.Text).grid(column=1, row=1, sticky="swe")

        # Email Box (Entry)
        e = ttk.Entry(Email_Frame, textvariable=self.email, font=self.Text,
                      foreground=self.Theme.colors.get("secondary"), bootstyle="success")
        validate.add_validation(e, validate.validator(self.Validate_Email))
        e.insert(0, 'RWBY@protonmail.com')
        e.grid(column=1, row=2, sticky="nwe")
        e.bind("<FocusIn>", lambda event, x=self.Theme: Keybind.Delete_Text(event, x))
        e.bind("<FocusOut>",
               lambda event, x=self.email, y="email", z=self.Theme: Keybind.Populate_Text(event, x, y, z))
        e.bind("<Return>", lambda event: p.focus())

        # Email Error Message (Label)
        ttk.Label(Email_Frame, textvariable=self.email_error_message, font=self.Error_Text,
                  foreground=self.Theme.colors.get("danger")).grid(column=1, row=3, sticky="nwe")

        # Password (Frame)
        Password_Frame = ttk.Frame(rFrame)
        Password_Frame.grid(column=1, row=6, sticky="nwes", padx=25)
        Password_Frame.columnconfigure(1, weight=1)
        Password_Frame.rowconfigure(1, weight=1)
        Password_Frame.rowconfigure(2, weight=0)
        Password_Frame.rowconfigure(3, weight=1)

        # Password (Label)
        ttk.Label(Password_Frame, text="Password", font=self.Text).grid(column=1, row=1, sticky="swe")

        # Password Box (Entry)
        p = ttk.Entry(Password_Frame, textvariable=self.password, font=self.Text, show="*", bootstyle="success",
                      foreground=self.Theme.colors.get(
                          "secondary"))  # , validate="focus", validatecommand=self.Validate_Password())
        validate.add_validation(p, validate.validator(self.Validate_Password))
        p.grid(column=1, row=2, sticky="nwe")
        p.insert(0, "WeissSchnee39")
        p.bind("<FocusIn>", lambda event, z=self.Theme: Keybind.Delete_Text(event, z))
        p.bind("<FocusOut>",
               lambda event, x=self.password, y="password", z=self.Theme: Keybind.Populate_Text(event, x, y, z))

        # Password Error Message (Label)
        ttk.Label(Password_Frame, textvariable=self.password_error_message, font=self.Error_Text,
                  foreground=self.Theme.colors.get("danger")).grid(column=1, row=3, sticky="nwe")

        # Privacy Policy
        ttk.Checkbutton(rFrame, text="I agree to the terms and conditions", bootstyle="light").grid(column=1,
                                                                                                         row=7,
                                                                                                         sticky="we",
                                                                                                         padx=25)

        # Sign Up Button
        ttk.Button(rFrame, text="Sign Up", bootstyle="success").grid(column=1, row=8, sticky="we", padx=100)



        # Right Frame Resizing
        rFrame.columnconfigure(1, weight=1)
        rFrame.rowconfigure(1, weight=3)
        rFrame.rowconfigure(2, weight=1)
        rFrame.rowconfigure(3, weight=0)
        rFrame.rowconfigure(4, weight=1)
        rFrame.rowconfigure(5, weight=1)
        rFrame.rowconfigure(6, weight=1)
        rFrame.rowconfigure(7, weight=0)
        rFrame.rowconfigure(8, weight=1)
        rFrame.rowconfigure(9, weight=1)
        rFrame.rowconfigure(15, weight=3)


    def Login(self):

        # Creates TopLevel
        TopLevel = tkinter.Toplevel(self.root)
        TopLevel.title("Lunar")
        TopLevel.columnconfigure(0, weight=1)
        TopLevel.rowconfigure(0, weight=1)

        # Creates Main Frame
        mainframe = ttk.Label(TopLevel)
        mainframe.grid(column=0, row=0, sticky="nwes")
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1, minsize=400)
        mainframe.rowconfigure(0, weight=1)

        # Creates Left Frame
        lFrame = ttk.Label(mainframe)
        lFrame.grid(column=0, row=0, sticky="nwes")

        # Creates Right Frame
        rFrame = ttk.Label(mainframe)
        rFrame.grid(column=1, row=0, sticky="nwes")

        # Create Left Widgets
        # Image
        ttk.Label(lFrame, image=self.image, anchor="center").grid(column=1, row=3, sticky="nwes")

        # Welcome Label
        ttk.Label(lFrame, text="Welcome Back!", font=self.Header, foreground="Black", anchor="center").grid(column=1, row=1, sticky="swe")

        # Text
        text = tkinter.Text(lFrame, autostyle=0, bg="white", highlightthickness=0, height=4, wrap="word", font=self.Text, fg="black")
        text.tag_configure('tag-center', justify='center')
        text.insert("1.0", "Gimme a break. Christ on a pogo stick, somebody just shoot me, please!", "tag-center")
        text["state"] = "disabled"
        text.grid(column=1, row=4, sticky="nwe")

        # Left Frame Resizing
        lFrame.columnconfigure(1, weight=1)
        lFrame.rowconfigure(1, weight=3)
        lFrame.rowconfigure(2, weight=1)
        lFrame.rowconfigure(3, weight=1)
        lFrame.rowconfigure(4, weight=1)
        lFrame.rowconfigure(5, weight=1)


        # Create Right Widgets
        # Sign In (Label)
        ttk.Label(rFrame, text="Sign In", font=self.Header, foreground="black", anchor="center").grid(column=1, row=2, sticky="we")

        # First Time Around Here? Sign up! (Frame/Label/Button)
        SmallFrame = ttk.Frame(rFrame)
        SmallFrame.grid(column=1, row=3, sticky="nwes")
        SmallFrame.columnconfigure(1, weight=1)
        SmallFrame.columnconfigure(2, weight=1)
        SmallFrame.rowconfigure(3, weight=1)

        ttk.Label(SmallFrame, text="First time around here?", font=self.Text, anchor="e").grid(column=1, row=3, sticky="nes")
        ttk.Button(SmallFrame, text="Sign Up", bootstyle="info-link", command=lambda: self.Start_Register(u, p, TopLevel)).grid(column=2, row=3, sticky="nws")

        # Username (Frame)
        Username_Frame = ttk.Frame(rFrame)
        Username_Frame.grid(column=1, row=4, sticky="nwes", padx=25)
        Username_Frame.columnconfigure(1, weight=1)
        Username_Frame.rowconfigure(1, weight=1)
        Username_Frame.rowconfigure(2, weight=0)
        Username_Frame.rowconfigure(3, weight=0)

        # Username/Email (Label)
        ttk.Label(Username_Frame, text="Username/Email Address", font=self.Text).grid(column=1, row=1, sticky="swe")

        # Username/Email Box (Entry)
        u = ttk.Entry(Username_Frame, textvariable=self.username, font=self.Text, foreground=self.Theme.colors.get("secondary"), bootstyle="success")
        u.insert(0, "Ruby Rose")
        u.grid(column=1, row=2, sticky="nwe")
        u.bind("<FocusIn>", lambda event, x=self.Theme: Keybind.Delete_Text(event, x))
        u.bind("<FocusOut>", lambda event, x=self.username, y="username", z=self.Theme: Keybind.Populate_Text(event, x, y, z))
        u.bind("<Return>", lambda event: p.focus())

        # Password (Frame)
        Password_Frame = ttk.Frame(rFrame)
        Password_Frame.grid(column=1, row=6, sticky="nwes", padx=25)
        Password_Frame.columnconfigure(1, weight=1)
        Password_Frame.rowconfigure(1, weight=1)
        Password_Frame.rowconfigure(2, weight=0)
        Password_Frame.rowconfigure(3, weight=1)

        # Password (Label)
        ttk.Label(Password_Frame, text="Password", font=self.Text).grid(column=1, row=1, sticky="swe")

        # Password Box (Entry)
        p = ttk.Entry(Password_Frame, textvariable=self.password, font=self.Text, show="*", bootstyle="success", foreground=self.Theme.colors.get("secondary")) #, validate="focus", validatecommand=self.Validate_Password())
        validate.add_validation(p, validate.validator(self.Validate_Password))
        p.grid(column=1, row=2, sticky="nwe")
        p.insert(0, "WeissSchnee39")
        p.bind("<FocusIn>", lambda event, z=self.Theme: Keybind.Delete_Text(event, z))
        p.bind("<FocusOut>", lambda event, x=self.password, y="password", z=self.Theme: Keybind.Populate_Text(event, x, y, z))

        # Password Error Message (Label)
        ttk.Label(Password_Frame, textvariable=self.password_error_message, font=self.Error_Text,
                  foreground=self.Theme.colors.get("danger")).grid(column=1, row=3, sticky="nwe")

        # Privacy Policy
        ttk.Checkbutton(rFrame, text="I agree to the terms and conditions", bootstyle="light").grid(column=1, row=7, sticky="we", padx=25)

        # Sign Up Button
        ttk.Button(rFrame, text="Sign Up", bootstyle="success").grid(column=1, row=8, sticky="we", padx=100)

        # Right Frame Resizing
        rFrame.columnconfigure(1, weight=1)
        rFrame.rowconfigure(1, weight=3)
        rFrame.rowconfigure(2, weight=1)
        rFrame.rowconfigure(3, weight=0)
        rFrame.rowconfigure(4, weight=1)
        rFrame.rowconfigure(5, weight=1)
        rFrame.rowconfigure(6, weight=1)
        rFrame.rowconfigure(7, weight=0)
        rFrame.rowconfigure(8, weight=1)
        rFrame.rowconfigure(9, weight=1)
        rFrame.rowconfigure(15, weight=3)





