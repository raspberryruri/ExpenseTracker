# Import Tkinter & ttkbootstrap
import tkinter

from Entry_UI import *
#Size=925x500 maybe

root = tkinter.Tk()
root.withdraw()

Style(style="flatly")
entry = Entry(root)
Entry.Register(entry)


root.mainloop()

'''
Theme File 
 • Class for storing theme/style information
 • Class for password validation/password hashing
 
Entry UI File
 • Class for the Login UI
 • Class for the Register UI
 
Dashboard UI File
 • Class for the Main Dashboard UI
 • 4 Classes inheriting the Main UI Class for each tab
 • Additional Classes for different Pop-Up Tabs?
 • Class for handling the database
 
Database File
 • Class for checking login/register information
 • Classes for handling user inputs in the main dashboard
 • Anything extra needed for the database
 
main.py
'''
