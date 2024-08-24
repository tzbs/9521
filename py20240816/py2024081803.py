from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
driver = webdriver.Chrome(executable_path='D:\\edgedriver_win64\\msedgedriver.exe')

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

try:
    # 打开微信网页版（这里以Chrome为例，根据实际情况可能需要调整为Edge）
    #driver.get('https://wx.qq.com/')
    content = driver.get('https://mp.weixin.qq.com/cgi-bin/appmsgpublish', headers=headers, params=params).text

    # 登录微信（这里省略具体登录步骤，需要根据你的账号情况实现）
    # ...

    # 导航到公众号（同样省略具体步骤）
    # ...

    # 抓取图文信息（假设图文信息在某个可识别的元素中）
    # 示例：获取第一个图文的标题和链接
    articles = driver.find_elements(By.CSS_SELECTOR, '你的文章列表CSS选择器')
    if articles:
        first_article = articles[0]
        title = first_article.find_element(By.CSS_SELECTOR, '你的文章标题CSS选择器').text
        link = first_article.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # 点击链接并抓取文章内容（这里也省略具体步骤）
        # ...

        print(f"Title: {title}, Link: {link}")

finally:
    # 关闭浏览器
    driver.quit()