import customtkinter as ctk
import modules.search_path as m_path
#import PIL

app_width = 850
app_height = 500

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.wm_iconbitmap("image/photo.ico")
        self.APP_HEIGHT = app_height
        self.APP_WIDTH = app_width
        self.geometry("850x500")
        self.title("Photoshop 17 pro max ultra hd 4k 1337 fps and 228 hz")
        self.resizable(False, False)
        self.FRAME_IMAGE = ctk.CTkFrame(
            width = 620, 
            height = 400, 
            master = self,
            fg_color= "black",
            corner_radius = 15)
        self.FRAME_IMAGE.place(x = 210, y = 245, anchor = ctk.W)


        self.FRAME_LIST_INFO = ctk.CTkFrame(
            width = 170, 
            height = 140, 
            master = self,
            fg_color= "purple",
            corner_radius = 15)

        self.FRAME_LIST_INFO.place(x = 20, y = 370, anchor = ctk.W)

        # self.FRAME_LIST_IMAGE = ctk.CTkFrame(
            # width = 173, 
            # height = 208, 
            # master = self, 
            # corner_radius = 15, 
            # border_width = 3)
# 
        # self.FRAME_LIST_IMAGE.place(x = 20, y = 190, anchor = ctk.W)


screen_app = App(app_width, app_height)


