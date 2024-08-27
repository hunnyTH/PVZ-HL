import math
import tkinter as tk
from Day2 import *
from PIL import Image, ImageTk
from tkinter import simpledialog,messagebox,filedialog
from tkinter import ttk


def toplexel_example(root):
    def open_dialog():
        dialog = tk.Toplevel(root)
        dialog.title("弹出窗口")
        dialog.geometry("200x100")
        label = tk.Label(dialog, text="这是一个弹出窗口！")
        label.pack(pady=20)
    button = tk.Button(root, text="打开弹出窗口", command=open_dialog)
    button.pack(pady=20)

def label_example(root):
    # 文字
    label = tk.Label(root, text="Hello, World!", bg="yellow", fg="red", font=("Arial", 16), anchor="center")
    label.pack(pady=20)

    # 图片
    img = Image.open(r"图片\transformer.png")
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img  # 保持引用，防止垃圾回收
    label.pack()

def button_example(root):
    def on_button_click():
        print("按钮被点击了！")

    # 创建一个按钮，并应用一些参数
    button = tk.Button(root, text="点击我",
                        command=on_button_click,
                        padx=20, 
                        pady=10,
                        bg="blue",
                        fg="white",
                        font=("Arial", 16), 
                        relief="solid", 
                        overrelief="sunken", 
                        activebackground="green", 
                        activeforeground="black", 
                        cursor="hand2")
    
    button.pack(pady=20)

def entry_example(root):
    # 假设的登录信息
    correct_id = "962464"
    correct_password = "123456"

    def login():
        # 获取输入框中的内容
        user_id = id_entry.get()
        user_password = password_entry.get()

        # 检查用户输入的ID和密码是否正确
        if user_id == correct_id and user_password == correct_password:
            messagebox.showinfo("登录成功", "登录成功！")
        else:
            messagebox.showerror("登录失败", "登录失败，请检查您的用户名和密码。")


    # 创建ID标签和输入框
    id_label = tk.Label(root, text=" 账户：")
    id_label.grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(root, width=20)
    id_entry.insert(0, "962464")  # 初始化ID
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    # 创建密码标签和输入框
    password_label = tk.Label(root, text="密码：")
    password_label.grid(row=1, column=0, padx=10, pady=10)

    password_entry = tk.Entry(root, width=20, show="*")  # 密码输入框显示星号
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # 创建登录按钮
    login_button = tk.Button(root, text="登录", command=login)
    login_button.grid(row=2, column=1, pady=10)

def text_example(root):
    def insert_text():
        text_area.insert(tk.END, "这是一个新文本\n")

    text_area = tk.Text(root, height=5, width=20)
    text_area.grid(row=0, column=0, sticky="nsew")

    scrollbar = tk.Scrollbar(root, command=text_area.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    text_area.config(yscrollcommand=scrollbar.set)

    button = tk.Button(root, text="插入文本", command=insert_text)
    button.grid(row=1, column=0, columnspan=2, sticky="ew")

    # 配置行列权重，确保文本框和滚动条可以扩展
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

def listbox_example(root):
    def select_item(event):
        # 使用event参数来获取选中的项
        index = event.widget.curselection()[0]
        selected_item = event.widget.get(index)
        # 更新文本框的内容
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, selected_item)

    # 创建Listbox
    listbox = tk.Listbox(root, selectmode='single', bg='light blue', fg='black', font=('Helvetica', 10))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # 创建滚动条
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # 绑定滚动条
    listbox.config(yscrollcommand=scrollbar.set)

    # 添加项目到Listbox
    items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']
    for item in items:
        listbox.insert('end', item)

    # 创建文本框
    text_box = tk.Text(root, height=2, width=20, bg='white', fg='black', font=('Helvetica', 10))
    text_box.pack(side=tk.LEFT, fill=tk.Y, expand=False)

    # 绑定事件到Listbox组件
    listbox.bind('<<ListboxSelect>>', select_item)

