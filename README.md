#### 基于Selenium WebDriver搜狗微信公众号爬虫  



**主要功能是根据输入的关键词爬取最新的文章，包括标题，简介，作者，上传时间等内容。**  

**通过webdriver解决搜狗微信的反扒机制，直接使用浏览器进行爬虫，虽然效率比较低，但是实现起来难度小，适合轻量级的爬虫。**  



**2021-9-17:相比较上一版本，新增了具体内容的爬取，仔细观察注释，在循环中设置页数，这里可新增一个页数变**  

**因为频繁访问具体页面获取数据会引起反爬程序，所以设置了在控制台手动输入验证码的环节，时间为100s**  

**可以自行修改或自行设置一个wait检测到特定的网页特征继续执行** 

**由于使用谷歌内核进行驱动，且环境统一，请使用者自行下载对应版本的谷歌驱动！**  



**注：如果搜狗微信没有登录只能默认爬取10页，登录后才能查任意次数**  

**最后采用输出Json文件或CSV文件的方式，以达到进行后续存储等工作的目的。**  

**详细代码说明请参考注释**  

**使用：keyword 修改搜索关键词，修改关键词运行即可。**  





Chromedriver下载网址：http://chromedriver.storage.googleapis.com/index.html
http://npm.taobao.org/mirrors/chromedriver/