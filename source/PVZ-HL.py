from constants import *
from tool import *
from BreedingScreen import BreedingScreen
from LoadingScreen import LoadingScreen,MainScreen
from CatalogScreen import PlantCatalogScreen, HybridCatalogScreen, MoreInformation
from ExperimentScreen import ExperimentScreen,ResultScreen
from RecordScreen import RecordScreen
# 应用程序主窗口
class PVZ_HL(tk.Tk):
    def __init__(self):
        super().__init__()
        # 数据加载
        self.basal_plant_card = [[None for _ in range(8)] for _ in range(6)]
        self.basal_plant_describe = [[None for _ in range(8)] for _ in range(6)]
        self.hybrid_plant_card =  [[None for _ in range(8)] for _ in range(12)]
        self.hybrid_plant_describe =  [[None for _ in range(8)] for _ in range(12)]
        self.basal_plant_load()
        self.hybrid_plant_load()
        self.hybridizationPlants = json_dataload(hybridizationplants_data_path)
        self.recorditem = json_dataload(record_data_path)
        # 窗口创建
        self.init_window()
        self.title(game_name)
        self.iconbitmap(icon_path)
        self.protocol("WM_DELETE_WINDOW", self.on_close)     
        pygame.mixer.music.play(loops=-1)  # 无限循环播放
        self.children['loading_screen'] = LoadingScreen(self)
        self.children['main_screen'] = MainScreen(self)
        self.children['breeding_screen'] = BreedingScreen(self)
        self.children['plant_catalog_screen'] = PlantCatalogScreen(self)
        self.children['hybrid_catalog_screen'] = HybridCatalogScreen(self)
        self.children['more_information_screen'] = MoreInformation(self)
        self.children['experiment_screen'] = ExperimentScreen(self)
        self.children['result_screen'] = ResultScreen(self)
        self.children['record_screen'] = RecordScreen(self)

    def basal_plant_load(self):
        """基础植物卡片和说明加载"""
        for row in range(6):
            for col in range(8):
                self.basal_plant_card[row][col]= image_load(57,78,basal_card_path,col+1+row*8,".jpg")
                self.basal_plant_describe[row][col] = image_load(287,462,basal_describe_path,col+1+row*8,".png")

    def hybrid_plant_load(self):
        """杂交植物卡片和说明加载"""
        for row in range(12):
            for col in range(8):
                self.hybrid_plant_card[row][col]= image_load(57,78,hybrid_card_path,col+1+row*8,".jpg")
                self.hybrid_plant_describe[row][col] = image_load(287,462,hybrid_describe_path,col+1+row*8,".png")
                if row==11 and col==3:break

    def init_window(self):
        """窗口初始化"""
        self.resizable(width=False, height=False)
        self.configure(bg='black')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def switch_to_screen(self, screen_name):
        """界面跳转"""
        for page in self.children.values():
            page.pack_forget()
        self.children[screen_name].pack()

    def on_close(self):
        """游戏关闭，保存数据"""
        if messagebox.askokcancel("退出", "确定要退出游戏吗？"):
            self.destroy()
            json_datasave(hybridizationplants_data_path,self.hybridizationPlants)
            json_datasave(record_data_path,self.recorditem)
            pygame.quit()


if __name__ == '__main__':
    """主程序入口"""
    app = PVZ_HL()
    app.mainloop()