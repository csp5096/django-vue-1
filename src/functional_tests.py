from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out it homepage

        self.browser.get('http://localhost:8000')

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

        inputbox.send_keys('Buy peacock feathers')

        ## Where she hits enter, the page updates and lists
        # "1: Buy peacock feathers" as an item in a to-do list

        input.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inivting her to add another itme
        # She enters "Use peacock feathers to make a fly"
        # Edith is very methodical

        self.fail('Finish the test!')

        # The page updates again, an now shows both items on here list

        # Edith wonders whether the site will remember here list.
        # Then she sees that the site has generated a unique URL for here --
        # there is some explanatory text to that effect.

        # She visits that URL - here to-do list i still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')