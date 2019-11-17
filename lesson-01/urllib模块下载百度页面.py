# urllib模块下载百度的html页面
import urllib.request

def load_baidu():
  url = "http://www.baidu.com"
  
  #请求网络数据
  response = urllib.request.urlopen(url)

  data = response.read().decode('utf-8')
  
  with open("baidu.html","w") as f:
    f.write(data)

load_baidu()