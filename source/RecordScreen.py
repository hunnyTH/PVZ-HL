from constants import *
from tool import *

class RecordScreen(tk.Frame):
    """杂交记录界面
    1. 每页3条记录
    2. 最多3页记录
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.breeding_background = create_background(self,record_background_path)
        self.close_button = close_button(self,close1_1_path,close1_2_path)
        self.back_button = back_button(self,back1_1_path,back1_2_path)
        self.ahead_buttton = create_button(self,
                                           dark_image_path=ahead2_1_path,
                                           light_image_path=ahead2_2_path,
                                           width=110,
                                           height=27,
                                           locate_x=330,
                                           locate_y=564,
                                           command=self.on_ahead_button_click)
        self.ahead_buttton = create_button(self,
                                           dark_image_path=next2_1_path,
                                           light_image_path=next2_2_path,
                                           width=110,
                                           height=27,
                                           locate_x=450,
                                           locate_y=564,
                                           command=self.on_next_button_click)
        
        self.page = 0
        self.record_num = 0
        self.empty_card = self.empty_card_load()
        self.empty_method = self.empty_method_load()
        self.all_record(page=0)
        self.pack()

    def empty_card_load(self):
        # 加载空白卡片
        image = Image.open(emptycard_path)
        image = image.resize((78, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo  
    def empty_method_load(self):
        # 加载空白方法
        image = Image.open(emptymethod_path)
        image = image.resize((175, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo        
    
    def on_ahead_button_click(self):
        if self.page!=0:
            self.page -= 1
            self.all_record(self.page)
            self.pack()
    def on_next_button_click(self):
        if self.page!=2 and (self.record_num-3*(self.page+1))>0:
            self.page += 1
            self.all_record(self.page)
            self.pack()
  
    def data_load(self):
        """加载杂交记录数据"""
        records = self.master.recorditem
        records = records[::-1]
        self.basal_plants_card = [[None for _ in range(4)] for _ in range(9)]
        self.hybrid_plants_card = [None for _ in range(9)] 
        self.method = [None for _ in range(9)] 
        self.record_num = 0
        for index, item in enumerate(records):
            basal_plant_card = item.get("parent_base_plant_ids")
            for col in range(len(basal_plant_card)):
                if basal_plant_card[col]!=0:
                    self.basal_plants_card[index][col] = image_load(78,100,basal_card_path,basal_plant_card[col],".jpg")
            if item.get("hybridization_plant_id")!=0:
                self.hybrid_plants_card[index] = image_load(78,100,hybrid_card_path,item.get("hybridization_plant_id"),".jpg")
            self.method[index] = image_load(175,100,method_path,item.get("hybridization_method"),".png")
            self.record_num += 1
            if index==8: break

    def one_item(self,id):
        """展示一条数据: 亲本植物+杂交方法+杂交植物"""
        line = id% 3 

        #  亲本植物
        self.card_frame = tk.Frame(self,bd=0)
        self.card_frame.place(x=156,y=108+line*155)
        for col in range(4):
            if self.basal_plants_card[id][col]!=None:
                label = tk.Label(self.card_frame,image=self.basal_plants_card[id][col] ,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")
            else:
                label = tk.Label(self.card_frame,image=self.empty_card,bd=0)
                label.grid(row=0, column=col,sticky="NSEW")         

        # 杂交方法
        if self.method[id]!=None:
            label2 = tk.Label(self,image=self.method[id],bd=0)
        else:
            label2 = tk.Label(self,image=self.empty_method,bd=0)
        label2.place(x=475,y=line*155+109)
        
        # 杂交植物
        if self.hybrid_plants_card[id]!=None:
            label3 = tk.Label(self,image=self.hybrid_plants_card[id],bd=0)
        else:
            label3 = tk.Label(self,image=self.empty_card,bd=0)
        label3.place(x=654,y=line*155+109)

    def all_record(self,page=0):
        self.data_load()
        self.one_item(0+page*3)
        self.one_item(1+page*3)
        self.one_item(2+page*3)
    