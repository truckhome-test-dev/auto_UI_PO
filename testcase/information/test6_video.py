import unittest
from selenium import webdriver
from page.information.news_video import NewsVideo
import time

class Test4_Video(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.360che.com/v/#pvareaid=1010101"
		self.news_video = NewsVideo(self.driver,self.url)
		self.news_video.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_video.video_into_video1()
		time.sleep(3)
