
import urllib.request
# 解析中文
import urllib.parse   
import string

def get_params():
  url = "http://www.baidu.com/"

  params = {
    "wd":"中文",
    "key":' zhang',
    "value":'san'
  }
  # 将字典类参数转化为 字符串参数 如：wd：”中文“ -> wd=”编码“
  str_params = urllib.parse.urlencode(params)
  # 连接url
  final_url = url + str_params
  # 带有中文的url转译成计算机可以识别的url
  end_url = urllib.parse.quote(final_url,safe=string.printable)
  # 开始请求
  response = urllib.request.urlopen(end_url)
  # # 解析响应结果
  return response.read().decode("utf-8")
  
print(get_params())


# urllib --- URL 处理模块
# 网址 https://docs.python.org/zh-cn/3/library/urllib.html



