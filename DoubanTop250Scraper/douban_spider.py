import requests
from bs4 import BeautifulSoup
import csv
import time

def fetch_movies():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    all_movies = []

    for page in range(0, 25, 25):  # 只抓前一页（前25个电影）
        url = f"https://movie.douban.com/top250?start={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="item")

        for item in items:
            title = item.find("span", class_="title").text
            rating = item.find("span", class_="rating_num").text
            quote = item.find("span", class_="inq")
            quote_text = quote.text if quote else "暂无简介"

            all_movies.append([title, rating, quote_text])
        time.sleep(1)  # 模拟延迟防止被封IP

    return all_movies

def save_to_csv(data, filename="douban_movies.csv"):
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["标题", "评分", "简介"])
        writer.writerows(data)
    print(f"✅ 已保存到 {filename}")

if __name__ == "__main__":
    try:
        movies = fetch_movies()
        save_to_csv(movies)
    except Exception as e:
        print(f"❌ 抓取失败，错误信息：{e}")
