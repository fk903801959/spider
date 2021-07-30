from selenium import webdriver
import time

# 构造chrome驱动浏览器
chrome = webdriver.Chrome()

url = 'https://cn.bing.com/'
# 在当前的浏览器中加载url对应的页面
chrome.get(url)

# 通过id找到搜索框标签，并调用send_keys方法向搜索框中传入值
chrome.find_element_by_id('sb_form_q').send_keys('python')

# 通过id找到搜索按钮Input标签，并调用click()方法进行点击操作
chrome.find_element_by_id('sb_form_go').click()

# 点击玩搜索按钮后，浏览器向服务器发送请求，然后接收从服务器发来的响应包，并把html文件渲染到浏览器页面上，渲染到过程会占用一定时间。
# 为了保证渲染完全，故需调用sleep()方法等待浏览器先完成页面渲染。
time.sleep(3)

# 获取进行搜索操作后的网页源代码并将其打印出来
html= chrome.page_source
print(html)

# 退出浏览器驱动程序
chrome.quit()
