import customtkinter as ctk
from tkinter import *
import modules.create_entry as m_entry
import modules.create_app as m_app
import modules.search_path as m_path
from PIL import Image, ImageDraw, ImageTk, ImageFilter, ImageFont
import modules.create_entry as m_entry
import modules.create_app as m_app
import modules.search_path as m_path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageTk
from PIL import ImageFilter
import requests
import os
import PIL




pelmen = 1
peremeni = 1

img = 0

width = 619
height = 401

def create_jpg():
    global label
    images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{pelmen}.jpg")), size = (width, height))
    label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                         image=images_path,
                         text="")
    label.place(x=0,y=200,anchor=ctk.W)
    
def create_png():
    global label
    images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{pelmen}.png")), size = (width, height))
    label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                             image=images_path,
                             text="")
    label.place(x=0,y=200,anchor=ctk.W)



def info_image():
    # global label_format
    # global label_width
    # global label_height
    # global label_mode
    try:
        img = Image.open(f"images/image{pelmen}.jpg")
        width = f"Width: {img.width}"
        height = f"Height: {img.height}"
        format = f"Format: {img.format}"
        mode = f"Mode: {img.mode}"

        label_width = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=width,)
        label_width.place(x = 21, y = 25, anchor = ctk.W)

        label_height = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=height)
        label_height.place(x = 21, y = 55, anchor = ctk.W)
        
        label_format = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=format)
        label_format.place(x = 21, y = 85, anchor = ctk.W)

        label_mode = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=mode)
        label_mode.place(x = 21, y = 115, anchor = ctk.W)

    except:
        img = Image.open(f"images/image{pelmen}.png")

        width = f"Width: {img.width}"
        height = f"Height: {img.height}"
        format = f"Format: {img.format}"
        mode = f"Mode: {img.mode}"
        #
        label_width = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=width)
        label_width.place(x = 21, y = 25, anchor = ctk.W)
        # 
        label_height = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=height)
        label_height.place(x = 21, y = 55, anchor = ctk.W)
        # 
        label_format = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=format)
        label_format.place(x = 21, y = 85, anchor = ctk.W)
        # 
        label_mode = ctk.CTkLabel(m_app.screen_app.FRAME_LIST_INFO,
                                 text=mode)
        label_mode.place(x = 21, y = 115, anchor = ctk.W)


list_name_image = []

   




def add_images():
    global peremeni
    global pelmen
    global img
    global list_name_image
    url = m_entry.text_address.get()
    try:
        req = requests.get(url,stream=True).raw
        img = Image.open(req)
    except:
        print("Прости, но эта ссылка не действительна")

    try:  
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        file_path = ctk.filedialog.askopenfilename(initialdir="images/", filetypes=(("JPEG files", "*.jpeg;*.jpg"),))
        file_path1 = os.path.splitext(os.path.basename(file_path))[0]
        list_name_image.append(file_path1)  
        create_jpg()
        info_image()
        (f"images/image{pelmen}.jpg")
        pelmen += 1
        peremeni = pelmen
    except:
        # pelmen += 1
        img.save(f"images/image{pelmen}.png", "png")
        file_path = ctk.filedialog.askopenfilename(initialdir="images/", filetypes=(("PNG files", "*.png"),))
        file_path1 = os.path.splitext(os.path.basename(file_path))[0]
        list_name_image.append(file_path1)
        create_png()
        info_image()
        (f"images/image{pelmen}.png")
        pelmen += 1
        peremeni = pelmen

    # rgba(255, 99, 71, 0)



    font = ctk.CTkFont(family="Sans",
                       size=15,
                       weight="bold",)
    
    box = Listbox(m_app.screen_app, font = font, bg = "purple", fg = "white")
    for  i in list_name_image:
        box.insert(END, i) 
    box.place(x = 20, y = 190, anchor = W)








# img = Image.open(f"images/image{pelmen}.jpg")  
canvas = ctk.CTkCanvas(m_app.screen_app.FRAME_IMAGE, 
                                   width=620, 
                                   height=400, 
                                   bg = "black")
            # Отображение изображения на холсте
canvas.data = {}

def start_drawing():
    global label
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(310, 200, anchor="c", image=photo) 
    canvas.data["image"] = photo
    # Расположение холста на окне
    canvas.place(x=0, y = 0)
    canvas.data["line_start"] = (0, 0)
    label.destroy()
    
