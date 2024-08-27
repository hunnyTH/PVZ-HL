import tkinter as tk
from Day2 import *

def optionmenu_example(root):
    def on_option_change(value):
        method_id = options.index(value) + 1
        messagebox.showinfo("选择", "选项"+ str(method_id) + ": "+value)

    # 创建 OptionMenu 的变量,字符串类型
    options = [" 默认杂交方式 ",
               " 强化杂交方式 ", 
               " 随机杂交方式 "]
    selected_value = tk.StringVar()
    selected_value.set(" 杂交方式选择 ")
    # 创建 OptionMenu
    option_menu = tk.OptionMenu(root, selected_value, *options, command=on_option_change,)
    # 美化界面
    option_menu.config(font=("华文新魏", 29, "bold"),
                       bg="darkslategray",activebackground="gray",
                       fg="limegreen", activeforeground="lime",
                       borderwidth=0, highlightthickness=0
                       )
    # 获取 OptionMenu 的菜单对象
    menu = option_menu['menu']
    # 设置菜单背景颜色
    menu.config(bg="darkslategray", fg="lime", font=("华文新魏", 25, "bold"))

    option_menu.pack(side=tk.TOP,pady=20)

def example(root):

    img_gif = tk.PhotoImage(file = r"images\Rock.png")#测试图片路径
    label_img = tk.Label(root, image = img_gif)  #设置 label 背景色为透明色'gray'
    root.img = img_gif
    label_img.pack()


if __name__=="__main__":
    root = tk.Tk()
    window_width = 400
    window_height = 300
    title_and_icon(root)
    window_size(root,window_width,window_height)
    window_location(root,window_width,window_height)
    root.configure(bg='lightBlue')  # 设置窗口背景颜色为红色

    #optionmenu_example(root)
    example(root)
    root.mainloop()