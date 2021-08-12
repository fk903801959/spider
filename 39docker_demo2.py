import requests
from urllib.parse import quote
from fake_useragent import UserAgent

lua_script = '''
function main(splash, args)
  assert(splash:go('https://www.guazi.com/buy'))
  assert(splash:wait(2))
  return splash:html()
end
'''

base_url = "http://localhost:8050/execute?lua_source=" + quote(lua_script)

response = requests.get(base_url,headers={'User-Agent':UserAgent().chrome})
response.encoding = 'utf-8'
print(response.text)