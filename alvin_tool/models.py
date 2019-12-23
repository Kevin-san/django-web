'''
Created on 2019/11/30

@author: xcKev
'''
from django.db import models

class MenuInfo(models.Model):
    Type=models.CharField(max_length=100,verbose_name='类别')
    Href=models.CharField(max_length=100,verbose_name='链接')
    Text=models.CharField(max_length=100,verbose_name='内容')
    DeleteFlag=models.BooleanField(default=False,blank=False,verbose_name='删除状态')
    submission_user=models.CharField(max_length=30,verbose_name="上传用户")
    submission_date=models.DateTimeField(verbose_name="上传时间")
    class Meta:
        db_table='LessonMenu'
        verbose_name='课程目录'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.Text

class LessonMenuIndexInfo(models.Model):
    Type=models.CharField(max_length=100,verbose_name='类别')
    Href=models.CharField(max_length=100,verbose_name='链接')
    Alt=models.CharField(max_length=100,verbose_name='别名')
    Title=models.CharField(max_length=100,verbose_name='标题')
    Text=models.CharField(max_length=400,verbose_name='内容')
    ImgSrc=models.CharField(max_length=100,verbose_name='图片位置')
    ImgWidth=models.IntegerField(verbose_name='图片宽度')
    ImgHeight=models.IntegerField(verbose_name='图片高度')
    DeleteFlag=models.BooleanField(default=False,blank=False,verbose_name='删除状态')
    submission_user=models.CharField(max_length=30,verbose_name="上传用户")
    submission_date=models.DateTimeField(verbose_name="上传时间")
    class Meta:
        db_table='LessonMenuIndex'
        verbose_name='课程子目录'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.Text
