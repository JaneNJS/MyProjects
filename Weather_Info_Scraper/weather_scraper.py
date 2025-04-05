import requests
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 获取 API 密钥
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 获取天气信息的函数
def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric&lang=zh_cn"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print(f"城市: {location}, {country}")
        print(f"温度: {temperature}°C")
        print(f"天气状况: {condition}")
    else:
        print("获取天气信息失败! 请检查城市名称或API密钥是否正确。")

# 主程序
if __name__ == "__main__":
    user_input_city = input("请输入城市名称（英文）: ")
    get_weather(user_input_city)
