from selenium.webdriver.common.by import By
from page import base

class NewsVideo(base.BasePage):

	#定位器
	news_video1 = (By.XPATH,"//*[@id='mybody']/div[6]/div[2]/div[2]/div[1]/dl/dt/a/img")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入视频详情页
	def video_into_video1(self):
		video1 = self.find_element(*self.news_video1)
		video1.click()

