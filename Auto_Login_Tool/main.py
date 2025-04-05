from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import time

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
login_url = config.get('login', 'url')
username = config.get('login', 'username')
password = config.get('login', 'password')

# 启动浏览器（使用 webdriver-manager 自动下载驱动）
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开登录页面
driver.get(login_url)

# 等待并填入用户名和密码
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)

# 可选：点击登录按钮（如果想要）
# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
# login_button.click()

# 等待几秒查看效果
time.sleep(5)
driver.quit()
