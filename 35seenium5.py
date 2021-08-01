from  selenium import webdriver
from lxml import etree
from time import sleep
# 配置浏览器驱动的相关参数
options = webdriver.ChromeOptions()
# options.add_argument('--headless') #无头浏览
options.add_argument('--blink-settings=imagesEnable=false') #不加载图片
chrome = webdriver.Chrome(options=options)

# 获取指定url
chrome.get('https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&spm=2.1.0')
# 将下拉框拉到底端，有助于加载显示整个页面
js = 'document.documentElement.scrollTop=10000'
chrome.execute_script(js) # 执行js脚本，将下拉框拉到底端
sleep(6) # 需停顿一段时间，等待页面渲染完成再获取页面元素
html = chrome.page_source # 此时再获取页面元素，注意与前面语句的先后顺序

e = etree.HTML(html)
links = e.xpath("//div[@class='p-name p-name-type-2']/a/@href") # 笔记本链接地址
prices = e.xpath("//div[@class='gl-i-wrap']/div[@class='p-price']/strong/i/text()") # 笔记本价格

for link,price in zip(links,prices):
    print(link,":",price)

print('共获取到',len(prices),'数据')
