import re
str = "I study python3.9 every_day,I love python"

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
print("--------match()--------")
# 匹配字符串"I"
m1 = re.match(r'I',str)
# 匹配字母或数字或下划线
m2 = re.match(r'\w',str)
# 匹配非空白符
m3 = re.match(r'\S',str)
# 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
m4 = re.match(r'.',str)
print(m1.group())
print(m2.group())
print(m3.group())
print(m4.group())

# re.search 扫描整个字符串并返回第一个成功的匹配。
print("--------search()--------")
s1 = re.search(r'study',str)
s2 = re.search(r's\w+',str)
s3 = re.search(r's\S+',str)
s4 = re.search(r's\w*',str)
s5 = re.search(r's\S*',str)
# 使用了()进行分组
s6 = re.search(r'I (s\S+)',str)

print(s1.group())
print(s2.group())
print(s3.group())
print(s4.group())
print(s5.group())
print(s6.group(1))

# re.findall 查找全部符合匹配的字符串
print("--------findall()--------")
f1 = re.findall(r'python',str)
f2 = re.findall(r'p\w+',str)
f3 = re.findall(r'p\S+',str)
f4 = re.findall(r'p\D+',str)
f5 = re.findall(r'p.+9',str)

# +表示重复一次或多次，即只匹配"p"后面1个或多个任意字符
f6 = re.findall(r'p.+\d',str)
# *表示重复零次或多次，即匹配"p"后面0或多个任意字符
f7 = re.findall(r'p.*\d',str)
# ?表示重复零次或一次，即只匹配"p"后面一个任意字符
f8 = re.findall(r'p.?',str)
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
print(f6)
print(f7)
print(f8)

# re.sub 替换字符串
print("--------sub()--------")
su1 = re.sub(r'every_day',r'EVERY_DAY',str)
su2 = re.sub(r'e\w+',r'EVERY_DAY',str)
print(su1)
print(su2)


print("--------test--------")
str1 = '<div><a class="title" href="www.bjsxt.com">尚学堂beijingsxt_123</a></div>'
str2 = '<div><a class="title" href="www.bjsxt.com">尚学堂</a></div><div><p>这是一个测试</p></div>'
t1 = re.findall(r'尚学堂beijingsxt_123',str1)
t2 = re.findall(r'[\u4e00-\u9fa5]+\w+',str1)
t3 = re.findall(r'<a class="title" href="www.bjsxt.com">(.*)</a>',str1)

# 把所有的div换成span标签
t4 = re.sub(r'div',r'span',str2)
# 把所有的含有<a>标签的div换成span标签
t5 = re.sub(r'<div>(<a .+a>)</div>',r'<span>\1</span>',str2)


print(t1)
print(t2)
print(t3)
print(t4)
print(t5)