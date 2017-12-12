from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        "Hepler Method"
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out it homepage

        # self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

        # She notices that page title and header mention to-do-lists

        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text

        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" in a text box
        # Edith's hobby is typing fly-fishing lures

        # inputbox = self.browser.find_element_by_id('Buy peacock feathers')

        ## Where she hits enter, the page updates and lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # input.send_keys(Keys.ENTER)
        time.sleep(1)
        """self.check_for_row_in_list_table('1: Buy peacock feathers')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.wait_for_row_in_list_table('1: Buy peacock feathers', [row.text for row in rows])"""

        # There is still a text box inivting her to add another itme
        # She enters "Use peacock feathers to make a fly"
        # Edith is very methodical

        inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacockfeather to make a fly')
        # inputbox.send_keys(Keys.ENTER)

        # The page updates again, an now shows both items on here list

        # self.check_for_row_in_list_table('1: Buy peacock fethers')
        # self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1; Buy peacock feathers', [row.text for row in rows])
        # self.assertIn('2: Use peacock featehrs to make a fly', [row.text for row in rows])

        # Edith wonders whether the site will remember here list.
        # Then she sees that the site has generated a unique URL for here --
        # there is some explanatory text to that effect.

        self.fail('Finish the test!')

        # She visits that URL - here to-do list i still there.

        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):

        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Buy peackock feathers')
        # inputbox.send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # she notices that here list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.

        ## WE use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies, etc.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the homepage. There is no sign of Edith's list

        self.browser.get(self.live_server_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Franics starts a new new list by entering a new item.
        # Hie is less interesting than Edith...

        inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Buy milk')
        # inputbox.send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/list/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list

        page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn('Buy peacock feathers', page_text)
        # self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep

    def test_layout_and_styling(self):

        # Edith goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        # She starts a new lis and see the input is nicely centered there too
        # input.send_keys('testing')
        # input.send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1: testing')

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertAlmostEqual(input.location['x'] + input.size['width'] / 2,
                               # 512,
                               # delta = 10)

