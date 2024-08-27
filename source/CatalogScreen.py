from constants import *
from tool import *

class PlantCatalogScreen(tk.Frame):
    """基础植物图鉴

    1. 卡片矩阵
    2. 植物说明
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.breeding_background = create_background(self,basalcatalog_background_path)
        self.close_button = close_button(self,close2_1_path,close2_2_path,clear=94)
        self.back_button = back_button(self,back2_1_path,back2_2_path,clear=94)
        self.empty_describe = empty_describe(self)
        self.card_button_matrix()
        self.pack()

    def card_button_matrix(self):
        """创建基础植物卡片矩阵"""
        card_frame = tk.Frame(self)
        card_frame.place(x=28,y=88)
        for row in range(6):
            for col in range(8):
                def on_click(row, col):
                    card_music.play()
                    """卡片点击事件, 展示植物说明"""
                    label = tk.Label(self, image=self.master.basal_plant_describe[row][col], bd=0)
                    label.place(x=530, y=94)                
                button = tk.Button(card_frame, image=self.master.basal_plant_card[row][col])
                button.config(borderwidth=0,highlightthickness=0)
                button.grid(row=row, column=col,sticky="NSEW")
                button.bind('<Button-1>', lambda event, r=row, c=col: on_click(r, c))

class HybridCatalogScreen(tk.Frame):
    """基础植物图鉴

    1. 卡片矩阵(翻页功能, 包含两个页面)
    2. 植物说明
    3. 更多信息
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.breeding_background = create_background(self,hybridCatalog_background_path)
        self.close_button = close_button(self,close2_1_path,close2_2_path,clear=82)
        self.back_button = back_button(self,back2_1_path,back2_2_path,clear=82)
        self.ahead_buttton = create_button(self,
                                           dark_image_path=ahead1_1_path,
                                           light_image_path=ahead1_2_path,
                                           width=110,
                                           height=27,
                                           locate_x=265,
                                           locate_y=566,
                                           command=self.on_ahead_button_click)
        self.next_buttton = create_button(self,
                                           dark_image_path=next1_1_path,
                                           light_image_path=next1_2_path,
                                           width=110,
                                           height=27,
                                           locate_x=377,
                                           locate_y=566,
                                           command=self.on_next_button_click)
        self.more_button = create_button(self,
                                         dark_image_path=morebutton1_path,
                                         light_image_path=morebutton2_path,
                                         width=138,
                                         height=40,
                                         locate_x=603,
                                         locate_y=542,
                                         command=self.on_more_button_click)        
        self.empty_describe = empty_describe(self,Y=82)

        self.init_card_photo = [[None for _ in range(8)] for _ in range(6)] # 卡片矩阵背景
        self.old_hybrid_plant = [[0 for _ in range(8)] for _ in range(12)]  # 杂交前可展示植物id
        self.new_hybrid_plant = [[0 for _ in range(8)] for _ in range(12)]  # 杂交后可展示植物id

        # 卡片矩阵初始化
        self.plants_num = 0
        self.page = 0
        self.page_change = False
        self.card_frame = tk.Frame(self,bd=0)
        self.card_frame.place(x=28,y=89)
        self.init_card_matrix()
        self.card_button_matrix(page=0,init=1)

        # 记录植物亲本及杂交方法信息
        self.method = 0
        self.basal_plant_ids = [0,0,0,0]
        self.pack()

    def init_card_matrix(self):
        """加载卡片矩阵空白背景"""
        for row in range(6):
            for col in range(8):
                self.init_card_photo[row][col]= image_load(57,78,init_card_path,col+1+row*8,".jpg")  

    def on_ahead_button_click(self):
        """上一页按钮点击事件"""
        if self.page==1:
            self.page_change = True
            self.page=0
            self.card_button_matrix(page=self.page)
            self.empty_describe = empty_describe(self,Y=82)
            self.pack()
        self.page_change = False

    def on_next_button_click(self):
        """下一页按钮点击事件"""
        if self.page==0 and self.plants_num>48:
            self.page_change = True
            self.page=1
            self.card_button_matrix(page=self.page)
            self.empty_describe = empty_describe(self,Y=82)
            self.pack()
        self.page_change = False

    def on_more_button_click(self):
        """查看更多信息按钮点击事件"""
        if self.method!=0 and self.basal_plant_ids[0]!=0:
            self.master.children['more_information_screen'].information_show(self.method,self.basal_plant_ids)
            self.master.switch_to_screen('more_information_screen') 
        self.method=0
        self.basal_plant_ids = [0,0,0,0]     

    def data_load(self,hybridizationplants):
        """加载展示杂交植物卡片"""
        self.plants_num=0; row = 0; col = 0
        for plant in hybridizationplants:
            if plant.get('new_hybrid')==False: 
                self.plants_num += 1
                self.new_hybrid_plant[row][col] = plant.get("id")         
                col += 1
                if col==8:
                    row += 1
                    col = 0

    def card_button_matrix(self,page=0,init=0):
        """创建杂交植物卡片矩阵
        
        1. 保存上一次卡片数据
        2. 加载最新卡片数据
        3. 只改变更新部分的按钮图片
        4. 使用self.page加载不同页面的数据
        """
        if init==0: 
            for row in range(12):
                for col in range(8):
                    self.old_hybrid_plant[row][col] = self.new_hybrid_plant[row][col]
        self.data_load(self.master.hybridizationPlants)
        for row in range(6):
            for col in range(8):
                if self.new_hybrid_plant[row+page*6][col]!=self.old_hybrid_plant[row+page*6][col] or \
                    (self.page_change==True and self.new_hybrid_plant[row+page*6][col]!=0): 
                    card_photo = id_to_photo(self.new_hybrid_plant[row+page*6][col],self.master.hybrid_plant_card)
                    button = tk.Button(self.card_frame, image=card_photo)
                    button.config(borderwidth=0,highlightthickness=0)
                    button.grid(row=row, column=col,sticky="NSEW")
                    def on_click(row, col):
                        card_music.play()
                        describe_photo = id_to_photo(self.new_hybrid_plant[row+page*6][col],self.master.hybrid_plant_describe)
                        label = tk.Label(self, image=describe_photo, bd=0)
                        label.place(x=530, y=82)
                        id = self.new_hybrid_plant[row+page*6][col]
                        self.basal_plant_ids = self.master.hybridizationPlants[id-1].get("parent_base_plant_ids")
                        self.method = self.master.hybridizationPlants[id-1].get("hybridization_method")
                    button.bind('<Button-1>', lambda event, r=row, c=col: on_click(r, c))
                elif self.new_hybrid_plant[row+page*6][col]==0 :
                    label = tk.Label(self.card_frame,image=self.init_card_photo[row][col],bd=0)
                    label.grid(row=row, column=col,sticky="NSEW")