def Scrollbar_example(root):
    def on_xscroll(event):
        canvas.xview_scroll(-int(event.delta/120), 'units')

    # 创建一个Canvas，并设置其宽度和高度
    canvas_width = 600
    canvas_height = 100
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')

    # 定义正弦曲线的参数
    amplitude = 40  # 波幅
    period = 100    # 周期
    phase_shift = 0 # 相位移动
    x_scale = 0.1   # 横坐标缩放

    # 在Canvas上创建正弦曲线
    points = []
    for i in range(0, canvas_width, 2):
        x = i / x_scale
        y = amplitude * math.sin((x / period) + phase_shift)
        y = canvas_height / 2 - y  # 将y坐标移动到Canvas中心
        points.append((i, y))

    # 绘制正弦曲线
    canvas.create_line(points, fill='blue')

    # 将Canvas的内容超出部分设置为可滚动
    canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

    # 创建一个Scrollbar，并与Canvas关联
    scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side="bottom", fill="x")

    # 将Scrollbar的滚动事件与Canvas的滚动方法关联
    canvas.config(xscrollcommand=scrollbar.set)
    canvas.bind('<MouseWheel>', on_xscroll)

    # 将Canvas放置到窗口中
    canvas.pack(side="left", fill="both", expand=True)

def checkbutton_example(root):
    def update_display(*args):
        selected_items = [f"Item {i+1}" for i, var in enumerate(var_list) if var.get()]
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, '\n'.join(selected_items))

    # 创建Checkbutton列表
    var_list = []
    labels = ["Item 01", "Item 02", "Item 03", "Item 04", "Item 05", "Item 06", "Item 07", "Item 08", "Item 09", "Item 10"]
    for i, label in enumerate(labels):
        var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(root, text=label, variable=var)
        checkbutton.grid(row=i, column=0, sticky='w', padx=5)  # 左对齐，添加内边距
        var_list.append(var)

    # 创建一个文本框用于显示选中的标签
    display_text = tk.Text(root)
    display_text.grid(row=0, column=1, rowspan=11,sticky='nsew')

    # 使用trace方法追踪变量的变化
    for var in var_list:
        var.trace('w', update_display)

def radiobutton_example(root):
    def display_choice():
        # 获取用户选择的选项
        choice = var.get()
        # 显示所选选项
        result_label.config(text="您选择了: " + choice)


    # 创建一个关联的变量
    var = tk.StringVar()
    var.set("Option 1")
    # 创建三个单选按钮
    r1 = tk.Radiobutton(root, text="选项1", variable=var, value="Option 1", command=display_choice)
    r2 = tk.Radiobutton(root, text="选项2", variable=var, value="Option 2", command=display_choice)
    r3 = tk.Radiobutton(root, text="选项3", variable=var, value="Option 3", command=display_choice)

    # 将单选按钮放置在窗口中
    r1.pack()
    r2.pack()
    r3.pack()

    # 显示所选选项的标签
    result_label = tk.Label(root, text="",width=20)
    result_label.pack()

def optionmenu_example(root):
    def update_label(*args):
        # 更新标签显示当前选中的选项
        label.config(text="当前选择: " + selected_option.get())

    # 创建一个StringVar对象，用于存储OptionMenu的当前选项
    selected_option = tk.StringVar(root)
    # 设置StringVar的初始值，这里设置为options列表中的第一个元素
    selected_option.set("选项1")

    # 创建一个OptionMenu，其中包含三个选项
    option_menu = tk.OptionMenu(root, selected_option, "选项1", "选项2", "选项3", command=update_label)
    option_menu.pack()

    # 创建一个标签，用于显示当前选中的选项
    label = tk.Label(root, text="",width=20)
    label.pack()

def labelframe_example(root):
    def submit_success():
        # 这个函数会在按钮被点击后运行，显示一个消息框
        messagebox.showinfo("提交成功", "您的信息已成功提交！")

    # 创建一个LabelFrame，带有标题"个人信息"
    personal_info_frame = tk.LabelFrame(root, text="个人信息", padx=10, pady=10)
    personal_info_frame.pack(padx=20, pady=20, fill='both', expand=True)

    # 在LabelFrame内创建一个Label
    name_label = tk.Label(personal_info_frame, text="姓名:")
    name_label.pack()

    # 在LabelFrame内创建一个Entry控件
    name_entry = tk.Entry(personal_info_frame)
    name_entry.pack()

    # 在LabelFrame内创建一个Button控件
    submit_button = tk.Button(personal_info_frame, text="提交", command=submit_success)
    submit_button.pack()

