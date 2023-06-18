from customtkinter import *
from tkinter import * 
import modules.create_app as m_app
import modules.functions_buttons as fb
# from modules.functions_buttons import list_name_image

font = CTkFont(family="Sans",
                   size=15,
                   weight="bold")

box = Listbox(m_app.screen_app, font = font, bg = "purple", fg = "white", width = 20, height = 10)
box.place(x = 20, y = 190, anchor = W)
box.insert(END, '') 