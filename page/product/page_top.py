#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_TopPage(BasePage):
	#重卡排行榜页

	subcate = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/ul/li[1]/a") #车系排行第一名
	check1 = (By.XPATH,u"/html/body/div[2]/span/a")   #车系综述页验证元素-卡车之家大logo
	productlist = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div/div/a[2]")  #切换到车型
	product = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/ul/li[1]/a")   #车型列表第一名
	brandlist = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div/div/a[1]")  #切换到品牌列表
	brand = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/ul/li[1]/a")  #品牌列表第一名
	hotprotab = (By.XPATH,u"//*[@id=\"se2\"]") #热门车型tab
	hotsubcate = (By.XPATH,u"//*[@id=\"samee1\"]/div[1]/a")  #热门车系
	hotproduct = (By.XPATH,u"//*[@id=\"samee2\"]/div[1]/a")   #热门车型
	hotbrand = (By.XPATH,u"//*[@id=\"samee1\"]/a[1]/span/img")  #热门品牌
	hotbbs = (By.XPATH,u"//*[@id=\"tabs1\"]/a[1]")  #热门帖子
	check2 = (By.XPATH,u"//*[@id=\"nv_forum\"]/div[6]/a[1]")
	hotarticletab = (By.XPATH,u"//*[@id=\"te3\"]")   #热门文章tab
	hotarticle = (By.XPATH,u"//*[@id=\"tabs3\"]/a[1]")   #热门文章
	check3 = (By.XPATH,u"/html/body/div[6]/div[1]/a/img")   #文章页验证元素-小卡车之家
	salestab = (By.XPATH,u"//*[@id=\"te2\"]")  #降价促销tab	
	sales = (By.XPATH,u"//*[@id=\"tabs2\"]/a[1]")  #降价促销
	check4 = (By.XPATH,"//*[@id=\"__layout\"]/div/div/div[1]/div[3]/div[2]/a[3]")  #促销页验证元素-促销新闻

	#打开网页
	def open_web(self,url):
		self.open_page(url)

	#进入车系排行第一名
	def first_subcate(self):
		self.click_base(*self.subcate)
		self.elem_display(1,*self.check1)

	#进入热门品牌
	def hot_brand(self):
		self.refreshpage()
		self.click_base(*self.hotbrand)
		self.elem_display(1,*self.check1)
            
	#点击热门车型tab
	def hot_product_tab(self):
		self.refreshpage() 
		self.click_base(*self.hotprotab)

	#进入热门车型
	def hot_product(self):
		self.click_base(*self.hotproduct)
		self.elem_display(1,*self.check1)

	#切换到车型列表
	def list_product(self):
		self.click_base(*self.productlist)

	#进入车型列表第一名
	def first_product(self):
		self.click_base(*self.product)
		self.elem_display(1,*self.check1)

	#切换到品牌列表
	def list_brand(self):
		self.click_base(*self.brandlist)

	#进入品牌列表第一名
	def first_brand(self):
		self.click_base(*self.brand)
		self.elem_display(1,*self.check1)

	#进入热门车系
	def hot_subcate(self):
		self.refreshpage()
		self.click_base(*self.hotsubcate)
		self.elem_display(1,*self.check1)

	#进入热门帖子
	def hot_bbs(self):
		self.refreshpage()
		self.click_base(*self.hotbbs)
		self.elem_display(1,*self.check2)

	#点击热门文章tab
	def hot_article_tab(self):
		self.refreshpage()
		self.click_base(*self.hotarticletab)

	#进入热门文章
	def hot_article(self):
		self.click_base(*self.hotarticle)
		self.elem_display(1,*self.check3)
	
	#点击降价促销tab
	def new_sales_tab(self):
		self.refreshpage()
		self.click_base(*self.salestab)

	#进入降价促销
	def new_sales(self):
		self.click_base(*self.sales)
		self.elem_display(1,*self.check4)