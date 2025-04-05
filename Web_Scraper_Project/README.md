# Web Scraper Project

这是一个简单的 Python 网页爬虫项目，用于抓取指定网页中的数据并保存到 CSV 文件中。

## 项目功能

该爬虫项目可以从指定网页抓取网页的标题 (`<h1>` 标签) 或所有链接（`<a>` 标签的 `href` 属性），并将这些数据保存到 CSV 文件中。

目前，项目包含以下功能：
- 发送 HTTP 请求获取网页内容
- 解析 HTML 内容，提取有用数据（如网页标题或链接）
- 将抓取到的数据保存到 CSV 文件中

## 项目结构

Web_Scraper_Project/ │ ├── main.py # 主程序，负责启动爬虫 ├── fetcher.py # 发送请求，获取网页内容 ├── parser.py # 解析 HTML 内容，提取需要的数据 ├── save.py # 将数据保存到 CSV 文件 └── scraped_data.csv # 存储抓取到的数据（例如，标题或链接）


### 文件说明

- **`main.py`**：爬虫的入口，调用其他模块的功能来完成网页数据抓取的任务。
- **`fetcher.py`**：负责发送 HTTP 请求并获取网页的 HTML 内容。
- **`parser.py`**：解析网页的 HTML 内容，提取我们需要的数据，如标题或链接。
- **`save.py`**：将抓取的数据保存到 CSV 文件中。

## 安装和运行

### 环境要求

请确保你已经安装了 Python 3.x，并且安装了以下依赖库：

```
pip install requests beautifulsoup4
运行步骤
克隆项目到本地：

git clone https://github.com/your_username/Web_Scraper_Project.git
cd Web_Scraper_Project
修改 main.py 中的目标 URL（如果需要抓取不同网页的数据）。

运行爬虫：

python main.py
结果将保存在 scraped_data.csv 文件中。

示例：抓取网页标题
目前，爬虫会从指定的网页抓取 <h1> 标签中的内容，以下是爬虫抓取的示例输出（保存到 scraped_data.csv 文件中）：

Title
Example Domain
示例：抓取所有超链接
你可以根据需要修改 parser.py 中的 parse_data 函数，抓取网页中的所有链接（<a> 标签的 href 属性）。抓取到的数据会保存在 CSV 文件中，以下是一个可能的输出：

Link
http://example.com
http://www.iana.org/domains/example
如何扩展功能
抓取更多的数据：

你可以修改 parser.py 来抓取更多的数据，如段落、图片、表格等，使用 BeautifulSoup 提供的其他解析方法。

多页面抓取：

如果需要抓取多个页面，可以在 main.py 中添加更多的 URL，使用循环抓取多个页面的数据。

处理不同格式的数据：

可以修改 save.py，将数据保存为其他格式（如 JSON、TXT 文件等）。

贡献
如果你有任何改进建议或发现问题，欢迎提交 Issues 或 Pull Requests。

许可证
本项目使用 MIT 许可证，详情请查看 LICENSE 文件。

### 解释：

- **项目功能**：清晰地列出项目目前实现的主要功能，可以帮助查看项目的人了解爬虫的工作原理。
- **项目结构**：展示项目文件夹结构，方便他人了解代码组织方式。
- **文件说明**：对每个文件的功能进行简短说明，使得他人快速了解每个模块的作用。
- **安装和运行**：提供了如何克隆、安装依赖、修改目标 URL、运行爬虫以及查看结果的详细步骤。
- **扩展功能**：鼓励他人参与项目，并说明如何扩展功能（如抓取更多数据、爬取多个页面等）。
- **贡献**：提供贡献方式，让别人参与到项目的开发中。
