from constants import *
from tool import *

class LoadingScreen(tk.Frame):
    """游戏加载界面：一段加载动画"""
    def __init__(self, parent):
        super().__init__(parent)
        self.loading_label = tk.Label(self)
        self.loading_label.pack()
        self.loading_image = Image.open(loading_path )
        self.loading_photo = ImageTk.PhotoImage(self.loading_image)
        self.loading_label.config(image=self.loading_photo)
        def update_loading(i):
            if i < 103:
                self.loading_image.seek(i)
                self.loading_photo = ImageTk.PhotoImage(self.loading_image)
                self.loading_label.config(image=self.loading_photo)
                self.after(66, update_loading, i + 1)
            else:
                self.loading_label.config(image=tk.PhotoImage())
                self.update_idletasks()
                self.on_loading_complete()
        update_loading(0)
        self.pack()

    def on_loading_complete(self):
        """点击杂交实验室按钮的事件处理"""
        self.master.switch_to_screen('main_screen')
    
class MainScreen(tk.Frame):
    """原游戏主界面：包含一个“杂交实验室”按钮"""
    def __init__(self, parent):
        super().__init__(parent)
        self.mainmenu = create_background(self,image_path=mainscreen_path)
        self.menu_button = create_button(self,
                                         dark_image_path=menubutton1_path,
                                         light_image_path=menubutton2_path,
                                         width=133,
                                         height=106,
                                         locate_x=450,
                                         locate_y=478,
                                         command=self.on_breeding_button_click)
        self.pack()

    def on_breeding_button_click(self):
        # 点击杂交实验室按钮的事件处理
        self.master.switch_to_screen('breeding_screen')
    