def draw_stick(x, y):
    if "line_start" in canvas.data:
        start = canvas.data["line_start"]
        end = (x, y)
        canvas.create_line(start[0], start[1], end[0], end[1], fill="purple", width=5)
        canvas.data["line_start"] = end
# Привязка обработчиков событий рисования
canvas.bind("<Button-1>", lambda event: start_drawing())
canvas.bind("<B1-Motion>", lambda event: draw_stick(event.x, event.y))
canvas.bind("<ButtonRelease-1>", lambda event: canvas.data.pop("line_start", None))   


def cut_images():
    global pelmen
    global peremeni
    pelmen -= 1
    peremeni = pelmen
    try:
        img2 = Image.open(f"images/image{pelmen}.jpg")
        img2 = img2.crop((100, 75, 300, 150))
        img2.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img2 = Image.open(f"images/image{pelmen}.png")
        img2 = img2.crop((100, 75, 300, 150))
        img2.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
       
    pelmen += 1
    peremeni = pelmen

def rotate_right():
    global pelmen 
    global peremeni
    pelmen -=1
    peremeni = pelmen
    try:
        img = Image.open(f"images/image{pelmen}.png")
        img = img.rotate(90)
        img.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img = Image.open(f"images/image{pelmen}.jpg")
        img = img.rotate(90)
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        info_image()
    pelmen += 1
    peremeni = pelmen
    
def rotate_left():
    global peremeni
    global pelmen
    pelmen -= 1
    peremeni = pelmen
    try:
        img = Image.open(f"images/image{pelmen}.png")
        img = img.rotate(-90)
        img.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img = Image.open(f"images/image{pelmen}.jpg")
        img = img.rotate(-90)
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    pelmen += 1
    peremeni = pelmen
       











 



def filters_blur():
    global peremeni
    global pelmen
    pelmen -= 1
    peremeni = pelmen
    try:

        img = Image.open(f"images/image{pelmen}.jpg")
        img = img.filter(ImageFilter.BLUR)
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img = Image.open(f"images/image{pelmen}.png")
        img = img.filter(ImageFilter.BLUR)
        img.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    pelmen += 1
    peremeni = pelmen

def filters_detail():
    global peremeni
    global pelmen
    pelmen -= 1
    peremeni = pelmen
    try:

        img = Image.open(f"images/image{pelmen}.jpg")
        img = img.filter(ImageFilter.DETAIL)
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img = Image.open(f"images/image{pelmen}.png")
        img = img.filter(ImageFilter.DETAIL)
        img.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    pelmen += 1
    peremeni = pelmen
    
    
def black_white():
    global peremeni
    global pelmen
    pelmen -= 1
    peremeni = pelmen
    try:
        img = Image.open(f"images/image{pelmen}.jpg")
        img = img.convert("L")
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        img = Image.open(f"images/image{pelmen}.png")
        img = img.convert("L")
        img.save(f"images/image{pelmen}.png", 'png')
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    pelmen += 1
    peremeni = pelmen
    

def convert():
    global peremeni
    global pelmen
    global label
    pelmen -= 1
    peremeni = pelmen
    img = Image.open(f"images/image{pelmen}.jpg")
    img.save(f"images/image{pelmen}.png", 'png')
    os.remove(path= f"images/image{pelmen}.jpg")
    pelmen += 1
    peremeni = pelmen


def create_text():
    global peremeni
    global pelmen
    pelmen -= 1
    peremeni = pelmen
    try:
        text1 = m_entry.text_txt.get()
        img = Image.open(f"images/image{pelmen}.jpg")
        draw = ImageDraw.Draw(img)
        text = text1
        font = ImageFont.truetype("arial.ttf", size = 30)
        draw.text((50, 50), text, font = font)
        img.save(f"images/image{pelmen}.jpg", 'jpeg')
        m_entry.entry_txt.delete(0, ctk.END)
        create_jpg()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    except:
        text1 = m_entry.text_txt.get()
        img = Image.open(f"images/image{pelmen}.png")
        draw = ImageDraw.Draw(img)
        text = text1
        font = ImageFont.truetype("arial.ttf", size = 30)
        draw.text((50, 50), text, font = font)
        img.save(f"images/image{pelmen}.png", 'png')
        m_entry.entry_txt.delete(0, ctk.END)
        create_png()
        # label_mode.destroy()
        # label_height.destroy()
        # label_width.destroy()
        # label_format.destroy()
        info_image()
    
    pelmen += 1
    peremeni = pelmen


