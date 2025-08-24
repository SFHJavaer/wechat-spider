# 微信公众号爬虫 (WeChat Spider)

基于 Selenium WebDriver 的搜狗微信公众号文章爬虫工具，支持关键词搜索、文章内容爬取和数据导出。

## 🚀 主要功能

- **关键词搜索**: 根据用户输入的关键词搜索微信公众号文章
- **文章信息爬取**: 自动爬取文章标题、作者、发布时间、简介等基本信息
- **全文内容获取**: 深入爬取文章的完整正文内容
- **智能翻页**: 支持多页数据自动翻页爬取
- **数据导出**: 支持 JSON 格式数据导出，方便后续处理
- **反爬机制应对**: 内置反爬检测和手动验证码输入处理

## 📋 环境要求

- Python 3.6+
- Google Chrome 浏览器
- ChromeDriver (需与 Chrome 版本匹配)
- 依赖包：
  - selenium
  - 其他标准库 (json, csv, time)

## 🛠️ 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/wechat-spider.git
   cd wechat-spider
   ```

2. **安装依赖**
   ```bash
   pip install selenium
   ```

3. **下载 ChromeDriver**
   - 访问 [ChromeDriver 下载页面](http://chromedriver.storage.googleapis.com/index.html)
   - 或使用国内镜像: http://npm.taobao.org/mirrors/chromedriver/
   - 下载与你 Chrome 浏览器版本匹配的 ChromeDriver
   - 将 `chromedriver.exe` 放在项目根目录

## 📖 使用方法

1. **运行爬虫**
   ```bash
   python main.py
   ```

2. **输入搜索关键词**
   - 程序启动后会提示输入搜索关键词
   - 输入你想要搜索的微信文章关键词

3. **等待登录**
   - 程序会自动打开搜狗微信搜索页面
   - 需要手动点击登录并完成登录流程

4. **处理验证码**
   - 如果遇到验证码，程序会暂停100秒
   - 在此期间手动输入验证码

5. **查看结果**
   - 爬取完成后，数据会保存为 `data_json.json` 文件
   - 包含文章标题、作者、时间、简介和完整内容

## 📁 项目结构

```
wechat-spider/
├── main.py              # 主程序入口
├── start_spider.py      # 爬虫启动和搜索逻辑
├── page_text.py         # 文章内容爬取逻辑
├── debug.py             # 调试工具
├── README.md            # 项目说明文档
├── data_json.json       # 爬取结果 (生成)
└── chromedriver.exe     # Chrome驱动 (需要下载)
```

## ⚠️ 注意事项

- **登录要求**: 未登录状态下只能爬取前10页内容，登录后可爬取更多页面
- **验证码处理**: 程序会检测反爬机制，遇到验证码时会暂停100秒供手动处理
- **爬取速度**: 为避免被检测，建议控制爬取频率
- **数据存储**: 目前主要支持 JSON 格式导出，CSV 导出代码已注释
- **页面变化**: 搜狗微信页面结构可能变化，需要相应调整 XPath 选择器

## 🔧 自定义配置

- **修改爬取页数**: 在 `page_text.py` 第74行修改 `if num > 86` 中的数字
- **调整等待时间**: 根据网络情况调整 `time.sleep()` 的参数
- **修改数据字段**: 在 `page_text.py` 中自定义抓取的数据字段

## 📝 更新日志

- **2021-09-17**: 新增具体内容爬取功能，支持获取文章正文
- **初始版本**: 实现基础的文章信息爬取和搜索功能

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目仅供学习和研究使用，请遵守相关法律法规和网站的使用条款。
