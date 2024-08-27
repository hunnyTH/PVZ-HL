from constants import *
from tool import *

class BreedingScreen(tk.Frame):
    """杂交实验室主菜单界面"""
    def __init__(self, parent):
        super().__init__(parent)
        self.breeding_background = create_background(self,breedingScreen_path)
        # 基础植物图鉴按钮
        self.base_catalog_button = create_button(self,
                                                 dark_image_path=plantCatalogButton1_path,
                                                 light_image_path=plantCatalogButton2_path,
                                                 width=360,
                                                 height=180,
                                                 locate_x=81,
                                                 locate_y=104,
                                                 command=self.on_base_catalog_button_click)
        # 杂交植物图鉴按钮
        self.hybrid_catalog_button = create_button(self,
                                                 dark_image_path=hybridCatalogButton1_path,
                                                 light_image_path=hybridCatalogButton2_path,
                                                 width=360,
                                                 height=180,
                                                 locate_x=460,
                                                 locate_y=104,
                                                 command=self.on_hybrid_catalog_button_click)
        # 杂交实验室按钮
        self.experiment_button = create_button(self,
                                                 dark_image_path=experimentButton1_path,
                                                 light_image_path=experimentButton2_path,
                                                 width=360,
                                                 height=180,
                                                 locate_x=81,
                                                 locate_y=293,
                                                 command=self.on_experiment_button_click)
        # 杂交历记录按钮
        self.record_button = create_button(self,
                                                 dark_image_path=historyButton1_path,
                                                 light_image_path=historyButton2_path,
                                                 width=360,
                                                 height=180,
                                                 locate_x=450,
                                                 locate_y=293,
                                                 command=self.on_record_button_click)
        # 杂交建议显示器
        self.advice_text()
        # 关闭界面
        self.close_button = close_button(self,close1_1_path,close1_2_path)
        self.pack()

    def on_base_catalog_button_click(self):
        # 点击基础植物图鉴按钮的事件处理
        self.master.switch_to_screen('plant_catalog_screen')

    def on_hybrid_catalog_button_click(self):
        # 点击杂交植物图鉴按钮的事件处理
        self.master.children['hybrid_catalog_screen'].card_button_matrix(page=0)
        self.master.switch_to_screen('hybrid_catalog_screen')
        
    def on_experiment_button_click(self):
        # 点击杂交实验按钮的事件处理
        self.master.switch_to_screen('experiment_screen')
        
    def on_record_button_click(self):
        # 点击杂交记录按钮的事件处理
        self.master.children['record_screen'].all_record(page=0)
        self.master.switch_to_screen('record_screen')

    def advice_text(self):
        image = Image.open(advice_background_path)
        # 将图片转换为Tkinter可以使用的格式
        image = image.resize((663, 89), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = tk.Label(self, image=photo,bd=0)
        background_label.place(x=106,y=470)
        self.photo = photo

        suggestions = ["你可以尝试不同的杂交方式", 
                       "也许使用不同类型的植物效果会更好！", 
                       "当亲本植物超过四种，会发生糟糕的事！", 
                       "如果没有想法，就去看看历史记录吧！", 
                       "你需要避免完全相反的属性，比如冰与火"]
        random_index = random.randint(0, len(suggestions)-1)
        suggestion = suggestions[random_index]
        button = tk.Button(self,text=suggestion,font=("Times New Roman", 19, "bold"),
                           fg="gold",
                           width=39,height=1,
                           bd=0,background="saddlebrown",
                           command=None,
                           activebackground="saddlebrown"
                           )
        button.place(x=145,y=492)
        self.after(60000,self.advice_text)
