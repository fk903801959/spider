#本次实验需注意事项
#1、最好用自搭建的服务器网站进行实验，因实验条件较为特殊
#2、模拟的是一个特殊的用户登录环境，要求是进行form表单提交且提交方式为post，明文提交
#3、由于大多数网站对于post请求都自带csrf码防跨站伪请求，可在djgon服务器环境中将配置文件中的
# django.middleware.csrf.CsrfViewMiddleware一栏注释掉，默认不启用csrf认证。

from urllib.request import Request,build_opener,HTTPCookieProcessor
from fake_useragent import UserAgent
from urllib.parse import urlencode
#用户登录主页面地址
login_url = "http://127.0.0.1:8000/student/tologin/"

#用户登录名和密码，用字典形式保存
form_data = {
    "sname":"zhangsan",
    "spwd":"123456"
}
# 伪造客户端环境
ua = UserAgent(path='json/fake_useragent_0.1.11.json')
headers = {
    "User-Agent":ua.random
}

# 根据创建的cookie生成cookie的管理器，若参数为空，则默认自动创建一个cookiejar实例对象用于临时存储cookie
cookie_handler = HTTPCookieProcessor()

request = Request(login_url,headers=headers,data=urlencode(form_data).encode())
opener = build_opener(cookie_handler)
response = opener.open(request)


# 登录页面跳转
user_url = "http://127.0.0.1:8000/student/tologin/stu_index"
request = Request(user_url,headers=headers)
response2 = opener.open(request)

print(response2.read().decode())