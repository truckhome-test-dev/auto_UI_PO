import unittest
from selenium import webdriver
from page.information.news_page import NewsPage
import time

class Test2_Page(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.360che.com/news/#pvareaid=1010101"
		self.news_page = NewsPage(self.driver,self.url)
		self.news_page.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_page.bbs_into_dynamic()
		time.sleep(3)
