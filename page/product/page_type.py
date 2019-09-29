#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_TypePage(BasePage):
	#品牌页

	qyche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[1]/a") #牵引车
	zhche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[2]/a") #载货车
	zxche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[3]/a") #自卸车
	zzzhou = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[4]/a") #中置轴
	gcche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[5]/a") #工程车
	wxche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[6]/a") #微型车
	zyche = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[7]/a") #专用车
	pk = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[8]/a") #皮卡
	dshc = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[9]/a") #低速货车
	pj = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[10]/a") #配件
	fb = (By.XPATH,u"//*[@id=\"navigator\"]/ul/li[11]/a") #封闭货车
	frisub = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/dl[1]/dt/a")  #牵引车-第一个车系 
	check1 = (By.XPATH,u"/html/body/div[2]/span/a")
	seprice = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/dl[2]/dd/a[1]")   #牵引车-第二个报价页
	thirdpic = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/dl[3]/dd/a[2]")   #牵引车-第三个图片页
	fourbbs = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/dl[4]/dd/a[3]")  #牵引车-第四个论坛页
	check2 = (By.XPATH,u"//*[@id=\"nv_forum\"]/div[6]/div[1]/a[1]")
	gcfirsub = (By.XPATH,u"/html/body/div[4]/div[9]/dl[1]/dt/a")   #工程车-第一个车系
	check3 = (By.XPATH,u"/html/body/div[2]/div[1]/div/a")
	gcseprice = (By.XPATH,u"/html/body/div[4]/div[9]/dl[2]/dd/a[1]")   #工程车-第二个报价
	check4 = (By.XPATH,u"/html/body/div[7]/div[2]/h1")
	pkfirsub = (By.XPATH,u"/html/body/div[4]/div[15]/dl[1]/dt/a")   #皮车-第一个车系
	check5 = (By.XPATH,u"//*[@id=\"select_tags\"]/span[1]") 


	def open_web(self,url):
		self.open_page(url)

	#牵引车
	def qyche_exist(self):
		self.elem_display(0,*self.qyche)

	#载货车
	def zhche_exist(self):
		self.elem_display(0,*self.zhche)

	#自卸车
	def zxche_exist(self):
		self.elem_display(0,*self.zxche)

	#中置轴
	def zzzhou_exist(self):
		self.elem_display(0,*self.zzzhou)						

	#工程车
	def gcche_exist(self):
		self.elem_display(0,*self.gcche)

	#微型车
	def wxche_exist(self):
		self.elem_display(0,*self.wxche)

	#专用车
	def zyche_exist(self):
		self.elem_display(0,*self.zyche)

	#皮卡
	def pk_exist(self):
		self.elem_display(0,*self.pk)

	#低速货车
	def dshc_exist(self):
		self.elem_display(0,*self.dshc)

	#配件
	def pj_exist(self):
		self.elem_display(0,*self.pj)

	#封闭货车
	def fb_exist(self):
		self.elem_display(0,*self.fb)

	#牵引车-第一个车系
	def frist_subcate(self):
		self.click_base(*self.frisub)
		self.elem_display(1,*self.check1)

	#牵引车-第二个报价页
	def second_price(self):
		self.click_base(*self.seprice)
		self.elem_display(1,*self.check1)

	#牵引车-第三个图片页
	def third_pic(self):
		self.click_base(*self.thirdpic)		
		self.elem_display(1,*self.check1)

	#牵引车-第四个论坛页
	def fourth_bbs(self):
		self.click_base(*self.fourbbs)			
		self.elem_display(1,*self.check2)

	#工程车-第一个车系
	def gcfir_subcate(self):
		self.click_base(*self.gcfirsub)		
		self.elem_display(1,*self.check3)
	
	#工程车-第二个报价
	def gcse_price(self):
		self.click_base(*self.gcseprice)	
		self.elem_display(1,*self.check4)

	#皮卡-第一个车系
	def pkfir_subcate(self):
		self.click_base(*self.pkfirsub)	
		self.elem_display(1,*self.check5)
