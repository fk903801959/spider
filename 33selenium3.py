from selenium import webdriver
from time import sleep

# 隐藏浏览器窗口界面
def headless():
    # 创建一个chrome的参数对象
    options = webdriver.ChromeOptions()
    # 在参数对象中添加属性"--headless",意为不显示浏览器窗口界面
    options.add_argument('--headless')
    # 配置浏览器驱动chrome对象的参数
    chrome = webdriver.Chrome(options=options)
    chrome.get('https://www.baidu.com')
    # 停止一段时间，等待浏览器将页面渲染完成。
    sleep(3)
    print(chrome.page_source)
    chrome.quit()

# 使用ip代理
def proxy():
    # 创建一个chrome的参数对象
    options = webdriver.ChromeOptions()
    # 在参数对象中添加属性"--proxy--server",意为不显示浏览器窗口界面
    options.add_argument('--proxy-server=http://47.107.128.69:888')
    # 配置浏览器驱动chrome对象的参数
    chrome = webdriver.Chrome(options=options)
    chrome.get('http://httpbin.org/get')
    # 停止一段时间，等待浏览器将页面渲染完成。
    sleep(3)
    print(chrome.page_source)
    chrome.quit()

def main():
    proxy()

if __name__ == '__main__':
    main()