# 使用ip代理来请求
import urllib.request

def create_proxy_handler():
  url = "http://www.baidu.com"

# 免费ip代理网址  xicidaili.com

  #增加代理
  proxys = [
    {'http':'114.233.50.90:9999'},
    {"http":'59.57.149.226:9999'},
    {"http":"114.239.146.237:808"},
    {"http":"183.164.239.32:9999"}
  ]
  for item in proxys:
     #代理处理器
    proxy_handler = urllib.request.ProxyHandler(item)
    print(item)
    #创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)

    #由于免费代理ip容易失效(时效性)，所以我们使用try
    try:
      # timeout超过5s就失效
      data = opener.open(url,timeout=2).read()
      print(data)
    except Exception as e:
      print(e)
 

create_proxy_handler()


 














