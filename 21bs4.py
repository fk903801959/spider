# Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，
# 因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
# 你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

#Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种
# Tag（标签）、NavigableString（内容）、BeautifulSoup（文档中的全部内容）、Comment（存在注释符的特殊内容）

from bs4 import BeautifulSoup
from bs4.element import Comment

html = '''
<title id='title'>尚学堂</title>
<div class='info1' float='left'>Welcome SXT</div>
<div class='info2' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!---没用---></strong>
</div>
<div class='info2'>
    This is a test.
</div>
'''
# 创建一个BS4的对象，解析器选择lxml
soup = BeautifulSoup(html,'lxml')
# BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
print(soup.name)

# 常规方法，利用soup获取符合要求的的第一个标签、属性和内容
# 获取标签
print("---获取标签---")
print(soup.title)
print(soup.div)
print(soup.span)

# 获取属性
print("---获取标签中的属性---")
print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a['href'])

# 获取内容
print("---获取标签中的文本内容---")
print(soup.title.string)
print(soup.title.text)
print(soup.strong.string)
print(soup.strong.text)

if type(soup.strong.string) == Comment:
    print("有注释,注释为：")
    # 将注释内容原样包括标签一起输出
    print(soup.strong.prettify())
else:
    print(soup.strong.string)

print("---搜索方法的介绍——过滤器---")
# 搜索方法，匹配查找符合特定条件的元素
# 常用过滤器：字符串、正则表达式、列表、keyword、True、CSS搜索,属性搜索


print("字符串：")
#返回所有div标签，用逗号隔开
print(soup.find_all('div'))

print("按CSS搜索：")
# 从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
print(soup.find_all(class_='info2'))

print("按属性搜索：")
#返回id为title的元素
print(soup.find_all(attrs={"id":"title"}))
#返回所有title标签中，id为title的元素
print(soup.find_all('title',attrs={"id":"title"}))

print("---css选择器---")
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('.info1'))
print(soup.select('div span'))
print(soup.select('div.info2 a'))