from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class VisitorTest(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options = options)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id-list-table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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

        inputbox.send_keys('Learning')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1. Learning')

        # 请输入另一个代办事项
        inputbox = self.browser.find_element_by_id('id-new-item')
        inputbox.send_keys('Working')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('2. Working')

        # 退出
        self.fail('Finished the test!')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
