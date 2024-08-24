from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 指定Edge WebDriver的路径
# 注意：这里你需要替换为你的Edge WebDriver的实际路径
service = Service(executable_path='D:\\edgedriver_win64\\msedgedriver.exe')

# 创建Edge WebDriver的实例
driver = webdriver.Edge(service=service)

try:
    # 打开Google主页
    driver.get("https://www.baidu.com")

    # 验证网页标题是否为"Google"
    # 注意：这里的标题可能会根据你的地区和语言设置而有所不同
    assert "百度一下，你就知道" in driver.title, "网页标题不是预期的'baidu'"

    print("测试成功，网页标题验证通过！")

finally:
    # 关闭浏览器
    driver.quit()