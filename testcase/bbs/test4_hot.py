import unittest
from selenium import webdriver
from page.bbs.page_hot import BBsHot
import time

class Test4_Hot(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "https://bbs.360che.com/hotthread/#pvareaid=1010101"
		self.page_hot = BBsHot(self.driver,self.url)
		self.page_hot.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.page_hot.bbs_into_detail()
		time.sleep(3)


