import customtkinter as ctk
import tkinter as tk
import modules.functions_buttons as m_func
import modules.search_path as m_path
import modules.create_app as c_app
import PIL

        
class Button(ctk.CTkButton):
    def __init__ (self, master, height, command, width, text, fg_color, image):
        super().__init__(master=master,
                         width=width,
                         height=height,
                         text=text,
                         command=command,
                         corner_radius = 0,
                         fg_color=fg_color,
                         image=image)
        
# Я деловая колбаса
# Я так устал
# Я поработал полчаса (два часа)


# Кнопка для открытия окна с палитрой для кисти(карандаша)

# window = Button(master=c_app.screen_app,
#                   width=90,
#                   height=35,
#                   text="",
#                   fg_color="purple",
#                   command=m_func.window,
#                   image = image)

# button_download.place(x = 610,y = 7.5, anchor = ctk.W)

#Тут будет окно с палитрой и размером кисти(карандаша)

# window = App(app_height = 400
#         app_width = 200
#         geometry("850x500"))



button_download = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  fg_color="purple",
                  command=m_func.add_images,
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/download.png")), size = (35, 35))
                  )

button_download.place(x = 20, y = 470.75, anchor = ctk.W)


button_shear = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.cut_images,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/scissors.png")), size = (30, 35)))

button_shear.place(x = 130, y = 470.75, anchor = ctk.W)


button_rotate_right = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.rotate_right,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/rotateright.png")), size =(35, 35)))

button_rotate_right.place(x = 740, y = 470.75, anchor = ctk.W)

button_rotate_left = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.rotate_left,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/rotateleft.png")), size =(35, 35)))

button_rotate_left.place(x = 630, y = 470.75, anchor = ctk.W)

button_draw_pictures = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.start_drawing,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/draw.png")), size =(35, 35)))
button_draw_pictures.place(x = 460, y = 470.75, anchor = ctk.W)

# button_back_pictures.bind("<")

button_convert = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.convert,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/convert.png")), size =(35, 35)))
button_convert.place(x = 350, y = 470.75, anchor = ctk.W)


# 


button_create_text = Button(master=c_app.screen_app,
                  width=30,
                  height=25,
                  text="",
                  command=m_func.create_text,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/text.png")), size =(20, 15)))
button_create_text.place(x = 610, y = 22.5, anchor = ctk.W)


button_change_size = Button(master=c_app.screen_app,
                  width=30,
                  height=25,
                  text="",
                  command=m_func.change_size,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/size.png")), size =(20, 15)))
button_change_size.place(x = 140, y = 7.5)





# create button for frame


# create button for frame

button_next_pictures = Button(master=c_app.screen_app,

                  width=50,
                  height=25,
                  text="",
                  command=m_func.next_image,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/right.png")), size =(25, 12.5)))

button_next_pictures.place(x = 540, y = 415, anchor = ctk.CENTER)


button_back_pictures = Button(master=c_app.screen_app,

                  width=50,
                  height=25,
                  text="",
                  command=m_func.past_image,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/left.png")), size =(25, 12.5)))

button_back_pictures.place(x = 480, y = 415, anchor = ctk.CENTER)



# 
button_blur_pictures = Button(master=c_app.screen_app,
                  width=40,
                  height=15,
                  text="",
                  command=m_func.filters_blur,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/filter_minus.png")), size =(15, 15)))

button_blur_pictures.place(x = 590, y = 480, anchor = ctk.CENTER)



# 
button_detail_pictures = Button(master=c_app.screen_app,
                  width=40,
                  height=15,
                  text="",
                  command=m_func.filters_detail,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/filter_plus.png")), size =(15, 15)))

button_detail_pictures.place(x = 590, y = 460, anchor = ctk.CENTER)


# 
button_black_white = Button(master=c_app.screen_app,
                  width=90,
                  height=35,
                  text="",
                  command=m_func.black_white,
                  fg_color="purple",
                  image = ctk.CTkImage(dark_image= PIL.Image.open(m_path.path_search("image/black_white.png")), size =(35, 35)))

button_black_white.place(x = 240, y = 470.75, anchor = ctk.W)

