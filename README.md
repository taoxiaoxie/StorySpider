# StorySpider

- StoryBot数据构造

1. 爆款短剧
  所谓“跑通模型”的产品，即是上述产品ReelShort。Sensor Tower数据显示，2023年7月，ReelShort在Google Play和App Store的总下载量达190万，月总流水达600万美元。
  7月，ReelShort有两部短剧爆了，即《Fated To My Forbidden Alpha》和《Never Divorce a Secret Billionaire Heiress》，“这两部剧爆了之后，大家发现霸总、狼人题材在国外的短剧市场，还是比较吃香的。”小夏说道。
  《Fated To My Forbidden Alpha》

   网址：
   https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/
  
2. DND龙与地下城
（需要对话内容至少30-40% 不超过80% 场景描述 旁白 对话）

# StorySpider爬虫
- 剧本数据路径：https://www.novelpalace.com/category/fated-to-my-forbidden-alpha-novel-book-free-online-alpha-alexander-selene/

- Run
1. 安装依赖
```bash
pip3 install -r requirements.txt
```

2. 下载huggingface 项目
```bash
git clone https://huggingface.co/datasets/alpindale/visual-novels
```

3. 运行爬虫项目
```bash
python3 main.py
```
> 注； 信号量设置为10，间隔时间为0.3s，(`config.py`)可根据自己的需求进行修改。
> 太快会被封ip。
