# https用白话来解释就是我们的http+ssl（证书），有一些小公司的SSL都是自己去做出来的，
# 所以有的时候我们访问一些小公司的网址的时候它会提醒我们去下载某些ssl证书，而那些不用去下载的网址说明已经通过了CA认证
from urllib.request import urlopen,Request
import ssl

url = "https://dongguan.zbj.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"}

request = Request(url,headers=headers)
#导入ssl包来进行忽略证书认证
context = ssl._create_unverified_context()

response = urlopen(request,context=context)
print(response.read().decode())