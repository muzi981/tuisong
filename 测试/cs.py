
import requests

# yqcity_list = config.get_list("yqcity")
yqcity_list = ['合肥', '六安']

# 获取城市疫情数据
def get_yq(city_3):
    try:
        res = requests.get(
            f'https://covid.myquark.cn/quark/covid/data/index_data?format=json&method=Huoshenshan.ncov2022&city={city_3}').json()['data']
        if len(res['cityData']) == 0:
            res['cityData'] = res['provinceData']
        yq_res_list = [
            {"desc": "🤒 新增确诊/无症状",
                "detail": str(res['cityData']["sure_new_loc"])+"/" + str(res['cityData']["sure_new_hid"])},
            {"desc": "😷 现有确诊",
                "detail": res['cityData']["present"]},
            {"desc": "⛔️ 中/高风险区",
                "detail": str(res['cityData']["danger"]["1"]) + "/" + str(res['cityData']["danger"]["2"])}
        ]
        yq_tip_list = []
        yq_tip_list.append(f'🏥 {city_3}疫情（{(res["time"][4:])}）')
        for item in yq_res_list:
            yq_tip_list.append(item['desc'] + "：" + str(item['detail']))
        yq_tip = '\n'.join(yq_tip_list)
        return yq_tip
    except Exception as e:
        print("获取疫情数据错误：", e)
        return None

# m = map(get_yq, yqcity_list)
# print(m)

# 获取所有疫情数据
def get_map_yq():
    if yqcity_list:
        map_yq_tip = None
        yq_list = list(map(get_yq, yqcity_list))
        yq_list = list(filter(None, yq_list))
        # print(yq_list+'1')
        # print(yq_list)
        if yq_list:
            map_yq_tip = "\n".join(yq_list)
        return map_yq_tip
    else:
        print("没有填写疫情数据城市")
        return None
print(get_map_yq())


info_list = []
multi_list = []
# pic_type = pictype
# own_link = link
# own_pic = diy.get_my_pic()
# own_title = diy.get_my_title()
# own_content = diy.get_my_content()

# print(get_map_yq())
# 加入疫情数据
#     yq_tip = get_map_yq()
#     if yq_tip:
#         info_list.append(yq_tip)
#         multi_list.append(handle_multi(
#             yq_tip, "COVID-19", yq_tip, None, None))