class MoreInformation(tk.Frame):
    """杂交植物更多信息界面，包括杂交方法和亲本植物说明"""
    def __init__(self, parent):
        super().__init__(parent)
        self.more_background = create_background(self,mor_background_path)
        self.back_button = create_button(self,
                                         dark_image_path=back1_1_path,
                                         light_image_path=back1_2_path,
                                         width=85,
                                         height=25,
                                         locate_x=24,
                                         locate_y=567,
                                         command=self.on_back_button_click)
        self.empty_information = self.empty_information_load()
        self.pack()

    def empty_information_load(self):
        """加载空的描述卡片"""
        image = Image.open(emptydescribe_path)
        image = image.resize((212, 308), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo  
    
    def on_back_button_click(self):
        # 返回杂交植物图鉴界面
        self.master.switch_to_screen('hybrid_catalog_screen')

    def information_show(self,method,basal_plant_ids):
        """展示杂交方法"""
        self.method = image_load(560,120,more_method_path,method,".png")
        label = tk.Label(self,image=self.method,bd=0)
        label.place(x=160,y=82)

        """展示亲本植物信息"""
        self.basal_plant_describe = [None for _ in range(4)]
        self.card_frame = tk.Frame(self,bd=0)
        self.card_frame.place(x=15,y=202)
        for col in range(4):
            if col<len(basal_plant_ids) and basal_plant_ids[col]!=0:
                self.basal_plant_describe[col] = image_load(212,308,basal_describe_path,basal_plant_ids[col],'.png')
                label = tk.Label(self.card_frame,image=self.basal_plant_describe[col] ,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")
            else:
                label = tk.Label(self.card_frame,image=self.empty_information,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")  
