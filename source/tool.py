from constants import *

def create_background(root,image_path):
    # 加载图片背景
    image = Image.open(image_path)
    image = image.resize((880, 600), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.photo = photo
    label.pack()

def create_button(root,dark_image_path, light_image_path,width,height,locate_x,locate_y,command):
    """创建按钮：加载暗和明亮两张图片, 模拟点击效果
    """
    img_dark = Image.open(dark_image_path)
    img_light = Image.open(light_image_path)
    img_dark = img_dark.resize((width, height), Image.Resampling.LANCZOS)
    img_light = img_light.resize((width, height), Image.Resampling.LANCZOS)
    photo_dark = ImageTk.PhotoImage(img_dark)
    photo_light = ImageTk.PhotoImage(img_light)
    def on_enter(event):
        label.config(image=photo_light)
    def on_leave(event):
        label.config(image=photo_dark)
    def on_click(event):
        button_music.play()
        command()

    # 创建Label作为按钮
    label = tk.Label(root, image=photo_dark, cursor="hand2",bd=0)
    label.photo = photo_dark  # 保持对图像的引用
    label.place(x=locate_x,y=locate_y)

    # 绑定鼠标事件
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<Button-1>", on_click)  # 绑定鼠标左键点击事件

def close_button(root,path_1,path_2,clear=0):
    """关闭按钮"""
    def on_close_button_click():
        # 点击关闭按钮的事件处理
        if clear==2:
            root.on_clear_button_click()
            root.method_choose_optionmenu()
            root.pack()
        elif clear==94 or clear==82:
            root.empty_describe = empty_describe(root,Y=clear)
            root.pack() 
        root.master.switch_to_screen('main_screen')

    create_button(root,
                  dark_image_path=path_1,
                  light_image_path=path_2,
                  width=85,
                  height=25,
                  locate_x=770,
                  locate_y=567,
                  command=on_close_button_click)       

def back_button(root,path_1,path_2,clear=0):
    """返回按钮"""
    def on_back_button_click():
        # 点击返回按钮的事件处理 
        if clear==2:
            root.on_clear_button_click()
            root.method_choose_optionmenu()
            root.pack()
        elif clear==94 or clear==82:
            root.empty_describe = empty_describe(root,Y=clear)
            root.pack()     
        root.master.switch_to_screen('breeding_screen')
    create_button(root,
                  dark_image_path=path_1,
                  light_image_path=path_2,
                  width=85,
                  height=25,
                  locate_x=24,
                  locate_y=567,
                  command=on_back_button_click)         
    
def empty_describe(root,Y=94):
    """空白植物描述
    基础植物图鉴和杂交植物图鉴的位置不同, 用参数Y区分
    """
    image = Image.open(emptydescribe_path)
    image = image.resize((287, 462), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo,bd=0)
    label.photo = photo
    label.place(x=530,y=Y)

def json_dataload(path):
    with open(path, 'r', encoding='utf-8') as file:
        data_list = json.load(file)
    return  data_list

def json_datasave(path,datalist):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(datalist, file, indent=4)

def image_load(width,height,path,num,suffix):
    """主要用于加载植物卡片和植物描述, 主路径相同, id命名"""
    full_path = path + str(num)+suffix
    image = Image.open(full_path)
    image = image.resize((width, height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    return photo    

def id_to_photo(id,data):
    """根据id查找图片, 在图鉴中使用"""
    hang =  (id-1)//8
    lie = id-hang*8-1
    return data[hang][lie]
    