from selenium.webdriver.common.by import By
from page import base

 #继承base后既可以调用base的方法也可自己添加新的方法
class SearchPage(base.BasePage):

	#通过id进行定位元素
	#search_loc = (By.ID,"kw")
	#定位元素
	search_loc = (By.ID,"keyword")#搜索框
	btn_loc = (By.CLASS_NAME,"hot-button")#搜索按钮
	#bbs_home = (By.xpath,"//*[@id="sitenav"]/dl[4]/dd/span[1]/a")

	#重写父类的open（）方法
	def open(self):
		self.open_page(self.url)

	def search_content(self,content):
		#调用父类的find_element,然后将本类的参数传入
		content1 = self.find_element(*self.search_loc)
		content1.send_keys(content)

	def btn_click(self):
		btn1 = self.find_element(*self.btn_loc)
		btn1.click()
