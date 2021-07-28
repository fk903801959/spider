import json

str = '{"name":"盗梦空间"}'

# loads把Json格式字符串解码转换成Python对象
obj = json.loads(str)
print(obj) # obj类型为一个python对象

# dumps把一个Python对象编码转换成Json字符串(注意：json.dumps() 序列化时默认使用的ascii编码，添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码)
obj_str1 = json.dumps(obj)
obj_str2 = json.dumps(obj,ensure_ascii=False)
print(obj_str1) # obj_str1类型为一个json字符串
print(obj_str2) # obj_str2类型为一个json字符串

# dump将Python内置类型序列化为json对象后写入文件
json.dump(obj,open("movie.json","w",encoding="UTF-8"),ensure_ascii=False)

# load读取文件中json形式的字符串元素 转化成python类型
movie_list = json.load(open("movie.json",encoding="UTF-8"))
print(movie_list)