# parser.py

from bs4 import BeautifulSoup

def parse_data(html):
    """
    解析网页内容，提取标题和链接等信息。
    """
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h1')  # 假设我们想抓取网页中的所有 h1 标签内容
    data = []

    for title in titles:
        data.append(title.get_text())  # 提取文本内容

    return data
