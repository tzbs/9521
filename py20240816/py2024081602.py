# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
import math
import random

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",
]

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
#cookie = "appmsglist_action_3943274291=card; ua_id=VuIAcdOtBqHnndxyAAAAAPRm13eyIz8IlH4r9QDewpk=; wxuin=21035274672260; mm_lang=zh_CN; personAgree_3943274291=true; poc_sid=HD44mmajmz9IpVJ-uYp95xpFeE-nxndiHFRsykMT; eas_sid=m1B7h2l105H566S4G8A6W0x3o7; pgv_pvid=1641041718; ts_uid=7159249510; pgv_pvi=8892408832; __root_domain_v=.weixin.qq.com; _qddaz=QD.854921634790799; qq_domain_video_guid_verify=91e73a0d41df614c; _qimei_uuid42=18716111f2b100f33d7d0a7d7bb374e937516615c1; _qimei_fingerprint=1568d6407fe894a1b033d02c920f1a3e; _qimei_q36=; _qimei_h38=e1476bec3d7d0a7d7bb374e902000006d18716; rand_info=CAESIIL5XvwMoU/iKfAAEqLL70exkVZbgXBs2RcOy4IEvuHe; slave_bizuin=3943274291; data_bizuin=3943274291; bizuin=3943274291; data_ticket=gDD4tpHsGaqVDhhcl2pywz04komDomP5lNpLdOQVb67nlGCew0yH3uydbvsAZM6X; slave_sid=cjdjNXhLTnVSVlN6Tk9UVXRiYnJiS2ZVQm9UVWFNYTBnbHJra0hYSzZUZUJDR01lNXNveVpiOWdtWGNWVDZ5cTUyQkhSY3JIMDlIcGtteFV5czVKYTVPbm9kd3YyWEpMaTY1TERmaURZSWlWQWpUUHYxemp0dVRjNjJ6UUhzWmVBQzJuTEl2cXB0Y05xMEpm; slave_user=gh_2ddf0452d62c; xid=d0b3a664ea296cf6700de4f363588e9a; _clck=3943274291|1|fod|0; mm_lang=zh_CN; _clsk=yhgbeq|1723780741892|1|1|mp.weixin.qq.com/weheat-agent/payload/record"
cookie='appmsglist_action_3943274291=card; ua_id=VuIAcdOtBqHnndxyAAAAAPRm13eyIz8IlH4r9QDewpk=; wxuin=21035274672260; mm_lang=zh_CN; personAgree_3943274291=true; poc_sid=HD44mmajmz9IpVJ-uYp95xpFeE-nxndiHFRsykMT; eas_sid=m1B7h2l105H566S4G8A6W0x3o7; pgv_pvid=1641041718; ts_uid=7159249510; pgv_pvi=8892408832; __root_domain_v=.weixin.qq.com; _qddaz=QD.854921634790799; qq_domain_video_guid_verify=91e73a0d41df614c; _qimei_uuid42=18716111f2b100f33d7d0a7d7bb374e937516615c1; _qimei_fingerprint=1568d6407fe894a1b033d02c920f1a3e; _qimei_q36=; _qimei_h38=e1476bec3d7d0a7d7bb374e902000006d18716; rand_info=CAESIIL5XvwMoU/iKfAAEqLL70exkVZbgXBs2RcOy4IEvuHe; slave_bizuin=3943274291; data_bizuin=3943274291; bizuin=3943274291; data_ticket=gDD4tpHsGaqVDhhcl2pywz04komDomP5lNpLdOQVb67nlGCew0yH3uydbvsAZM6X; slave_sid=cjdjNXhLTnVSVlN6Tk9UVXRiYnJiS2ZVQm9UVWFNYTBnbHJra0hYSzZUZUJDR01lNXNveVpiOWdtWGNWVDZ5cTUyQkhSY3JIMDlIcGtteFV5czVKYTVPbm9kd3YyWEpMaTY1TERmaURZSWlWQWpUUHYxemp0dVRjNjJ6UUhzWmVBQzJuTEl2cXB0Y05xMEpm; slave_user=gh_2ddf0452d62c; xid=d0b3a664ea296cf6700de4f363588e9a; _clck=3943274291|1|fod|0; mm_lang=zh_CN; _clsk=mev6h9|1723817352089|2|1|mp.weixin.qq.com/weheat-agent/payload/record'
# 使用Cookie，跳过登陆操作

data = {
    "token": "1505477827",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    #"fakeid": "",
    "type": "9",
}
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",

}
content_json = requests.get(url, headers=headers, params=data).json()
count = int(content_json["app_msg_cnt"])
print(count)
page = int(math.ceil(count / 5))
print(page)
content_list = []
# 功能：爬取IP存入ip_list列表

for i in range(page):
    data["begin"] = i * 5
    user_agent = random.choice(user_agent_list)
    headers = {
        "Cookie": cookie,
        "User-Agent": user_agent,

    }
    ip_headers = {
        'User-Agent': user_agent
    }
    # 使用get方法进行提交
    # 返回了一个json，里面是每一页的数据
    for item in content_json["app_msg_list"]:
        # 提取每页文章的标题及对应的url
        items = []
        items.append(item["title"])
        items.append(item["link"])
        t = time.localtime(item["create_time"])
        items.append(time.strftime("%Y-%m-%d %H:%M:%S", t))
        content_list.append(items)
    print(i)
    if (i > 0) and (i % 10 == 0):
        name = ['title', 'link', 'create_time']
        test = pd.DataFrame(columns=name, data=content_list)
        test.to_csv("url.csv", mode='a', encoding='UTF-8')
        print("第" + str(i) + "次保存成功")
        content_list = []
        time.sleep(random.randint(60, 90))
    else:
        time.sleep(random.randint(15, 25))

name = ['title', 'link', 'create_time']
test = pd.DataFrame(columns=name, data=content_list)
test.to_csv("url.csv", mode='a', encoding='UTF-8')
print("最后一次保存成功")