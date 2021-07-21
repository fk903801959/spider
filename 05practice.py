#该实例可用于获取百度贴吧的指定吧名和其对应的页面信息
from urllib.request import urlopen,Request
from urllib.parse import quote

#获取网页信息
def get_html(url):
    #封装请求头部信息，使用伪造的客户端浏览器软件软件环境
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"}
    #封装一个Request请求对象
    request = Request(url,headers=headers)
    #使用urlopen方法发出请求包，并将从服务器返回到响应包赋值给response对象
    response = urlopen(request)
    #返回解码后的响应包
    return response.read().decode()

#保存网页
def save_html(html,filename):
    # 使用文件的写操作，指定编码格式为utf-8，创建一个用于存储页面信息的html页面
    with open('web/{}'.format(filename), 'w', encoding='utf-8') as f:
        #将获取到的html页面信息写入对应的html文件中
        f.write(html)


def main():
    content = input("请输入要获取的贴吧名称：")
    num = int(input("请输入要获取的贴吧页数："))
    #根据百度贴吧的页数规律，使用for函数来连续获取相应页面的响应信息
    for i in range(num):
        url = "https://tieba.baidu.com/f?kw='{}'&ie=utf-8&pn={}".format(quote(content),'i*50')
        # 传递url来调用获取页面信息的方法，并将结果赋值给html对象
        html= get_html(url)
        # 使用filename对象来记录不同页面的存储文件名称
        filename = content+"_第" + str(i+1) + "页.html"
        # 传递html和filename来调用保存页面信息的方法
        save_html(html,filename)

if __name__ == '__main__':
    main()