def gif_example(root):
    label = tk.Label(root)
    label.pack()

    # 确保路径正确，并且文件存在
    image_path = "图片\\checkbutton.gif"
    try:
        image = Image.open(image_path)
    except IOError:
        print(f"无法加载图像文件：{image_path}")
        return

    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # 保存对photo对象的引用

    def update_loading(i):
        if i < image.n_frames:  # 使用 image.n_frames 获取帧数
            image.seek(i)
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo  # 保存对photo对象的引用
            root.after(100, update_loading, i + 1)
        else:
            label.config(image=tk.PhotoImage())  # 清除图像
            root.update_idletasks()

    update_loading(0)

def imagebutton_example(root):
    def on_button_click():
        messagebox.showinfo("测试成功！", "按钮被点击了！")

    image_path = r"图片\button.png"  # 确保路径正确，并且图像文件存在
    try:
        # 尝试打开图像文件
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        # 创建图像按钮
        button = tk.Button(root, image=photo, text="点击我", compound="bottom", command=on_button_click)
        button.image = photo  # 保持对 photo 的引用
        button.pack()
    except Exception as e:
        messagebox.showerror("错误", f"无法加载图像：{e}")

def progressbar_example(root):
    # 更新进度条函数
    def update_progress():
        for i in range(101):
            progress_bar['value'] = i
            root.update_idletasks()  # 更新GUI
            root.update()  # 更新窗口
            root.after(100)  # 每100ms更新一次    

    # 创建进度条
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100, length=300)
    progress_bar.pack(pady=20)

    # 开始进度条
    progress_bar.start(100)  # 设置进度条的更新频率为 100ms

    # 创建一个按钮来控制进度条
    button = tk.Button(root, text="Start Progress", command=update_progress)
    button.pack()

def menu_example(root):
    def open_file():
        print("打开文件")
    def save_file():
        print("保存文件")
    def exit_app():
        root.destroy()
    def cut_text():
        print("剪切文本")
    def copy_text():
        print("复制文本")
    def paste_text():
        print("粘贴文本")

    # 创建菜单栏
    menu_bar = tk.Menu(root)

    # 创建文件菜单
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="打开", command=open_file)
    file_menu.add_command(label="保存", command=save_file)
    file_menu.add_separator()  # 添加分隔线
    file_menu.add_command(label="退出", command=exit_app)

    # 创建编辑菜单
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="剪切", command=cut_text)
    edit_menu.add_command(label="复制", command=copy_text)
    edit_menu.add_command(label="粘贴", command=paste_text)

    # 将菜单添加到菜单栏
    menu_bar.add_cascade(label="文件", menu=file_menu)
    menu_bar.add_cascade(label="编辑", menu=edit_menu)

    # 将菜单栏设置到窗口
    root.config(menu=menu_bar)
    
def frame_example(root):
    def on_button_click():
        messagebox.showinfo("Frame 1", "按钮在Frame 1被点击了！")

    def on_button_click_frame2():
        messagebox.showinfo("Frame 2", "按钮在Frame 2被点击了！")

    # 创建第一个Frame
    frame1 = tk.Frame(root, bg='lightgray', padx=20, pady=20)
    frame1.pack(padx=20, pady=10, fill='both', expand=True)

    # 在Frame 1中添加一个按钮
    button_frame1 = tk.Button(frame1, text="点击我（Frame 1）", command=on_button_click)
    button_frame1.pack(pady=10)

    # 创建第二个Frame
    frame2 = tk.Frame(root, bg='blue', padx=20, pady=20)
    frame2.pack(padx=20, pady=10, fill='both', expand=True)

    # 在Frame 2中添加一个按钮
    button_frame2 = tk.Button(frame2, text="点击我（Frame 2）", command=on_button_click_frame2)
    button_frame2.pack(pady=10)
    
