import requests
from bs4 import BeautifulSoup
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'appmsglist_action_3943274291=card; ua_id=VuIAcdOtBqHnndxyAAAAAPRm13eyIz8IlH4r9QDewpk=; wxuin=21035274672260; mm_lang=zh_CN; personAgree_3943274291=true; poc_sid=HD44mmajmz9IpVJ-uYp95xpFeE-nxndiHFRsykMT; eas_sid=m1B7h2l105H566S4G8A6W0x3o7; pgv_pvid=1641041718; ts_uid=7159249510; pgv_pvi=8892408832; __root_domain_v=.weixin.qq.com; _qddaz=QD.854921634790799; qq_domain_video_guid_verify=91e73a0d41df614c; _qimei_uuid42=18716111f2b100f33d7d0a7d7bb374e937516615c1; _qimei_fingerprint=1568d6407fe894a1b033d02c920f1a3e; _qimei_q36=; _qimei_h38=e1476bec3d7d0a7d7bb374e902000006d18716; rand_info=CAESIIL5XvwMoU/iKfAAEqLL70exkVZbgXBs2RcOy4IEvuHe; slave_bizuin=3943274291; data_bizuin=3943274291; bizuin=3943274291; data_ticket=gDD4tpHsGaqVDhhcl2pywz04komDomP5lNpLdOQVb67nlGCew0yH3uydbvsAZM6X; slave_sid=cjdjNXhLTnVSVlN6Tk9UVXRiYnJiS2ZVQm9UVWFNYTBnbHJra0hYSzZUZUJDR01lNXNveVpiOWdtWGNWVDZ5cTUyQkhSY3JIMDlIcGtteFV5czVKYTVPbm9kd3YyWEpMaTY1TERmaURZSWlWQWpUUHYxemp0dVRjNjJ6UUhzWmVBQzJuTEl2cXB0Y05xMEpm; slave_user=gh_2ddf0452d62c; xid=d0b3a664ea296cf6700de4f363588e9a; _clck=3943274291|1|fod|0; mm_lang=zh_CN; _clsk=yhgbeq|1723780741892|1|1|mp.weixin.qq.com/weheat-agent/payload/record',
    'priority': 'u=0, i',
    'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=10&count=10&token=1505477827&lang=zh_CN',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}
params = (
    ('sub', 'list'),
    ('begin', '0'),
    ('count', '10'),
    ('token', '1505477827'),
    ('lang', 'zh_CN'),
)
content=requests.get('https://mp.weixin.qq.com/cgi-bin/appmsgpublish',headers=headers,params=params).text

soup = BeautifulSoup(content, 'html.parser')  # 或者使用 'html.parser'
print(soup)#cup1=soup.findAll('div',attrs={'class':'publish_content publish_record_history'})
#print(cup1)
#for link in soup.findAll('a'):
    #print(link.get('href'))
#cup1=soup.findAll('div',attrs={'class':'publish_content.publish_record_history'})
#cup2=cup1.findAll('a')
#print(soup.find('publish_list'))
#soup1=BeautifulSoup(content1,'html.parser')
#print(cup1)
#print('********************')
#print(soup1)