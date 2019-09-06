import unittest
from selenium import webdriver
from page.bbs.example_page import SearchPage
import time

class TestExample(unittest.TestCase):
	"""UI自动化搜索"""
	def setUp(self):
		# self.driver = webdriver.Firefox()
		self.driver = webdriver.Chrome()
		time.sleep(3)
		self.url = "http://www.360che.com/"
		time.sleep(3)
		self.content ="卡车之家"

	def test_search(self):
		bing_page = SearchPage(self.driver,self.url)
		bing_page.open()
		time.sleep(3)
		bing_page.search_content(self.content)
		time.sleep(3)
		bing_page.btn_click()
		time.sleep(3)

	def tearDown(self):
		#time.sleep(5)
		self.driver.quit()
