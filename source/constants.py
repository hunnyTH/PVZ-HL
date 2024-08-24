import random
import json
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk


game_name = "植物杂交实验室"
window_width = 880
window_height = 600

hybridizationplants_data_path = r"data\hybridizationPlants.json"
record_data_path = r"data\record.json"
"""
杂交规则：
1. 基础杂交方式
2. 加强杂交方式
3. 单株变异
4. 僵尸感染
5. 神秘结果
"""

# common
icon_path = r"images\Screen\common\PVZ.ico"
loading_path = r"images\Screen\common\loading.gif"
back1_1_path = r"images\Screen\common\back1_1.png"
back1_2_path = r"images\Screen\common\back1_2.png"
close1_1_path = r"images\Screen\common\close1_1.png"
close1_2_path = r"images\Screen\common\close1_2.png"
back2_1_path = r"images\Screen\common\back2_1.png"
back2_2_path = r"images\Screen\common\back2_2.png"
close2_1_path = r"images\Screen\common\close2_1.png"
close2_2_path = r"images\Screen\common\close2_2.png"
emptydescribe_path= r"images\Screen\common\emptydescribe.png"


# 游戏主界面
mainscreen_path = r"images\Screen\mainmenu\mainmenu.gif"
menubutton1_path = r"images\Screen\mainmenu\menubutton1.png"
menubutton2_path = r"images\Screen\mainmenu\menubutton2.png"

# 杂交实验室
breedingScreen_path= r"images\Screen\breeding\BreedingScreen.png"
plantCatalogButton1_path = r"images\Screen\breeding\PlantCatalogButton1.png"
plantCatalogButton2_path = r"images\Screen\breeding\PlantCatalogButton2.png"
hybridCatalogButton1_path = r"images\Screen\breeding\HybridCatalogButton1.png"
hybridCatalogButton2_path = r"images\Screen\breeding\HybridCatalogButton2.png"
experimentButton1_path = r"images\Screen\breeding\ExperimentButton1.png"
experimentButton2_path = r"images\Screen\breeding\ExperimentButton2.png"
historyButton1_path = r"images\Screen\breeding\HistoryButton1.png"
historyButton2_path = r"images\Screen\breeding\HistoryButton2.png"
advice_background_path = r"images\Screen\breeding\adviceLabel.png"

# 基础植物图鉴
basalcatalog_background_path = r"images\Screen\basalcatalog\background.png"
basal_describe_path = "images\\Plantsdescribe\\basalPlants\\"
basal_card_path = "images\\PlantsCard\\basalPlants\\"

# 杂交植物图鉴
hybridCatalog_background_path = r"images\Screen\hybridcatalog\background.png"
ahead1_1_path = r"images\Screen\hybridcatalog\ahead1.png"
ahead1_2_path = r"images\Screen\hybridcatalog\ahead2.png"
next1_1_path = r"images\Screen\hybridcatalog\next1.png"
next1_2_path = r"images\Screen\hybridcatalog\next2.png"
init_card_path = "images\\Screen\\init_card\\"
hybrid_describe_path = "images\\Plantsdescribe\\hybridizationPlants\\"
hybrid_card_path = "images\\PlantsCard\\hybridizationPlants\\"

# 更多信息
morebutton1_path = r"images\Screen\HybridCatalog\more1.png"
morebutton2_path = r"images\Screen\HybridCatalog\more2.png"
mor_background_path = r"images\Screen\more\background.png"
more_method_path = "images\\Screen\\more\\method"

# 杂交实验
experiment_background_path = r"images\Screen\experiment\background.png"
start1_path = r"images\Screen\experiment\start1.png"
start2_path = r"images\Screen\experiment\start2.png"
clearButton1_path = r"images\Screen\experiment\clear_1.png"
clearButton2_path = r"images\Screen\experiment\clear_2.png"
emptycard_path = r"images\Screen\experiment\emptycard.png"
# 杂交结果
result_background_path= r"images\Screen\result\background.png"
result_back1_path = r"images\Screen\result\back1.png"
result_back2_path = r"images\Screen\result\back2.png"
result_path = "images\\Screen\\result\\result"
emptyresult_path = r"images\Screen\result\emptyresult.png"

# 杂交历史记录
record_background_path = r"images\Screen\record\background.png"
ahead2_1_path = r"images\Screen\record\ahead_1.png"
ahead2_2_path = r"images\Screen\record\ahead_2.png"
next2_1_path = r"images\Screen\record\next_1.png"
next2_2_path = r"images\Screen\record\next_2.png"
method_path = "images\\Screen\\record\\method_"
emptymethod_path = r"images\Screen\record\emptymethod.png"
