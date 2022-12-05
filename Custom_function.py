'''
Author: Thund1r thund1r@foxmail.com
Date: 2022-09-22 14:16:12
LastEditTime: 2022-10-03 04:31:16
Description: 自定义函数

Copyright (c) 2022 by Thund1r thund1r@foxmail.com, All Rights Reserved. 
'''
# -*- coding: utf8 -*-
from datetime import date, datetime, timedelta
from zhdate import ZhDate as lunar_date
from borax.calendars.lunardate import LunarDate
import requests
import config
import re
import random

pictype_list = config.get_list("pictype")
tian = config.get("tian")
today = datetime.now() + timedelta(hours=8)
start_date = config.get('start_date')
birthday = config.get('birthday')
city = config.get('city')
tianhang_chp = config.get('tianhang_chp')
pyqmeiju = config.get('pyqmeiju')
tianhang_tq = config.get('tianhang_tq')
tianhang_tq2 = config.get('tianhang_tq2')
tianhang_nl = config.get('tianhang_nl')



#------------------------------------------------------生日模块--------------------------------------------------------------
#切片获取年月日
n = int(birthday[0:4:1])
y = int(birthday[5:7])
r = int(birthday[8:])
# 农历转阳历
date1 = lunar_date(n, y, r)
#农历日期转换称公历日期.将公里日期输出为字符串
dt_str = date1.to_datetime().strftime('%Y-%m-%d')# 2020-08-25 00:00:00，农历转换成阳历日期  datetime 类型

# 生日-----------支持农历生日倒计时
# 1、倒计时函数实现方式一：
def get_birthday_l():
  next = date1.to_datetime()
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

# 2、倒计时函数实现方式二：
def get_birthday_m():
  next = datetime.strptime(dt_str, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

# 3、倒计时函数实现方式三：
year = LunarDate.today().year  #LunarDate.today().year  获取当前年份
birthday1 = LunarDate(year, y, r)#构建农历日期
birthday2 = birthday1.to_solar_date()#转化成公历日期，输出为字符串
def get_birthday_s():
  next = datetime.strptime(birthday2.strftime("%Y-%m-%d"), "%Y-%m-%d")#先转换成datetime.date类型,再转换成datetime.datetime
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days



# -----------------------------------------------随机颜色函数---------------------------------------
# 随机颜色2
def get_random_color():
  colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  color = ""
  for i in range(6):
      color += colorArr[random.randint(0,14)]
  return "#"+color


# -----------------------------------------------相恋时间函数---------------------------------------
def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days