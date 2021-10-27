href.click()  # 点击详情页模拟
WebDriverWait(browser, 1000).until(  # 对象是brower，就是驱动器，最大等待1000时间
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'rich_media_title')  # （刷新，直到登陆成功找到class为yh，就成功了，大家可以从源代码里找到这个标签，同时返回布尔数）
    )
)
text_list = browser.find_elements_by_xpath('//ul[@class="news-list2"]/li')  # 从根目录找到class为。。的ul元素
print(text_list)
text = text_list.text
print(text)
