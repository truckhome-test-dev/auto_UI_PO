import unittest
from selenium import webdriver
from page.information.news_home import NewsHome
import time

class Test1_Home(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.360che.com/"
		self.news_home = NewsHome(self.driver,self.url)
		self.news_home.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_home.bbs_into_home()
		time.sleep(3)

	def test_02(self):
		self.news_home.bbs_into_topic()
		time.sleep(3)

	def test_03(self):
		self.news_home.bbs_into_article()
		time.sleep(3)

	def test_04(self):
		self.news_home.bbs_into_broadcast()
		time.sleep(3)

	def test_05(self):
		self.news_home.bbs_into_video()
		time.sleep(3)
		
		

