from constants import *
from tool import *
# 杂交实验界面
class ExperimentScreen(tk.Frame):
    """植物杂交系统
    
    1. 基础植物卡片矩阵
    2. 基础植物选择框
    3. 杂交方法选择
    4. 杂交实验开始
    """
    def __init__(self, parent):
        super().__init__(parent)
        # 背景和基础组件
        self.breeding_background = create_background(self,experiment_background_path)
        self.close_button = close_button(self,close2_1_path,close2_2_path,clear=2)
        self.back_button = back_button(self,back2_1_path,back2_2_path,clear=2)
        self.start_button = create_button(self,
                                          dark_image_path=start1_path,
                                          light_image_path=start2_path,
                                          width=351,
                                          height=103,
                                          locate_x=503,
                                          locate_y=455,
                                          command=self.on_start_button_click)
        self.clear_button = create_button(self,
                                          dark_image_path=clearButton1_path,
                                          light_image_path=clearButton2_path,
                                          width=180,
                                          height=100,
                                          locate_x=590,
                                          locate_y=238,
                                          command=self.on_clear_button_click,
                                          )
        self.method_choose_optionmenu()

        # 杂交信息
        self.card_choose_photo = [None for _ in range(4)]
        self.card_choose_photo_id = [0,0,0,0]
        self.card_choose_num = 0
        self.method_id = 0
        self.result_plant_id = 0   
        self.result = 0

        # 基础植物卡片和选择框初始化
        self.empty_card = self.empty_card_load()
        self.card_choose_frame()
        self.card_button_matrix()

        self.pack()

    def empty_card_load(self):
        """空白卡片加载"""
        image = Image.open(emptycard_path)
        image = image.resize((78, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo    

    def card_button_matrix(self):
        """基础植物卡片矩阵"""
        card_frame = tk.Frame(self)
        card_frame.place(x=28,y=88)
        card_frame.config(bg="orange")
        for row in range(6):
            for col in range(8):
                button = tk.Button(card_frame, image=self.master.basal_plant_card[row][col])
                button.config(borderwidth=0,highlightthickness=0)
                button.grid(row=row, column=col,sticky="NSEW")
                def on_click(row, col):
                    if self.card_choose_num ==4 :
                        messagebox.showinfo("错误", "你最多只能添加四种基础植物！")
                    else:
                        self.card_choose_photo_id[self.card_choose_num] = col+1+row*8
                        self.card_choose_num += 1
                        self.card_choose_frame()
                button.bind('<Button-1>', lambda event, r=row, c=col: on_click(r, c))
        
    def card_choose_frame(self):
        """基础植物卡片选择框"""
        self.card_frame = tk.Frame(self,bd=0)
        self.card_frame.place(x=518,y=138)
        for col in range(4):
            if col < self.card_choose_num:
                self.card_choose_photo[col] = image_load(78,100,basal_card_path,self.card_choose_photo_id[col],".jpg")
                label = tk.Label(self.card_frame,image=self.card_choose_photo[col] ,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")
            else:
                label = tk.Label(self.card_frame,image=self.empty_card,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")                

    def method_choose_optionmenu(self):
        """杂交方法选择"""
        def on_option_change(value):
            self.method_id = options.index(value) + 1
        options = [" 基础杂交方式 ",
                   " 使用强化药剂 ", 
                   " 单株辐射变异 ",
                   " 注射僵尸血清 ",
                   " 使用神奇魔法 "]
        
        selected_value = tk.StringVar()
        selected_value.set(" 杂交方式选择 ")
        option_menu = tk.OptionMenu(self, selected_value, *options, command=on_option_change,)
        option_menu.config(font=("华文新魏", 29, "bold"),
                           bg="darkslategray",activebackground="gray",
                           fg="limegreen", activeforeground="lime",
                           borderwidth=0, highlightthickness=0)
        menu = option_menu['menu']
        menu.config(bg="darkslategray", fg="lime", font=("华文新魏", 25, "bold"))
        option_menu.place(x=530, y=386)

    def on_start_button_click(self):
        """开始杂交实验按钮点击事件"""
        if self.card_choose_photo_id[0]!=0 and self.method_id!=0:
            if (self.method_id==3 or self.method_id==4) and self.card_choose_photo_id[1]!=0:
                messagebox.showinfo("提示", "该杂交方法只能选择单株植物！")
                self.on_clear_button_click()
            else:
                self.on_breeding_method_select()
                self.master.children['result_screen'].result_show(self.result,self.result_plant_id)
                self.on_clear_button_click()
                self.master.switch_to_screen('result_screen')
        elif self.card_choose_photo_id[0]!=0 and self.method_id==0:
            messagebox.showinfo("提示", "请选择杂交方式！")
        else:
            messagebox.showinfo("提示", "请选择基础植物！")
    
    def on_clear_button_click(self):
        """清空组件，初始化基础植物选择和杂交方法"""

        self.card_choose_photo_id = [0,0,0,0]
        self.card_choose_num = 0
        self.method_id = 0
        for col in range(4):
            label = tk.Label(self.card_frame,image=self.empty_card,bd=0)
            label.grid(row=0, column=col,sticky="NSEW")      

    def on_breeding_method_select(self):
        """杂交实验: 数据匹配
        
        1. 匹配杂交方法, 成功则:
            a. 匹配规则:
                规则1-4: 亲本植物是否为玩家选择的子集，是则杂交成功
                规则5: 产生一个随机数, 匹配随机植物
            b. 判断是否为新植物, 是则result=0,否则result=1
        2. 失败则: result=2
        3. 跳转至结果界面
        4. 修改杂交植物数据, 添加杂交记录
        """
        def is_subset(list1, list2):
            # 子集判断
            return all(item in list2 for item in list1)
        def is_new(type):
            # 是否为新植物判断
            if type: return 0
            else: return 1

        sign = False
        random_integer = random.randint(0, 6)
        num = 0
        for plant in self.master.hybridizationPlants:
            if plant.get("hybridization_method")==self.method_id: 
                if self.method_id!=5:
                    sign = is_subset(plant.get("parent_base_plant_ids"),self.card_choose_photo_id)
                    if sign==True: break
                else:
                    if num==random_integer:
                        sign=True
                        break
                    else:
                        num += 1
        if sign:
            self.result_plant_id = plant.get("id")
            self.result = is_new(plant.get("new_hybrid"))
            self.master.hybridizationPlants[self.result_plant_id-1]["new_hybrid"] = False
        else:
            self.result = 2
            self.result_plant_id = 0
        self.add_record()

    def add_record(self):
        # 添加杂交记录
        record = {  
                    "id": len(self.master.recorditem)+1,
                    "parent_base_plant_ids": self.card_choose_photo_id,
                    "hybridization_method": self.method_id,
                    "hybridization_plant_id": self.result_plant_id   
                }
        self.master.recorditem.append(record)

class ResultScreen(tk.Frame):
    """杂交结果界面"""
    def __init__(self, parent):
        super().__init__(parent)
        self.breeding_background = create_background(self,result_background_path)
        self.back_button = create_button(self,
                                         dark_image_path=result_back1_path,
                                         light_image_path=result_back2_path,
                                         width=85,
                                         height=25,
                                         locate_x=24,
                                         locate_y=567,
                                         command=self.on_back_button_click)
        self.result_plant = None
        self.result_text = [None, None, None]
        self.result_text_load()
        self.pack()

    def result_text_load(self):
        """加载结果的三种情况"""
        for col in range(3):
            self.result_text[col] = image_load(300,90,result_path,col+1,".png")

    def on_back_button_click(self):
        """返回植物杂交界面"""
        self.master.children['experiment_screen'].on_clear_button_click()
        self.master.switch_to_screen('experiment_screen')

    def result_show(self,result,result_plants_id):
        """result: 
            0. 新植物
            1. 已经获得
            2. 杂交失败
        """
        self.label1 = tk.Label(self,image=self.result_text[result],bd=0)
        self.label1.place(x=290,y=362)

        if result_plants_id!=0:
            self.result_plant = image_load(114,156,hybrid_card_path,result_plants_id,".jpg")
        else:
            image = Image.open(emptyresult_path)
            image = image.resize((114, 156), Image.Resampling.LANCZOS)
            self.result_plant = ImageTk.PhotoImage(image)
        self.label2 = tk.Label(self,image=self.result_plant,bd=0)
        self.label2.place(x=382,y=123)