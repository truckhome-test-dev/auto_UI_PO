import unittest
from selenium import webdriver
from page.information.news_topic import NewsTopic
import time

class Test4_Topic(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://topic.360che.com/pclist.html#pvareaid=1010101"
		self.news_topic = NewsTopic(self.driver,self.url)
		self.news_topic.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_topic.article_into_phone()
		time.sleep(3)
