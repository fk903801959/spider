from urllib.request import urlopen,Request
from urllib.parse import quote,urlencode


url = "http://www.baidu.com/"
url1 = "https://www.baidu.com/s?wd=python"

# 搜索字符为中文汉字时可以使用quote或urlencode方法进行编码转换
# 这是通过quote方法进行转码,适用于仅编码wd为汉字的情况
url2 = "https://www.baidu.com/s?wd={}".format(quote("尚学堂"))

# 使用urlencode方式转码，需创建一个字典对象，字典中的键值对通过urlencode方法调用后，自动用&连接。
args={
    "wd":"知乎",
    "ie":"utf-8"
}
url3 = "https://www.baidu.com/s?{}".format(urlencode(args))

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"}

request = Request(url3, headers=headers)
response = urlopen(request)
print(response.read().decode())