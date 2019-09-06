from selenium.webdriver.common.by import By
from page import base

class NewsArticle(base.BasePage):

	#定位器
	news_tab_car1 = (By.XPATH,"/html/body/div[3]/a[1]")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入轻卡详情
	def article_into_car1(self):
		car1 = self.find_element(*self.news_tab_car1)
		car1.click()

