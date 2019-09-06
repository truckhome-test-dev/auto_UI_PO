from selenium.webdriver.common.by import By
from page import base

class NewsPage(base.BasePage):

	#定位器
	news_dynamic = (By.XPATH,"//*[@id='DaoHangDiv']/ul/li[2]/a/span")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入业界动态
	def bbs_into_dynamic(self):
		dynamic = self.find_element(*self.news_dynamic)
		dynamic.click()

