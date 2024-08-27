import tkinter as tk
from PIL import Image, ImageTk
from Day2 import *

def label_button(root):
    # 加载图片
    dark_image = tk.PhotoImage(file="images\CloseButton.png")  # 替换为你的暗图片路径
    light_image = tk.PhotoImage(file="images\CloseButtonHighlight.png")  # 替换为你的亮图片路径

    def on_enter(event):
        """鼠标进入Label时调用的函数"""
        label.config(image=light_image)

    def on_leave(event):
        """鼠标离开Label时调用的函数"""
        label.config(image=dark_image)

    def on_click(event):
        """Label被点击时调用的函数"""
        messagebox.showinfo("点击了！", "按钮被点击了")

    # 创建Label作为按钮
    label = tk.Label(root, image=dark_image, cursor="hand2",bg='Blue')
    label.pack(pady=20)

    # 绑定鼠标事件
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<Button-1>", on_click)  # 绑定鼠标左键点击事件

def canvas_button(root,width,height):
    def on_button_click(event):
        tk.messagebox.showinfo("按钮点击", "按钮被点击了")

    def on_hover(event):
        canvas.itemconfig(label, fill="white")
        canvas.itemconfig(button, fill="black")
        canvas.update_idletasks()

    def on_leave(event):
        canvas.itemconfig(label, fill="black")
        canvas.itemconfig(button, fill="white")
        canvas.update_idletasks()

    # 创建画布
    canvas = tk.Canvas(root, width=width, height=height, bg="white",bd=0)
    canvas.pack()

    # 加载图片
    img = Image.open("images\Almanac_ZombieBack.jpg")
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img) 
    canvas.create_image(width//2, height//2, image=photo)
    canvas.photo = photo

    # 创建透明按钮
    button_width = 100
    button_height = 50
    button_x = 390
    button_y = 500

    # 创建按钮，设置透明背景和文字
    # 按钮可以为任意形状，只要设置width为0，不填充颜色，就可以做到透明
    button = canvas.create_rectangle(button_x, button_y, button_x + button_width, button_y + button_height,
                                     width=1,
                                     outline="red",
                                     fill="white"
                                     )
    label = canvas.create_text(button_x + button_width // 2, 
                               button_y + button_height // 2, 
                               text="点击我", fill="black", font=("Arial", 16))

    # 鼠标悬停和离开事件处理
    canvas.tag_bind(label, "<Enter>", on_hover)
    canvas.tag_bind(button, "<Enter>", on_hover)
    canvas.tag_bind(label, "<Leave>", on_leave)
    canvas.tag_bind(button, "<Leave>", on_leave)

    # 点击按钮事件处理
    canvas.tag_bind(button, "<Button-1>", on_button_click)
    canvas.tag_bind(label, "<Button-1>", on_button_click)

if __name__=="__main__":
    root = tk.Tk()
    window_width = 880
    window_height = 600
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='lightBlue')  # 设置窗口背景颜色为红色

    label_button(root)
    #canvas_button(root,window_width,window_height)
    root.mainloop()