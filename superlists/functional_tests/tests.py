from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class VisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = self.open_chrome()

    def tearDown(self):
        self.browser.quit()

    def open_chrome(self):
        options = Options()
        options.add_argument('--headless')
        return webdriver.Chrome(chrome_options = options)

    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id-list-table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_for_one_user(self):
        # 打开在线待办事项应用首页
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1. Learning')

        # 请输入另一个代办事项
        inputbox = self.browser.find_element_by_id('id-new-item')
        inputbox.send_keys('Working')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2. Working')

        # 退出
        # self.fail('Finished the test!')

    def test_multiple_users_can_start_lists_at_diffrent_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id-new-item')
        inputbox.send_keys('Playing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Playing')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/list/.+')

        self.browser.quit()

        # A new user
        self.browser = self.open_chrome()
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Playing', page_text)

        inputbox = self.browser.find_element_by_id('id-new-item')
        inputbox.send_keys('Sleeping')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Sleeping')
        guest_list_url = self.browser.current_url
        self.assertRegex(guest_list_url, '/lists/.+')
        self.assertNotEqual(guest_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Playing', page_text)
        self.assertIn('Sleeping', page_text)
