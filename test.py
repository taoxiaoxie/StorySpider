# 网址： 
# https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/
import requests
from bs4 import BeautifulSoup
import json
import requests


post_url='https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

word=input("enter a word:")
data={
    'kw':word
}

response=requests.post(url=post_url,data=data,headers=headers)

dic_obj=response.json()

fileName=word+'.json'
fp=open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)


print('over!!!')