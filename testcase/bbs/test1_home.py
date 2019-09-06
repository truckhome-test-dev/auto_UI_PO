import unittest
from selenium import webdriver
from page.bbs.page_home import BBsHome
import time

class Test1_Home(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.360che.com/"
		self.bbs_page = BBsHome(self.driver,self.url)
		self.bbs_page.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.bbs_page.bbs_into_home()
		time.sleep(5)
		try:
			self.bbs_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"卡车之家论坛 - 网聚卡车人的力量 我的卡车论坛##")
		except AssertionError as e:
			raise

	def test_02(self):
		self.bbs_page.close_br(self.driver)
		self.bbs_page.bbs_into_page()
		time.sleep(5)
		try:
			self.bbs_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"卡车之家论坛 - 网聚卡车人的力量 我的卡车论坛")
		except AssertionError as e:
			raise

	def test_03(self):
		self.bbs_page.close_br(self.driver)
		self.bbs_page.bbs_into_new()
		time.sleep(5)
		try:
			self.bbs_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【卡车新帖子】_ 卡车之家论坛")
		except AssertionError as e:
			raise

	def test_04(self):
		self.bbs_page.close_br(self.driver)
		self.bbs_page.bbs_into_hot()
		time.sleep(5)
		try:
			self.bbs_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"卡车十大热帖排行_卡车论坛_卡车之家论坛")
		except AssertionError as e:
			raise

	def test_05(self):
		self.bbs_page.close_br(self.driver)
		self.bbs_page.bbs_into_car()
		time.sleep(5)
		try:
			self.bbs_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【车型论坛大全】_ 卡车之家论坛")
		except AssertionError as e:
			raise
		

