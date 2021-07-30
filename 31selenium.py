import time
from selenium import webdriver

# 构造浏览器
chrome = webdriver.Chrome()

# 发送请求，访问url
url = 'https://www.baidu.com'
chrome.get(url)

# 截图
chrome.save_screenshot('screen_shot/baidu.png')

# 获取源代码
html = chrome.page_source
print(html)

# 自动关闭浏览器
time.sleep(5)
chrome.quit()
