import tkinter
import ttkbootstrap as ttk
import re

# Class defines the main theme
class Style:

    def __init__(self, style=None, root=None, *args):
        self.Theme = ttk.Style(theme=style)
        self.Text = tkinter.font.Font(family="Yuanti TC", name="appTextFont", size=12, weight="normal")
        self.Theme.configure("TButton", font=self.Text, fg="black")
        self.Theme.configure("TCheckbutton", font=self.Text, fg="black")
        self.Header = tkinter.font.Font(family="BM Hanna Pro", name="appHeaderFont", size=48, weight="bold")
        self.Error_Text = tkinter.font.Font(family="Yuanti TC Italic", name="appErrorTextFont", size=11, slant="italic")



# Class defines functions common in the UI
class Keybind:

    populate = {"username": "Ruby Rose",
                "email": 'RWBY@protonmail.com',
                "password": "WeissSchnee39"}

    # Deletes the preview text when user focuses an Entry Widget
    def Delete_Text(self, theme):
        if str(self.widget.cget("foreground")) == str(theme.colors.get("secondary")):
            self.widget.delete(0, "end")
            self.widget.configure(foreground="black")

    # Populates the preview text when user un-focuses an empty Entry widget
    def Populate_Text(self, text, key, theme):
        if text.get() == "":
            self.widget.insert(0, Keybind.populate[key])
            self.widget.configure(foreground=theme.colors.get("secondary"))

