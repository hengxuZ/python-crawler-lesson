# 由于反/防爬虫策略，以及防止封ip的风险
# 我们选择动态切换user-agent

import urllib.request
import ssl
import random

# 创建未证实的ssl上下文
context = ssl._create_unverified_context()

def load_baidu():
  url = "https://www.baidu.com"
  header = {
    ''
  }
  # 创建代理列表
  user_agent_list = [
  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
  'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
  ]
  #每次请求的浏览器都是不一样的
  random_user_agent = random.choice(user_agent_list)
 #创建请求对象,方便后期新增 headers信息
  request = urllib.request.Request(url)
  # 增加请求头
  request.add_header('User-Agent',random_user_agent)
  #请求网络数据
  response = urllib.request.urlopen(request,context=context)
  data = response.read().decode('utf-8')
  
  with open("baidu1.html","w") as f:
    f.write(data)
  # print(response.headers)

load_baidu()