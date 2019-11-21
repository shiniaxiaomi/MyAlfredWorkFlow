# -*- coding: utf-8 -*-
import sys
import requests
from urllib.parse import unquote # 导入转码工具包

query = sys.argv[1] #获取参数
domain=sys.argv[2]
query=unquote(query, 'utf-8') #编码格式转化

url=domain+"/getJson/" +query

response = requests.get(url)
# print(response.text)

sys.stdout.write(response.text)