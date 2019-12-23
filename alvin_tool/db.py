'''
Created on 2019/11/30

@author: xcKev
'''
from alvin_tool.models import MenuInfo, LessonMenuIndexInfo


def get_menus(typekey):
    return MenuInfo.objects.filter(Type=typekey,DeleteFlag=0)

def get_menu_indexs(typekey):
    return LessonMenuIndexInfo.objects.filter(Type=typekey,DeleteFlag=0)

