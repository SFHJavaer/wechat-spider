

from selenium import webdriver  # 从自动化库里导入这个模块
from selenium.webdriver.support.ui import WebDriverWait  # 从模块导入显示等待（隐式，强制）
from selenium.webdriver.support import \
    expected_conditions as EC  # 导入模块（）可以对网页上元素，弹窗是否存在，可点击等等进行判断，一般用于断言或与WebDriverWait配合使用。
from selenium.webdriver.common.by import By  # By是selenium中内置的一个class，在这个class中有各种方法来定位元素（定位器，用于css，xpath ）
import page_text


# 声明一个谷歌浏览器的驱动器
browser = webdriver.Chrome(executable_path='./chromedriver')  # 打开chrome和驱动（webdriver模块放一个文件，不写路径）（自动化库到驱动到浏览器）
# url网址
url = 'https://weixin.sogou.com/'
# 请求该网址
browser.get(url)  # get方法打开网址

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}  # 添加为自己的


# 找到输入框id
def start_spiders():  # 定位是关键，找到输入框等等，选择元素，通过特征


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

    
    page_text.page_text()

    
    
  
