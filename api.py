'''
Author: Thund1r thund1r@foxmail.com
Date: 2022-09-22 14:16:12
LastEditTime: 2022-10-03 04:31:16
Description: API数据

Copyright (c) 2022 by Thund1r thund1r@foxmail.com, All Rights Reserved. 
'''
# -*- coding: utf8 -*-
from datetime import date, datetime, timedelta
import requests
import config
import re
import random
import math

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

# 获取天行彩虹屁
def get_chp():
    if not tianhang_chp:
        return None
    try:
        chp_url = f"http://api.tianapi.com/caihongpi/index?key={tianhang_chp}"
        chp_res = requests.get(chp_url).json()
        return "🌈 " + chp_res["newslist"][0]["content"]
    except Exception as e:
        print("获取彩虹屁数据错误，请检查是否正确填写天行Key，是否申请彩虹屁接口:", e)
        return None

# 获取天行彩虹屁----1
def get_chp1():
    if not pyqmeiju:
        return None
    try:
        chp_url = f"http://api.tianapi.com/caihongpi/index?key={pyqmeiju}"
        chp_res = requests.get(chp_url).json()
        return "🌈 " + chp_res["newslist"][0]["content"]
    except Exception as e:
        print("获取彩虹屁数据错误，请检查是否正确填写天行Key，是否申请彩虹屁接口:", e)
        return None

# 彩虹屁接口---shadiao api
def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

# 朋友圈文案api接口--shadiao api
def get_words1():
  words1 = requests.get("https://api.shadiao.pro/pyq")
  if words1.status_code != 200:
    return get_words1()
  return words1.json()['data']['text']

# 天行数据--天气接口
def get_weather1():
    if not city:
        return None
    try:
        url = f"https://api.tianapi.com/tianqi/index?key={tianhang_tq2}&city={city}"
        res1 = requests.get(url).json()
        muzi = res1['newslist'][0]
        return muzi['area'], muzi['weather'], muzi['real'], muzi['lowest'], muzi['highest'], muzi['wind'], muzi['windsc'], muzi['tips'], muzi['week'], muzi['sunrise'], muzi['sunset'], muzi['humidity']
    except Exception as s:
        print("获取天行数据天气接口错误", s)
        return None

#pm25接口
def get_weather3():
    if not city:
        return None
    try:
       url = f"http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city={city}"
       res1 = requests.get(url).json()
       muzi1 = res1['data']['list'][0]
       return math.floor(muzi1['pm25'])
    except Exception as e:
        print("获取pm25数据接口异常", e)
        return None

#农历接口api获取
def get_lunar_calendar():
    if not tianhang_nl:
        return None
    try:
        date = today.strftime("%Y-%m-%d")
        url = f"http://api.tianapi.com/lunar/index?key={tianhang_nl}&date={date}"
        lunar_calendar = requests.get(url, verify=False).json()
        res3 = lunar_calendar['newslist'][0]
        return res3['lubarmonth'], res3['lunarday'], res3['jieqi'], res3['lunar_festival'], res3['festival']
    except Exception as e:
        print('获取天行农历接口数据测完', e)
        return  None
# def get_lunar_calendar():
#   date = today.strftime("%Y-%m-%d")
#   url = "http://api.tianapi.com/lunar/index?key=d5edced4967c76fd11899dbe1b753d91&date=" + date
#   lunar_calendar = requests.get(url,verify=False).json()
#   res3 = lunar_calendar['newslist'][0]
#   return res3['lubarmonth'],res3['lunarday'],res3['jieqi'],res3['lunar_festival'],res3['festival']


# 获取随机图片链接数据
# 来自搏天API:https://api.btstu.cn/
def get_random_pic():
    p_type_list = pictype_list
    p_type = "fengjing"
    if p_type_list and isinstance(p_type_list, list):
        p_type = random.choice(p_type_list)
    try:
        pic_url = f"https://api.btstu.cn/sjbz/api.php?format=json&lx={p_type}"
        pic_res = requests.get(pic_url).json()["imgurl"]
        return pic_res
    except Exception as e:
        print("获取随机图片数据错误:", e)
        return None


# 获取bing每日壁纸数据
def get_bing():
    try:
        bing_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        bing_res = requests.get(bing_url).json()
        bing_pic = "https://cn.bing.com/" + bing_res["images"][0]["url"]
        bing_title = bing_res["images"][0]["title"]
        bing_content = re.sub(
            "\\(.*?\\)", "", bing_res["images"][0]["copyright"])
        bing_tip = f"{bing_title}——{bing_content}"
        return {
            "bing_pic": bing_pic,
            "bing_tip": bing_tip
        }
    except Exception as e:
        print("获取必应数据错误:", e)
        return None


# 获取金山词霸数据
def get_ciba():
    try:
        ciba_url = "http://open.iciba.com/dsapi/"
        ciba_res = requests.get(ciba_url).json()
        ciba_en = ciba_res["content"]
        ciba_zh = ciba_res["note"]
        ciba_pic = ciba_res["fenxiang_img"]
        ciba_tip = f"🔤 {ciba_en}\n🀄️ {ciba_zh}"
        return {
            "ciba_tip": ciba_tip,
            "ciba_pic": ciba_pic
        }
    except Exception as e:
        print("获取金山词霸数据错误:", e)
        return None


# 获取ONE一个图文数据
def get_one():
    try:
        one_url = "https://apier.youngam.cn/essay/one"
        one_res = requests.get(one_url).json()['dataList'][0]
        one_id = "VOL."+one_res['id']
        one_pic = one_res['src']
        one_tip = f"✒️ {one_id} {one_res['text']}"
        return {
            "one_pic": one_pic,
            "one_tip": one_tip
        }
    except Exception as e:
        print("获取ONE一个图文数据错误:", e)
        return None


# # 获取XXX自定义图片与文字
# def get_XXX():
#     try:
#         XXX_url = "https://XXXX.XXX"
#         XXX_res = requests.get(XXX_url).json()
#         print("获取XXX自定义图片与文字json数据:", XXX_res)
#         XXX_item0 = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_item1 = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_pic = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_tip = "✒️ " + XXX_item0 + "\n" + "🗓️ " + XXX_item1
#         res = {
#             # 没有图片就删除下面这一句
#             "XXX_pic": XXX_pic,
#             "XXX_tip": XXX_tip
#         }
#         print("获取XXX数据:", res)
#         return res
#     except Exception as e:
#         print("获取XXX数据错误:", e)
#         return None