# main.py

from scraper import fetch_data
from parser import parse_data
from save import save_data

def main():
    url = "https://example.com"  # 目标网页地址
    html = fetch_data(url)      # 获取网页数据
    data = parse_data(html)     # 解析数据
    save_data(data)             # 保存数据

if __name__ == "__main__":
    main()
