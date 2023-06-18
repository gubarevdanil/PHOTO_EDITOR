import customtkinter as ctk
import modules.create_app as m_app

font = ctk.CTkFont(family="Sans",
                   size=15,
                   weight="bold")


text_address = ctk.StringVar()

entry_url_address = ctk.CTkEntry(master=m_app.screen_app,
                     width=170,
                     height=40,
                     corner_radius = 15,
                     fg_color="purple",
                     text_color="white",
                     font=font,
                     textvariable=text_address)

entry_url_address.place(x = 20,y = 40)

#2

text_txt = ctk.StringVar()

entry_txt = ctk.CTkEntry(master=m_app.screen_app,
                     width=200,
                     height=30,
                     corner_radius = 15,
                     fg_color="purple",
                     text_color="white",
                     font=font,
                     textvariable=text_txt)

entry_txt.place(x=400, y=7.5)



# 3
text_width = ctk.StringVar()
entry_width = ctk.CTkEntry(master=m_app.screen_app,
                     width=50,
                     height=25,
                     corner_radius = 15,
                     fg_color="purple",
                     text_color="white",
                     font=font,
                     textvariable=text_width)

entry_width.place(x = 20,y = 7.5)

text_height = ctk.StringVar()
entry_height = ctk.CTkEntry(master=m_app.screen_app,
                     width=50,
                     height=25,
                     corner_radius = 15,
                     fg_color="purple",
                     text_color="white",
                     font=font,
                     textvariable=text_height)

entry_height.place(x = 80,y = 7.5)
