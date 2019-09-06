import unittest
from selenium import webdriver
from page.information.news_article import NewsArticle
import time

class Test3_Article(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.360che.com/Lablelist.html#pvareaid=1010101"
		self.news_article = NewsArticle(self.driver,self.url)
		self.news_article.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.news_article.article_into_car1()
		time.sleep(3)
