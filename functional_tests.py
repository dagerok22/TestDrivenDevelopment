import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# def get_firefoxbinary():
#     return FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox')
#
# binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox')
# browser = webdriver.Firefox(firefox_binary=binary)
#

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
# browser.get('http://localhost:8000')
# She notices the page title and header mention to-do lists
# assert 'To-Do' in browser.title
# She is invited to enter a to-do item straight away
# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)
# The page updates again, and now shows both items on her list
# browser.quit()

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        # browser.get('http://localhost:8000')
        self.browser.get('http://127.0.0.1:8000/')
        # She notices the page title and header mention to-do lists
        # assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('To-Do', header_text)
        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         inputbox)
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any('Buy peacock feathers' == row.text for row in rows))
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        # The page updates again, and now shows both items on her list
        # browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
