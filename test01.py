from fake_useragent import UserAgent
import requests
from lxml import etree
from time import sleep

# 获取指定url地址的页面信息
def get_html(url):
    headers = {'User-Agent':UserAgent().chrome}
    resp = requests.get(url,headers=headers)
    sleep(3)
    # 如果状态码为200，即页面信息返回成功
    if resp.status_code == 200:
        # 返回的是中文页面，页面信息使用utf-8编码
        resp.encoding = 'utf-8'
        return resp.text
    else:
        print("页面信息获取失败！")
        return None


def parse_index(html):
    e = etree.HTML(html)
    name = e.xpath("//div[@class='name']/a/text()")
    return name

def write_file(model_list,page):
    with open('model_list.txt','a',encoding='utf-8') as f:
        f.write(page)
        f.write(str(model_list))
        print(page,'获取成功！')

def main():
    num = int(input("请输入你要获取的页数："))
    for page in range(num):
        url = 'https://www.t2u.cc/starrings/{}'.format(page+1)
        info_html = get_html(url)
        sleep(2)
        model_list = parse_index(info_html)
        thepage = '页数：{}'.format(page+1)
        write_file(model_list,thepage)

if __name__ == '__main__':
    main()