def messagebox_example(root):
    # 显示一个信息框
    messagebox.showinfo("信息", "这是一条信息")

    # 显示一个询问框
    if messagebox.askquestion("询问", "你确定要退出吗？") == 'yes':
        print("用户点击了 'Yes'")
    else:
        print("用户点击了 'No'")

    # 显示一个确认对话框，用户必须点击 'OK' 或 'Cancel'
    response = messagebox.askokcancel("确认", "你确定要删除这些文件吗？")
    if response:
        print("用户点击了 'OK'")
    else:
        print("用户点击了 'Cancel'")

    # 显示一个错误框
    messagebox.showerror("错误", "发生了一个错误！")

    # 显示一个警告框
    messagebox.showwarning("警告", "你正在尝试访问一个受限的区域！")


def simpledialog_example(root):
    # 创建一个文本框用于显示信息
    text_area = tk.Text(root, height=10, width=50)
    text_area.pack()

    # 获取用户输入的字符串
    name = simpledialog.askstring("输入", "请输入您的名字：")
    if name is None:
        text_area.insert(tk.END, "用户取消了名字输入\n")
    else:
        text_area.insert(tk.END, "您输入的名字是: {}\n".format(name))

    # 获取用户输入的整数
    age = simpledialog.askinteger("输入", "请输入您的年龄：", minvalue=0)
    if age is None:
        text_area.insert(tk.END, "用户取消了年龄输入\n")
    else:
        text_area.insert(tk.END, "您输入的年龄是: {}\n".format(age))

    # 获取用户输入的浮点数
    weight = simpledialog.askfloat("输入", "请输入您的体重（千克）：")
    if weight is None:
        text_area.insert(tk.END, "用户取消了体重输入\n")
    else:
        text_area.insert(tk.END, "您输入的体重是: {}\n".format(weight))

def filedialog_example(root):
    def open_file():
        # 打开文件选择对话框
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            # 显示所选文件的路径
            result_label.config(text="已选择文件: " + file_path)

    def save_file():
        # 打开保存文件对话框
        file_path = filedialog.asksaveasfilename(
            title="保存文件",
            defaultextension="txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            # 显示保存的文件路径
            result_label.config(text="已保存文件: " + file_path)

    def open_directory():
        # 打开目录选择对话框
        directory_path = filedialog.askdirectory()
        if directory_path:
            # 显示所选目录的路径
            result_label.config(text="已选择目录: " + directory_path)

    def exit_program():
        # 退出程序
        root.destroy()

    # 创建一个标签用于显示结果
    result_label = tk.Label(root, text="请执行一个操作")
    result_label.pack(pady=10)

    # 创建按钮，用于打开文件选择对话框
    open_button = tk.Button(root, text="打开文件", command=open_file)
    open_button.pack(pady=5)

    # 创建按钮，用于保存文件
    save_button = tk.Button(root, text="保存文件", command=save_file)
    save_button.pack(pady=5)

    # 创建按钮，用于打开目录选择对话框
    directory_button = tk.Button(root, text="打开目录", command=open_directory)
    directory_button.pack(pady=5)

    # 创建按钮，用于退出程序
    exit_button = tk.Button(root, text="退出程序", command=exit_program)
    exit_button.pack(pady=5)

if __name__=="__main__":
    root = tk.Tk()
    window_width = 400
    window_height = 300
    title_and_icon(root)
    #window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='lightBlue')  # 设置窗口背景颜色为红色

    #toplexel_example(root)
    label_example(root)
    #button_example(root)
    #entry_example(root)
    #text_example(root)
    #listbox_example(root)
    #Scrollbar_example(root)
    #checkbutton_example(root)
    #radiobutton_example(root)
    #optionmenu_example(root)
    #labelframe_example(root)
    #gif_example(root)
    #imagebutton_example(root)
    #progressbar_example(root)
    #menu_example(root)
    #frame_example(root)
    #messagebox_example(root)
    #simpledialog_example(root)
    #filedialog_example(root)
    root.mainloop()