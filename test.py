# 网址： 
# https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/
import requests
from bs4 import BeautifulSoup
import json
import requests

url="https://www.sogou.com/web"

kw=input("enter a keyword:")
param={
    'query':kw
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

response=requests.get(url=url,params=param,headers=headers)
print(response.text)
with open(kw+'.html','w',encoding='utf-8') as f:
    f.write(response.text)

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



    
# def page_get(url,headers):
#     # url = "https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/"
#     # url = "https://www.novelpalace.com/chapter-1-fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/""
#     # https://www.sogou.com/web?query=%E6%B3%A2%E6%99%93%E5%BC%A0&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=7608&sst0=1704709566790&lkt=0%2C0%2C0&sugsuv=1702880951638469&sugtime=1704709566790
#     # 波晓张
#     #处理url携带的参数
#     # 1.指定url

#     # 2.发起请求 
#     # get方法返回一个响应对象
#     response = requests.get(url, headers)
#     print(response)
#     # 3.获取响应数据
#     if response.status_code == 200:
#     # 4.持久化存储
#         with open("story.html", "w", encoding="utf-8") as file:
#             file.write(response.text)
#         print("网页内容已保存到story.html")
#     else:
#         print("网页请求失败")
# page_get("https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/",story_headers)   
    
# if __name__ == "__main__":
#     # url = "https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/"
#     # 1.指定url
#     url = input("请输入要爬取的网页链接：")
#     # 2.发起请求 
#     # get方法返回一个响应对象
#     response = requests.get(url)
#     print(response)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Find the div with class 'archive-description' for the paragraph text
#     archive_description = soup.find('div', class_='archive-description')

#     # Find all divs with class 'entry-content' for the 'Read more' links
#     entry_contents = soup.find_all('div', class_='entry-content')

#     # Open a file to write the output
#     with open('output.txt', 'w', encoding='utf-8') as file:
#         # Write the paragraph text to the file
#         file.write(archive_description.get_text(separator='\n', strip=True))
#         file.write('\n\n')

#         # Loop through each 'entry-content' and extract the hyperlink text and URL
#         for entry_content in entry_contents:
#             read_more_link = entry_content.find('a', class_='blogpost-button')
#             if read_more_link:
#                 file.write(read_more_link.get_text() + ': ' + read_more_link['href'] + '\n')

#     # Always close the file when you're done
#     file.close()
        
    
# # # 假定的HTML内容
# # html_content = '''
# # <div class="entry-content">
# #     <p>Filed to story: Fated to My Forbidden Alpha Novel Free Online &gt;&gt; Selene had barely taken two steps out the door when she felt a sudden heat sweeping over her body. Her senses were on fire. There was no pain, only heightened awareness of everything around her. Taste and smell fought for dominance in a struggle&#8230;</p>
# #     <div class="text-center">
# #         <a href="https://www.novelpalace.com/chapter-1-fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/" class="blogpost-button">Read more</a>
# #     </div>
# # </div>
# # '''

# # # 使用BeautifulSoup解析HTML
# # soup = BeautifulSoup(html_content, 'html.parser')

# # # 提取段落文本
# # paragraph_text = soup.find('div', class_='entry-content').p.text

# # # 提取超链接文本和URL
# # read_more_link = soup.find('div', class_='entry-content').find('a', class_='blogpost-button')
# # hyperlink_text = read_more_link.text
# # hyperlink_url = read_more_link['href']

# # # 输出结果
# # print("段落文本:", paragraph_text)
# # print("超链接文本:", hyperlink_text)
# # print("超链接URL:", hyperlink_url)

# # # 将结果写入txt文件
# # with open('output.txt', 'w', encoding='utf-8') as file:
# #     file.write("段落文本:\n" + paragraph_text + "\n\n")
# #     file.write("超链接文本:\n" + hyperlink_text + "\n")
# #     file.write("超链接URL:\n" + hyperlink_url + "\n")

