from urllib.request import urlopen

#要访问的地址
url = 'http://www.baidu.com/'

#发送请求
response = urlopen(url)

#读取内容
info = response.read()

#打印内容
# print(info.decode())


#返回HTTP的响应码
print(response.getcode())

#返回实际访问的url
print(response.geturl())

#返回HTTP响应的报头
print(response.info())