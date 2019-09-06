from selenium.webdriver.common.by import By
from page import base

class NewsHome(base.BasePage):

	#定位器
	news_home = (By.XPATH,"//*[@id='sitenav']/dl[1]/dt/a")
	news_article = (By.XPATH,"//*[@id='sitenav']/dl[1]/dd/span[1]/a")
	news_topic = (By.XPATH,"//*[@id='sitenav']/dl[1]/dd/span[3]/a")
	news_broadcast = (By.XPATH,"//*[@id='sitenav']/dl[1]/dd/span[2]/a")
	news_video = (By.XPATH,"//*[@id='sitenav']/dl[1]/dd/span[4]/a")

	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入资讯
	def bbs_into_home(self):
		home = self.find_element(*self.news_home)
		home.click()

	#进入文章
	def bbs_into_article(self):
		article = self.find_element(*self.news_article)
		article.click()

	#进入专题
	def bbs_into_topic(self):
		topic = self.find_element(*self.news_topic)
		topic.click()
		
	#进入直播
	def bbs_into_broadcast(self):
		broadcast = self.find_element(*self.news_broadcast)
		broadcast.click()

	#进入视频
	def bbs_into_video(self):
		video = self.find_element(*self.news_video)
		video.click()

	#查找元素并输入内容	
	def search_content(self,content):
		content1 = self.find_element(*self.bbs_home)
		content1.send_keys(content)

	#找到元素并点击
	def btn_click(self):
		btn1 = self.find_element(*self.bbs_home)
		btn1.click()
