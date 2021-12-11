import start_spider
import time
num = 0
# 声明一个列表存储字典
data_list = []
def page_text():
    while True:
        browser = start_spider.browser
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
                #同时将搜索的关键词存入数据库中
                # data_dict['key_words'] = keyword


                # print(data_dict)

                data_list.append(data_dict)  # 把遍历出的数据添加到列表末尾
                # 如果找不到下一页按钮就抛出异常并退出循环
                browser.back()
            except IndexError as i:
                print("爬虫被检测，请手动输入验证码：")
                time.sleep(100)
                continue
        next
        try:
            sogou_next = browser.find_element_by_id('sogou_next')
            # 如果下一页按钮存在就继续
            sogou_next.click()
            num = num + 1
            if num > 86:  # 修改循环来控制爬取的页数
                break
        except Exception as e:
            break
         
        
           
