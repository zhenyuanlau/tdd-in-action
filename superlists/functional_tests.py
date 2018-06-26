from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options = chrome_options)

# 打开在线待办事项应用首页
chrome.get('http://localhost:8000')

# 看到网页标题包含 “To-Do” 
assert 'Django' in chrome.title
