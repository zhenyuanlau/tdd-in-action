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
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 请输入一个代办事项
        inputbox = self.browser.find_element_by_id('id-new-item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 输入 Learning
        inputbox.send_keys('Learning')

        # 回车
        inputbox.send_keys(Keys.ENTER)

        # 页面显示 1. Learning
        table = self.browser.find_element_by_id('id-list-table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Learning' for row in rows)
        )

        # 退出
        self.fail('Finished the test!')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
