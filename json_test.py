import json

books = [
    {
        "name": "三国演义",
        "price": 18.8
    },
{
        "name": "水浒传",
        'price': 19.9,
    }
]

fp = open('test.json','w',encoding='utf-8')
json.dump(books,fp,ensure_ascii=False)
fp.close()