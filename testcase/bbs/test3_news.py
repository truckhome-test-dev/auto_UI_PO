import unittest
from selenium import webdriver
from page.bbs.page_news import BBsNews
import time

class Test3_News(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "https://bbs.360che.com/newlist/#pvareaid=1010101"
		self.page_news = BBsNews(self.driver,self.url)
		self.page_news.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.page_news.bbs_into_detail()
		time.sleep(3)



