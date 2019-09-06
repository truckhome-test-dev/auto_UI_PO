import unittest
from selenium import webdriver
from page.information.news_broadcast import NewsBroadcast
import time

class Test4_Broadcast(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://zhibo.360che.com/#pvareaid=1010101"
		self.news_broadcast = NewsBroadcast(self.driver,self.url)
		self.news_broadcast.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_broadcast.broadcast_into_broadcast1()
		time.sleep(3)
