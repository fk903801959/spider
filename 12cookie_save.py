# cookielib 模块的主要作用是提供可存储 cookie 的对象，以便于与 urllib 模块配合使用来访问 Internet 资源。
# Cookielib 模块非常强大，我们可以利用本模块的 CookieJar 类的对象来捕获 cookie 并在后续连接请求时重新发送，比如模拟登录功能。
# 该模块主要的对象有 CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
# 它们的关系：CookieJar —— 派生 ——>FileCookieJar —— 派生 ——->MozillaCookieJar 和 LWPCookieJar

from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar

# 伪造客户端环境
ua = UserAgent(path='json/fake_useragent_0.1.11.json')
headers = {"User-Agent": ua.random}


# 记录cookie信息，并以txt文件的形式进行保存
def get_cookie():
    login_url = "http://127.0.0.1:8000/student/tologin/"

    # 用户登录名和密码，用字典形式保存
    form_data = {
        "sname": "zhangsan",
        "spwd": "123456"
    }

    # 创建一个MozillaCokieJar实例对象,用于存储cookie数据
    cookie_jar = MozillaCookieJar()
    # 根据创建的cookie实例对象生成cookie的管理器
    cookie_handler = HTTPCookieProcessor(cookie_jar)

    request = Request(login_url, headers=headers, data=urlencode(form_data).encode())
    opener = build_opener(cookie_handler)
    opener.open(request)

    #保存cookie文件：
    # save()函数带有两个参数，ignore_discard和ignore_expires。
    # ignore_discard:  即保存需要被丢弃的cookie。
    # ignore_expires:  即过期的cookie也保存。
    cookie_jar.save('cookie/stu_cookie.txt',ignore_discard=True,ignore_expires=True)

#使用已保存的cookie信息，进行登录访问操作
def use_cookie():
    info_url="http://127.0.0.1:8000/student/tologin/stu_index"
    request = Request(info_url,headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load('cookie/stu_cookie.txt',ignore_discard=True,ignore_expires=True)
    cookie_handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(cookie_handler)
    response = opener.open(request)
    print(response.read().decode())

if __name__ == "__main__":
    get_cookie()
    use_cookie()