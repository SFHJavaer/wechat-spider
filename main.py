from selenium import webdriver  # 从自动化库里导入这个模块
from selenium.webdriver.support.ui import WebDriverWait  # 从模块导入显示等待（隐式，强制）
from selenium.webdriver.support import \
    expected_conditions as EC  # 导入模块（）可以对网页上元素，弹窗是否存在，可点击等等进行判断，一般用于断言或与WebDriverWait配合使用。
from selenium.webdriver.common.by import By  # By是selenium中内置的一个class，在这个class中有各种方法来定位元素（定位器，用于css，xpath ）
import json
import csv
import requests
from lxml import etree
import time

# 声明一个谷歌浏览器的驱动器
browser = webdriver.Chrome(executable_path='./chromedriver')  # 打开chrome和驱动（webdriver模块放一个文件，不写路径）（自动化库到驱动到浏览器）
# url网址
url = 'https://weixin.sogou.com/'
# 请求该网址
browser.get(url)  # get方法打开网址

# 声明一个列表存储字典
data_list = []


def start_spiders():  # 定位是关键，找到输入框等等，选择元素，通过特征
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }  # 添加为自己的
    # 找到输入框id
    query = browser.find_element_by_id('query')  # 和下方定位同理
    keyword = input('输入：')
    query.send_keys(keyword)  # query是一个element对象，用send_keys方法输入字符串
    # 找到搜索按钮
    swz = browser.find_element_by_class_name('swz')  # 找到搜索按钮，找到这个swz标签（classname是这个，如果name或者id唯一用name，id找也行（找特征））
    swz.click()
    # 找到登陆按钮并点击

    top_login = browser.find_element_by_id('top_login')
    top_login.click()#一步一步模拟
    # 显示等待是否登陆成功
    WebDriverWait(browser, 1000).until( #对象是brower，就是驱动器，最大等待1000时间
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'yh')#（刷新，直到登陆成功找到class为yh，就成功了，大家可以从源代码里找到这个标签，同时返回布尔数）
        )
    )
    print('登陆成功')
    num = 0

    while True:
        # 找到所有的li标签（在开发者里面找到相应的元素（由标签名等等）List是列表）
        #lis = browser.find_elements_by_xpath('//ul[@class="news-list"]/li')  # 从根目录找到class为。。的ul元素
        # 找到下一页的按钮
        # 遍历列表，存到字典里去

        for a in range(9):
            try:
                    # 题目
                    lis = browser.find_elements_by_xpath('//ul[@class="news-list"]/li')

                    title = lis[a].find_element_by_xpath('.//h3').text

                    # 作者
                    author = lis[a].find_element_by_class_name('account').text
                    # 时间
                    datetime = lis[a].find_element_by_class_name('s2').text
                    # 文章摘要
                    content = lis[a].find_element_by_class_name('txt-info').text
                    # 文章链接
                    href = lis[a].find_element_by_xpath('.//h3/a').get_attribute('href')
                    # 学号
                    id = '20190200514'
                    browser.get(href)

                    time.sleep(0.5)
                    text_list = browser.find_elements_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section')
                    # text_list = browser.find_elements_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section[4]/span')  # 从根目录找到class为。。的ul元素
                    texts = ""
                    for i in text_list:
                        texts += (i.text)

                    print(texts)
                    # for text in text_list:
                    #     text2 = text.text
                    #     print(text2)
                    #     texts += text2

                    # 声明一个字典存储数据

                    data_dict = {}
                    data_dict['text'] = texts
                    data_dict['title'] = title
                    data_dict['author'] = author
                    data_dict['datetime'] = datetime
                    data_dict['content'] = content
                    data_dict['href'] = href
                    data_dict['user_id'] = id
                    data_dict['key_words'] = keyword

                    # print(data_dict)

                    data_list.append(data_dict)  # 把遍历出的数据添加到列表末尾
                # 如果找不到下一页按钮就抛出异常并退出循环
                    browser.back()
            except IndexError as i:
                print("爬虫被检测，请手动输入验证码：")
                time.sleep(100)
                continue


        try:
            sogou_next = browser.find_element_by_id('sogou_next')
            # 如果下一页按钮存在就继续
            sogou_next.click()
            num = num + 1
            if num > 86:     #修改循环来控制爬取的页数
                break
        except Exception as e:
            break


def main():
    start_spiders()


if __name__ == '__main__':
    main()
    # 退出浏览器
    browser.quit()
    print(data_list)
    # 将数据存储到json文件中
    with open('data_json.json', 'a+', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)  # 用dump把python数据结构转换为json类型
    print('json文件写入完成')
    # 将数据存入csv文件中
    # 表头
    # csv_title = data_list[0].keys()#返回一个字典的【0】键
    # with open('data_csv.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     # 写入表头
    #     writer.writerow(csv_title)
    #     # 批量写入表
    #     for row in data_list:
    #         writer.writerow(row.values())
    # print('csv文件写入完成')
    # # coding:utf-8
    # import requests, re
