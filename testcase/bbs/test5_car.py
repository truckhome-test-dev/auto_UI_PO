import unittest
from selenium import webdriver
from page.bbs.page_car import BBsCar
import time

class Test5_Car(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "https://bbs.360che.com/clublist/#bbsindex_more#pvareaid=1010101"
		self.page_car = BBsCar(self.driver,self.url)
		self.page_car.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.page_car.bbs_into_detail()
		time.sleep(3)


