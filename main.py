# 网址： 
# https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/
import requests
from bs4 import BeautifulSoup
import json
import requests
import re
import os
    
# story_url="https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/page/{}"

# #在此示例中，我们删除了':authority', ':method', ':path', 和 ':scheme' 因为这些是HTTP/2中使用的特殊表头。现在你的headers应该是有效的，并且可以正常使用requests库来发送GET请求。记得将'Cookie': 'your-cookie-value'中的your-cookie-value替换为实际的cookie
# # 自定义表头
# story_headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Cache-Control': 'max-age=0',
#     'Cookie': 'your-cookie-value',
#     'Referer': 'https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/',
#     'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
# }

# #解析出标题和详情页的url
# #1.实例化beautifulsoup对象，将页面源码加载到对象中
# # soup=BeautifulSoup(page_text.text,'lxml')

# #-soup.tagName a div  属性定位
# #-soup.find
# #-soup.find('div',class_/id/attr='song')
# #-soup.find_all('tagName') 返回符合要求的所有与标签（列表） 
# #-soup.select('.tang') 某种选择器（id,class,标签...选择器），返回的是一个列表。
# # print(soup.select('.tang > ul > li > a'[0]))   层级选择器 > 表示一个层级
# # print(soup.select('.tang > ul a'[0])) 空格表示多个层级
# # 获取标签之间的文本数据
# # - soup.a.text/string/get_text()
# #    -text/get_text()获取某一个标签中所有的文本内容
# #    -string：只能获取该标签下面的直系的文本内容·
# # print(soup.select('.tang > ul a')[0].string/get_text()))
# # 获取标签中的属性值
# # - soup.a['href']

# with open('fated-to-my-forbidden-alpha.txt','w',encoding='utf-8') as fp:
#     i=1
#     url=story_url.format(i)
#     print(url)
#     response=requests.get(url=url, headers=story_headers)
#     page_text=response.text
    
#     print(response.status_code)
#     #对首页的页面数据进行爬取

#     #在首页中解析出章节的标题和详情页的uel
#     #1. 实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
#     soup=BeautifulSoup(page_text,'lxml')

#     #解析章节标题和详情页的url
#     story_title=soup.select('.page-title')[0].text
#     print(story_title)
#     story_text=soup.select('.archive-description')[0].text
#     print(story_text)
#     fp.write(story_title+':'+story_text+'\n')
#     print(story_title+'爬取成功!!!')
    
#     for i in range(1, 11):
#         url=story_url.format(i)
#         print(url)
#         response=requests.get(url=url, headers=story_headers)
#         page_text=response.text
        
#         print(response.status_code)
        
#         soup=BeautifulSoup(page_text,'lxml')

#         li_list=soup.select('.text-center > a')
#         print(li_list)
#         for li in li_list:
#             print(li['href'])
#             detail_url=li['href']
#             #对详情页发起请求，解析出章节内容
#             detail_page_text=requests.get(url=detail_url,headers=story_headers).text
#             #解析出详情页中相关的章节内容
#             detail_soup=BeautifulSoup(detail_page_text,'lxml')
#             title=detail_soup.find('h1', class_='entry-title').text
#             print(title)
#             div_tag = detail_soup.find('div', class_= 'entry-content')
#             #解析章节内容
#             content=div_tag.text
#             print(type(content))
#             # print(content.splitlines())
#             # clean_lines = [line.strip() for line in content.splitlines()]
#             # # 过滤掉空字符串
#             # clean_lines = [line for line in clean_lines if line]
#             # clean_content = '\n'.join(clean_lines)
#             clean_content = re.sub(r'<< Previous Chapter.*Start Reading Free', '', content, flags=re.DOTALL)
#             print(clean_content)
#             fp.write(title+':'+clean_content+'\n')
#             print(title+'爬取成功!!!')

story_url="https://www.goodnovel.com/stories/Werewolf-novels"

#在此示例中，我们删除了':authority', ':method', ':path', 和 ':scheme' 因为这些是HTTP/2中使用的特殊表头。现在你的headers应该是有效的，并且可以正常使用requests库来发送GET请求。记得将'Cookie': 'your-cookie-value'中的your-cookie-value替换为实际的cookie
# 自定义表头
story_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Cookie": "currentLanguage=en; _gid=GA1.2.844050405.1705905420; _gat_gtag_UA_156286741_1=1; _ga_63M8B9SVWF=GS1.1.1705905162.6.1.1705905425.0.0.0; _ga=GA1.2.84453865.1704787821",
    "If-None-Match": 'W/"17e26-t8YC5k65fMOi4FPxWOBTXDOUp1A"',
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}



# 创建文件夹
folder_name = "GoodNovel"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 定义爬取函数
def scrape_genre(genre):
    url = f"https://www.goodnovel.com/stories/{genre}-novels"
    response = requests.get(url, headers=story_headers)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    novels = soup.find_all("div", class_="book-info")

    for novel in novels:
        title = novel.find("h4").text
        author = novel.find("p", class_="author").text
        description = novel.find("p", class_="desc").text

        print("标题：", title)
        print("作者：", author)
        print("描述：", description)
        print()

        # 创建小说文件
        file_name = f"{folder_name}/{title}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"标题：{title}\n")
            file.write(f"作者：{author}\n")
            file.write(f"描述：{description}\n")
            file.write("\n")

            # 获取小说章节内容
            chapters_url = novel.find("a")["href"]
            response = requests.get(chapters_url, headers=story_headers)
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")

            chapters = soup.find_all("div", class_="chapter-item")

            for chapter in chapters:
                chapter_title = chapter.find("a").text
                chapter_url = chapter.find("a")["href"]

                file.write(f"章节：{chapter_title}\n")

                # 获取章节内容
                response = requests.get(chapter_url, headers=story_headers)
                html_content = response.text
                soup = BeautifulSoup(html_content, "html.parser")

                content = soup.find("div", class_="chapter-content").text
                file.write(content)
                file.write("\n\n")

# genre列表
genres = ["Werewolf", "Romance", "Fantasy", "YA-TEEN"]

# 爬取每个genre的小说剧本故事
for genre in genres:
    scrape_genre(genre)
