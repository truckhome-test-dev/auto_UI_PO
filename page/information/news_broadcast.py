from selenium.webdriver.common.by import By
from page import base

class NewsBroadcast(base.BasePage):

	#定位器
	news_broadcast1 = (By.XPATH,"/html/body/div[6]/div[1]/a")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入卡车之家直播
	def broadcast_into_broadcast1(self):
		broadcast1 = self.find_element(*self.news_broadcast1)
		broadcast1.click()

