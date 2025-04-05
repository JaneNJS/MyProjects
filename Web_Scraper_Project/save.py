# save.py

import csv

def save_data(data):
    """
    将抓取的数据保存到 CSV 文件中。
    """
    with open('data/scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])  # 写入表头
        for item in data:
            writer.writerow([item])  # 写入数据行
