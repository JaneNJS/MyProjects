# scraper.py

import requests

def fetch_data(url):
    """
    从指定 URL 获取网页内容。
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None