def change_size():
    global peremeni
    global height
    global width
    global pelmen
    global label
    global img
    pelmen -= 1
    peremeni = pelmen 
    try:
        height = int(m_entry.text_height.get())
      
        width = int(m_entry.text_width.get())
        
    except:
        print("Sorry but you need type number")  

    if height > 619 and width > 401 or height < 619 and width > 401 or height > 619 and width < 401: 
        print("no, you cant do this")
        height = 619
        width = 401
        try:
            label.destroy()
            img.save(f"images/image{pelmen}.png", 'png')
            # label.destroy()
            img = Image.open(f"images/image{pelmen}.png")
            info_image()
            # label_mode.destroy()
            # label_height.destroy()
            # label_width.destroy()
            # label_format.destroy()
            create_png()
            
        except:
            label.destroy()
            # m_app.screen_app.FRAME_IMAGE.destroy()
            img.save(f"images/image{pelmen}.jpg", 'jpeg')
            # label.destroy()
            img = Image.open(f"images/image{pelmen}.jpg")
            info_image()
            # label_mode.destroy()
            # label_height.destroy()
            # label_width.destroy()
            # label_format.destroy()
            create_jpg()
            # m_app.screen_app.FRAME_IMAGE.destroy()
            
            
    elif height <= 619 and width <= 401:
        print("Nice bro")
        try:
            print("Nice bro PNG")
            label.destroy()
            # m_app.screen_app.FRAME_IMAGE.destroy()
            img.save(f"images/image{pelmen}.png", 'png')
            # label.destroy()
            img = Image.open(f"images/image{pelmen}.png")
            info_image()
            # label_mode.destroy()
            # label_height.destroy()
            # label_width.destroy()
            # label_format.destroy()
            create_png()
            
        except:
            print("Nice bro JPG")
            label.destroy()
            # m_app.screen_app.FRAME_IMAGE.destroy()
            img.save(f"images/image{pelmen}.jpg", 'jpeg')
            # label.destroy()
            img = Image.open(f"images/image{pelmen}.jpg")
            info_image()
            # label_mode.destroy()
            # label_height.destroy()
            # label_width.destroy()
            # label_format.destroy()
            create_jpg()
            
    pelmen += 1 
    peremeni = pelmen
    

def next_image():
    global label
    global pelmen
    global peremeni
    peremeni += 1
    try:
        # label.destroy()
        if peremeni <= len(list_name_image):
            # label.destroy()
            images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{peremeni}.png")), size = (width, height))
            label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                                 image=images_path,
                                 text="")
            label.place(x=0,y=200,anchor=ctk.W)
        elif peremeni > len(list_name_image):
            peremeni = len(list_name_image)
            print("э куда лезешь там дорога нет")
        
    except:
        # label.destroy()
        if peremeni <= len(list_name_image):
            label.destroy()
            images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{peremeni}.jpg")), size = (width, height))
            label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                                 image=images_path,
                                 text="")
            label.place(x=0,y=200,anchor=ctk.W)
        elif peremeni > len(list_name_image):
            peremeni = len(list_name_image)
            print("э куда лезешь там дорога нет")
     
def past_image():
    global label
    global pelmen
    global peremeni
    peremeni -= 1
    try:
        if peremeni <= len(list_name_image):
            # label.destroy()
            images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{peremeni}.png")), size = (width, height))
            label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                                 image=images_path,
                                 text="")
            label.place(x=0,y=200,anchor=ctk.W)
  
            
        elif peremeni < len(list_name_image):
            peremeni = len(list_name_image)
            print("э куда лезешь там дорога нет")   
    except:
        if peremeni <= len(list_name_image):
        # label.destroy()
            images_path = ctk.CTkImage(dark_image=PIL.Image.open(m_path.path_search(f"images/image{peremeni}.jpg")), size = (width, height))
            label = ctk.CTkLabel(m_app.screen_app.FRAME_IMAGE,
                                 image=images_path,
                                 text="")
            label.place(x=0,y=200,anchor=ctk.W)
            
            
        elif peremeni < len(list_name_image):
            peremeni = len(list_name_image)
            print("э куда лезешь там дорога нет")
        