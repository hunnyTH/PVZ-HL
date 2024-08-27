import tkinter as tk
from tkinter import messagebox

def title_and_icon(root):
    root.title("小老弟来喽")  # 窗口标题
    root.iconbitmap(r"图片\icon.ico")  # 设置窗口图标
def window_size(root,window_width,window_height):
    root.geometry(f"{window_width}x{window_height}")  
    #root.configure(width=window_width,height=window_height)
    #root.config(width=window_width,height=window_height)

    root.resizable(width=False, height=False)  # 禁止调整窗口大小，优先级高于下面两个
    #root.minsize(200, 200)  # 设置窗口最小尺寸为 200x200
    #root.maxsize(600, 400)  # 设置窗口最大尺寸为 600x400  
def window_location(root,window_width,window_height):
    """
    root.geometry('+100+100')  # 窗体在屏幕左上角
    root.geometry('-100-100')  # 窗体在屏幕右下角
    root.geometry('+100-100')  # 窗体在屏幕左下角
    root.geometry('-100+100')  # 窗体在屏幕右上角
    """
    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口的位置
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    # 设置窗口位置
    root.geometry(f'+{x}+{y}')    
def bind_example(root):
    def on_key_press(event):
    # 当用户按下键盘上的任意键时调用
        print(f"您按下了: {event.char}")

    def on_click(event):
        # 当用户点击窗口时调用
        print(f"鼠标点击位置: x={event.x}, y={event.y}")

    # 绑定键盘按键事件
    root.bind('<Key>', on_key_press)

    # 绑定鼠标点击事件
    root.bind('<Button-1>', on_click)
def close(root):
    def on_close():
        if messagebox.askokcancel("退出", "你确定要退出吗？"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)  # 绑定关闭窗口事件

def Tk_function():
    root = tk.Tk()
    # 设置窗口大小为 400x300
    window_width = 400
    window_height = 300
    root.configure(bg='lightblue')  # 设置窗口背景颜色为浅绿色

    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    bind_example(root)
    close(root)
    root.mainloop()

def pack_test(window_width=1600,window_height=1200):
    # 创建主窗口
    root = tk.Tk()
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='red')  # 设置窗口背景颜色为红色

    # 创建标签
    label1 = tk.Label(root, text="这是第一个标签",bg="yellow")
    label1.pack(side=tk.TOP, fill=tk.X, expand=True)

    # 创建按钮
    button1 = tk.Button(root, text="这是第一个按钮",bg="blue")
    button1.pack(side=tk.LEFT, fill=tk.Y, expand=True)

    # 创建另一个标签
    label2 = tk.Label(root, text="这是第二个标签", bg="yellow")
    label2.pack(side=tk.TOP, fill=tk.NONE, expand=True)

    # 创建另一个按钮
    button2 = tk.Button(root, text="这是第二个按钮",bg="blue")
    button2.pack(side=tk.LEFT, fill=tk.NONE, expand=True)

    # 创建输入框
    entry = tk.Entry(root,bg="pink")
    entry.pack(side=tk.LEFT, fill=tk.Y, expand=True)

    # 创建滚动条
    scrollbar = tk.Scrollbar(root,bg="green")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # 创建文本框
    text = tk.Text(root,bg="black")
    text.pack(side=tk.LEFT, fill=tk.Y, expand=True)

    # 运行主循环
    root.mainloop()

def pack_example(window_width=400,window_height=300):
    # 创建主窗口
    root = tk.Tk()
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='red')  # 设置窗口背景颜色为红色

    # 创建三个按钮组件
    button1 = tk.Button(root, text="Button 1")
    button2 = tk.Button(root, text="Button 2")
    button3 = tk.Button(root, text="Button 3")

    # 使用 pack 布局管理器并设置间隙
    button1.pack(anchor=tk.NW,padx=10, pady=10,ipadx=10, ipady=10)  # 设置按钮1的水平和垂直外部填充
    button2.pack(anchor=tk.CENTER,padx=20, pady=20,ipadx=10, ipady=20)  # 设置按钮2的水平和垂直外部填充
    button3.pack(anchor=tk.SE,padx=10, pady=10,ipadx=10, ipady=10)  # 设置按钮3的水平和垂直外部填充

    # 启动事件循环
    root.mainloop()

def grid_test(window_width=800,window_height=600):
    root = tk.Tk()
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='red')  # 设置窗口背景颜色为红色

    # 创建组件
    label1 = tk.Label(root, text="Label 1", bg="yellow")
    label2 = tk.Label(root, text="Label 2", bg="pink")
    label3 = tk.Label(root, text="Label 3", bg="green")
    button1 = tk.Button(root, text="Button 1")
    button2 = tk.Button(root, text="Button 2")
    input_field = tk.Entry(root)

    # 使用grid布局管理器放置组件
    label1.grid(row=0, column=0,sticky="N")
    label2.grid(row=0, column=1,sticky="E")
    label3.grid(row=1, column=0, columnspan=2,sticky="NW")  # 跨越两列
    button1.grid(row=2, column=0,sticky="NE")
    #button2.grid(row=2, column=1,sticky="NSEW")
    button2.grid(row=2, column=1,sticky="NE")
    input_field.grid(row=3, column=0, columnspan=2,sticky="NSEW")  # 跨越两列

    # 运行主循环
    root.mainloop()

def grid_example():
    # 创建主窗口
    root = tk.Tk()
    root.configure(bg='red')  # 设置窗口背景颜色为红色
    title_and_icon(root)


    # 创建标签
    label1 = tk.Label(root, text="这是第一个标签", bg="lightblue")
    label2 = tk.Label(root, text="这是第二个标签", bg="lightgreen")
    label3 = tk.Label(root, text="这是第三个标签", bg="pink")

    # 使用 grid 布局管理器放置标签
    label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    label2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    label3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # 使窗口大小可变，并让组件随窗口大小调整
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # 主事件循环
    root.mainloop()

def place_test(window_width=400,window_height=300):
    root = tk.Tk()
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='red')  # 设置窗口背景颜色为红色

   # 创建按钮和标签
    button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked"),width=10,height=5)
    button.place(x=10, y=10)    

    root.update()
    
    label = tk.Label(root, text="Hello, World!",width=20, height=5)
    # 获取按钮的高度
    height = button.winfo_height()
    # 获取按钮的y轴位置（相对于窗口的顶部）
    y_position = button.winfo_y()
    print(height,y_position)

    label.place(x=10, y=height+y_position+10)

    # 进入事件循环
    root.mainloop() 



if __name__=="__main__":
    #Tk_function()
    #pack_test(400,300)
    #pack_example()
    #grid_test()
    #grid_example()
    place_test()