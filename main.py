import json
import csv

from start_spider import start_spiders

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
