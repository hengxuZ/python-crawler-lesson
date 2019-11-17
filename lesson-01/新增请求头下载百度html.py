
# urllib模块配置headers，访问https协议的百度

import urllib.request
import ssl

# 创建未证实的ssl上下文
context = ssl._create_unverified_context()

def load_baidu():
  url = "https://www.baidu.com"
  header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
  }
 #创建请求对象,方便后期新增 headers信息
  request = urllib.request.Request(url,headers=header)
  #请求网络数据
  response = urllib.request.urlopen(url,context=context)
  data = response.read().decode('utf-8')
  
  with open("baidu1.html","w") as f:
    f.write(data)
  # print(response.headers)

load_baidu()