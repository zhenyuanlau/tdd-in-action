from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class VisitorTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options = options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开在线待办事项应用首页
        self.browser.get('http://localhost:8000')

        # 看到网页标题包含 “To-Do”
        self.assertIn('TO-DO', self.browser.title)
        self.fail('Finished the test!')

        # 请输入一个代办事项

        # 输入 参加大学同学聚会

        # 回车，页面更新
        # 页面显示 1. 参加大学同学聚会

        # 退出

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
