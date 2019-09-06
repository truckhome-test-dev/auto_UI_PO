import unittest
from selenium.webdriver.common.by import By
from page import base

class BBsHome(base.BasePage):

	#定位器
	bbs_home = (By.XPATH,"//*[@id='sitenav']/dl[4]/dt/a")
	bbs_page = (By.XPATH,"//*[@id='sitenav']/dl[4]/dd/span[1]/a")
	bbs_new = (By.XPATH,"//*[@id='sitenav']/dl[4]/dd/span[3]/a")
	bbs_hot = (By.XPATH,"//*[@id='sitenav']/dl[4]/dd/span[2]/a")
	bbs_car = (By.XPATH,"//*[@id='sitenav']/dl[4]/dd/span[4]/a")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#进入社区
	def bbs_into_home(self):
		home = self.find_element(*self.bbs_home)
		home.click()
	

	#进入社区首页
	def bbs_into_page(self):
		page = self.find_element(*self.bbs_page)
		page.click()

	#进入最新帖子
	def bbs_into_new(self):
		new = self.find_element(*self.bbs_new)
		new.click()
		
	#进入十大热帖
	def bbs_into_hot(self):
		hot = self.find_element(*self.bbs_hot)
		hot.click()

	#进入车型论坛
	def bbs_into_car(self):
		car = self.find_element(*self.bbs_car)
		car.click()

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

	#异常情况返回上一个浏览器
	def error_br(self,browser):
		close = self.error_browser(browser)



# 1. find_element(By.ID,"kw")

# 2. find_element(By.NAME,"wd")

# 3. find_element(By.CLASS_NAME,"s_ipt")

# 4. find_element(By.TAG_NAME,"input")

# 5. find_element(By.LINK_TEXT,"新闻板块“）

# 6. find_element(By.PARTIAL_LINK_TEXT,"新”)

# 7. find_element(By.XPATH,"//*[@class='s_ipt']")

# 8. find_element(By.CSS_SELECTOR,“#kw”)