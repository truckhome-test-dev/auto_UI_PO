from selenium.webdriver.common.by import By
from page import base

class BBsNews(base.BasePage):

	#定位器 
	bbs_news_detail = (By.XPATH,"//*[@id='normalthread_3349849']/tr/th/a")

	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入帖子详情
	def bbs_into_detail(self):
		detail = self.find_element(*self.bbs_news_detail)
		detail.click()


	#查找元素并输入内容	
	def search_content(self,content):
		content1 = self.find_element(*self.bbs_home)
		content1.send_keys(content)

	#找到元素并点击
	def btn_click(self):
		btn1 = self.find_element(*self.bbs_home)
		btn1.click()
		
	#检查title	
	def check_title(self):
		self.get_title()

	#切换窗体
	def swithc_br(self,browser):
		swithc = self.swithc_browser(browser)

	#关闭当前窗体
	def close_br(self,browser):
		close = self.close_browser(browser)

	#获取属性内容
	def check_text(self):
		self.driver.find_element(*self.bbs_news_detail).text

