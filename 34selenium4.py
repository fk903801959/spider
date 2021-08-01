from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless') # 不显示浏览器窗口界面
options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome = webdriver.Chrome(options=options)
# 本次实例为收集虎牙直播中lol游戏相关的直播间信息
chrome.get('https://www.huya.com/g/lol')

while True:
    names = chrome.find_elements_by_class_name('title')
    counts = chrome.find_elements_by_class_name('js-num')
    # 将页面中收集到的直播间名称和观看人数信息依次打印出来
    for name,count in zip(names,counts):
        print(name.text,":",count.text)

    # 对当前网页元素进行字符串查找，若没有'laypage_next'字符串，即没有“下一页”按钮标签，则认为已经到达页底，此时需打破循环，停止信息收集。
    # 补充知识点：driver.page_source.find('字符串') 查找失败： -1
    if chrome.page_source.find('laypage_next') != -1:
        chrome.find_element_by_class_name('laypage_next').click() # 通过类名找到“下一页”标签按钮，并进行点击操作。
        sleep(3)
    else:
        break