import tkinter as tk

def example():
    # 创建窗口
    root = tk.Tk()
    # 创建按钮
    button = tk.Button(root, text="小老弟来喽！")
    button.pack()  # 添加组件
    # 创建文本
    label = tk.Label(root, text="欢迎使用 Tkinter!")
    label.pack()    # 添加组件
    # 创建输入框
    entry = tk.Entry(root)
    entry.pack()    # 添加组件

    root.mainloop() # 启动事件循环

def window_example(root):
    root.title("Tkinter Tutorial")
    root.configure(bg="black")
    root.geometry("400x300")

def pack_example(root):
    button1 = tk.Button(root, text="Button 1")
    button1.pack(side=tk.LEFT)

    button2 = tk.Button(root, text="Button 2")
    button2.pack(side=tk.LEFT)

    button3 = tk.Button(root, text="Button 3")
    button3.pack(side=tk.LEFT)

def grid_example(root):
    button1 = tk.Button(root, text="Button 1")
    button1.grid(row=0, column=0)

    button2 = tk.Button(root, text="Button 2")
    button2.grid(row=0, column=1)

    button3 = tk.Button(root, text="Button 3")
    button3.grid(row=1, column=0)

def place_example(root):
    button1 = tk.Button(root, text="Button 1")
    button1.place(x=50, y=50)

    button2 = tk.Button(root, text="Button 2")
    button2.place(x=100, y=100)

def event_example(root):
    def on_button_click(event):
        print("Button clicked!")

    button1 = tk.Button(root, text="Button 1")
    button1.bind("<Button-1>", on_button_click)
    button1.pack()

def font_example(root):
    label = tk.Label(root, text="欢迎使用 Tkinter!", font=("Arial", 14, "bold"), fg="blue")
    label.pack()

def image_example(root):
    # 加载图片
    from PIL import Image, ImageTk
    img = Image.open(r"图片\transformer.png")
    img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img)
    label.image = img  # 保持引用，防止垃圾回收
    label.pack()

def menu_example(root):
    # 创建菜单栏
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # 创建文件菜单
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="文件", menu=file_menu)

    # 添加菜单项到文件菜单
    file_menu.add_command(label="打开", command=lambda: print("打开文件"))
    file_menu.add_command(label="保存", command=lambda: print("保存文件"))
    file_menu.add_separator()  # 添加分隔线
    file_menu.add_command(label="退出", command=root.quit)

    # 创建帮助菜单
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="帮助", menu=help_menu)

    # 添加菜单项到帮助菜单
    help_menu.add_command(label="关于", command=lambda: print("关于信息"))


if __name__=="__main__":
    #example()    
    root = tk.Tk()
    window_example(root)
    #pack_example(root)
    #grid_example(root)
    #place_example(root)
    #event_example(root)
    #font_example(root)
    #image_example(root)
    #menu_example(root)
    root.mainloop()
