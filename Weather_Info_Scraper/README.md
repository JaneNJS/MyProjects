# 天气信息抓取器（Weather Info Fetcher）

这是一个基于 OpenWeather API 编写的简易天气查询工具。用户只需输入城市名称（英文），即可获取该城市的实时天气状况，包括温度、天气描述等。项目展示了对第三方 API 使用、数据解析、异常处理和敏感信息管理的完整开发流程，适合作为简历作品或面试展示项目。

---

## 🧰 技术栈

- **Python 3.x**  
- `requests`：发送 HTTP 请求，获取接口数据  
- `python-dotenv`：从 `.env` 文件中读取 API 密钥  
- OpenWeather API：提供实时天气数据  

---

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

---

## ⚙️ 配置 API 密钥

1. 访问 [https://openweathermap.org](https://openweathermap.org) 注册并登录；
2. 获取你的 API 密钥；
3. 在项目根目录新建 `.env` 文件，并写入如下内容：

```
API_KEY=你的OpenWeather密钥
```

⚠️ 请确保 `.env` 文件被添加至 `.gitignore`，以防密钥泄露。

---

## 🗂 项目结构

```
weather_fetcher/
├── main.py              # 主程序代码
├── .env                 # 存储 API 密钥（不上传）
├── requirements.txt     # 依赖列表
└── README.md            # 项目说明文档
```

---

## 🚀 使用方法

运行程序：

```bash
python main.py
```

输入城市名称（英文）后，会返回该城市的天气信息：

```text
请输入城市名称（英文）: Beijing
城市: Beijing, CN
温度: 17.94°C
天气状况: 多云
```

---

## ✅ 项目亮点

- ✅ 使用第三方 API 实时获取数据；
- ✅ 使用 `.env` 管理密钥，符合实际开发规范；
- ✅ 结构清晰，逻辑简单易读；
- ✅ 增加异常处理，提升用户体验；
- ✅ 适合初学者学习爬虫/API 数据交互流程；

---

## 🌱 可扩展方向

- 中文城市名自动翻译（可集成 Google Translate API）；
- 查询未来天气预报（调用 Forecast 接口）；
- 打包为桌面应用（Tkinter、PyQt）；
- 添加历史记录保存/导出功能（CSV/本地数据库）；

---

## 💼 适用场景

- 技术面试作品展示  
- 简历中“项目经验”板块  
- 学习 `requests` + API + `.env` 文件管理的实战练习  

---

## 📮 联系我

如果你喜欢这个项目，欢迎 star 或 fork，也欢迎联系我交流学习 💬  
