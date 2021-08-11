from pymongo import MongoClient

# 获取连接数据对象
client = MongoClient() # client = MongoClient(host, port),默认为client = MongoClient('localhost', '27017')
# 获取数据库实例
sanguo = client.sanguo
# 获取集合实例
General = sanguo.General
# 操作集合

# 查找操作
def do_find():
    print("\033[1;31m--------1、基本查找--------\033[0m")
    generals = General.find()
    # print(generals) # 打印出的是一个游标对象
    # print(generals.next()) # 使用next方法移动游标，将文档一个一个打印出来
    for general in generals: # 使用for循环打印游标内所有的文档对象
        print(general)

    print("\033[1;31m--------2、条件查找--------\033[0m")
    # 注意：在mongoshell中操作时，key值可不加引号，但在python中必须加上引号，以表明其为一个字典对象
    general = General.find_one({"country":"魏国"}) # collection.find_one()找到集合中符合条件的第一条文档数据
    general2 = General.find({"country":"吴国"}) # collection.find()找到集合中符合条件的所有文档数据

    print('\033[1;34mfind_one():\033[0m')
    print(general)

    print('\033[1;34mfind():\033[0m')
    for general in general2:
        print(general)

    # 注意：原先用来统计集合内文档数的collection.find().count()已经被弃用
    # 现在使用collection.count_documents({})来统计集合内的文档数，注意参数中一定要加过滤器{}，过滤器中为空，默认统计全部文档数。
    print('\033[1;34mcount_documents({}):\033[0m')
    num = General.count_documents({})
    print(num)

    #通过skip().limit()筛选特定位置的文档数据
    print('\033[1;34mskip().limit():\033[0m')
    weiguo_generals = General.find().skip(4).limit(3)
    for general in weiguo_generals:
        print(general)

# 插入操作
def do_save():
    print("\033[1;31m--------插入文档--------\033[0m")
    print('\033[1;34minsert():\033[0m')
    General.insert_one({"name":"鲁肃","country":"吴国"}) #insert()方法已过时，推荐使用insert_one或insert_many来插入文档数据。
    print("文档数据插入成功！")

# 更新操作
def do_update():
    print("\033[1;31m--------更新文档--------\033[0m")
    print('\033[1;34mupdate():\033[0m')
    General.update_one({"name":"鲁肃"},{"$set":{"age":53}}) #update()方法已过时，推荐使用update_one或update_many来插入文档数据。
    print("文档数据更新成功！")

# 删除操作
def do_remove():
    print("\033[1;31m--------删除文档--------\033[0m")
    print('\033[1;34mremove():\033[0m')
    General.remove({"name":"黄盖"}) # 除此之外，还可以使用delete_one()和delete_many()来删除文档数据
    print("文档数据删除成功！")

if __name__ == '__main__':
    do_remove()
