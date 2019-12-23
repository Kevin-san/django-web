'''
Created on 2019/11/30

@author: xcKev
'''
from alvin_tool.entitys import HomeIndexItem
from alvin_tool import db
from alvin_core import common_tools

def get_home_index():
    menu_list = db.get_menus('index')
    val_list = []
    for menu in menu_list:
        menu_type = menu.Href.split('#')[1]
        index_list = db.get_menu_indexs(menu_type)
        item = HomeIndexItem(menu_type,menu.Text,index_list)
        val_list.append(item)
    keys = ['menu_list','val_list']
    vals = [menu_list,val_list]
    return common_tools.create_map(keys,vals)
    