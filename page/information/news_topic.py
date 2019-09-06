from selenium.webdriver.common.by import By
from page import base

class NewsTopic(base.BasePage):

	#定位器
	news_tab_phone = (By.XPATH,"//*[@id='pc_topic']/ul/li[1]/a[1]/img")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入移动
	def article_into_phone(self):
		phone = self.find_element(*self.news_tab_phone)
		phone.click()

