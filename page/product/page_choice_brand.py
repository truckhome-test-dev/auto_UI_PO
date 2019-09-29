#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_BrandPage(BasePage):
	#品牌页

	brand = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[1]/dl/dt/a/img") #奔驰左侧图片
	brand1 = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[2]/div[1]/a")     #奔驰品牌右侧文字
	series = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[2]/div[2]/dl/dt/a")    #奔驰新Actros 
	serprice = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[2]/div[2]/dl/dd/a[1]")   #奔驰新Actros报价
	serpic = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[2]/div[2]/dl/dd/a[2]")    #奔驰新Actros图库
	serbbs = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[2]/div[2]/dl/dd/a[3]")    #奔驰新Actros报价论坛
	group = (By.XPATH,u"/html/body/div[4]/div[6]/div[2]/a")   #东风股份集团
	hot = (By.XPATH,u"/html/body/div[6]/a[1]")             #热销榜
	# kctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[2]")
	pktype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[3]")
	ddkctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[4]")
	fbhctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[5]")
	wxtype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[6]")
	pjtype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[7]")
	gcctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[8]")
	zyctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[9]")
	gctype = (By.XPATH,u"/html/body/div[4]/div[3]/div[2]/a[10]")	
	kctype = (By.LINK_TEXT,"卡车品牌")

	#打开网页
	def open_web(self,url):
		self.open_page(url)

	#品牌页进入品牌页（图的方式）
	def brand_brand(self):
		self.click_base(*self.brand)

	#品牌页进入品牌页（字的方式）
	def brand_brand1(self):
		self.click_base(*self.brand1)

	#品牌页进入车系综述页
	def brand_series(self):
		self.click_base(*self.series)

	#品牌页进入车系报价页
	def brand_serprice(self):
		self.click_base(*self.serprice)

	#品牌页进入车系图片页
	def brand_serpic(self):
		self.click_base(*self.serpic)

	#品牌页进入论坛页
	def brand_serbbs(self):
		self.click_base(*self.serbbs)

	#品牌页进入集团页
	def brand_group(self):
		self.click_base(*self.group)

	#品牌页进入热销榜页
	def brand_hot(self):
		self.click_base(*self.hot)

	#品牌页切换卡车品牌
	def brand_kctype(self):
		self.click_base(*self.kctype)

	#品牌页切换皮卡品牌
	def brand_pktype(self):
		self.click_base(*self.pktype)

	#品牌页切换电动车品牌
	def brand_ddkctype(self):
		self.click_base(*self.ddkctype)

	#品牌页切换封闭货车品牌
	def brand_fbhctype(self):
		self.click_base(*self.fbhctype)

	#品牌页切换微型车品牌
	def brand_wxtype(self):
		self.click_base(*self.wxtype)

	#品牌页切换配件品牌
	def brand_pjtype(self):
		self.click_base(*self.pjtype)

	#品牌页切换工程车品牌
	def brand_gcctype(self):
		self.click_base(*self.gcctype)

	#品牌页切换专用车品牌
	def brand_zyctype(self):
		self.click_base(*self.zyctype)

	#品牌页切换挂车品牌
	def brand_gctype(self):
		self.click_base(*self.gctype)


