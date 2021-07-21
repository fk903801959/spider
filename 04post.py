from urllib.request import urlopen,Request
from urllib.parse import urlencode

url = "https://www.bjsxt.com/wp-login.php"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"}


args={
    "log":"fk903801959",
    "pwd":"123456"
}
f_data = urlencode(args)

#Request请求对象的里有data参数，它就是用在POST里的，我们要传送的数据就是这个参数data，data是一个字典，里面要匹配键值对
request = Request(url, headers=headers, data=f_data.encode()) # 注意使用urlencode生成的字符串还需要通过encode编码成字节流再传入data中
response = urlopen(request)
print(response.read().decode())