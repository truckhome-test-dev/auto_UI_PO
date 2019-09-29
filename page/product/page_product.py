#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_ProductPage(BasePage):
    #车型页

    param = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[2]/a")   #车型配置页
    check1 = (By.XPATH,u"//*[@id=\"mybody\"]/div[5]/div[4]/h4")   #配置页验证元素
    pic = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[3]/a")   #车型图片页                     
    check2 = (By.XPATH,u"//*[@id=\"logo\"]/a/img")  #图片页验证元素
    price = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[4]/a")  #车型报价页
    check3 = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[1]/div[1]/div[1]/h4")  #报价页验证元素-"经销商报价"
    article = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[5]/a")  #车型文章页
    check4 = (By.XPATH,u"//*[@id=\"article_tabs\"]/span[1]/a")  #文章页验证元素-"全部"
    bbs = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[6]/a")   #车型论坛页
    check5 = (By.XPATH,u"//*[@id=\"nv_forum\"]/div[6]/div[1]/a[1]")  #论坛页验证元素-"卡车之家论坛"
    service = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[7]/a")    #车型服务站页
    check6 = (By.XPATH,u"/html/body/div[4]/div[4]/div[2]/div[1]/div[1]/div[1]/strong/a")  #服务站验证元素-服务站不全？

    #打开网页
    def open_web(self,url):
        self.open_page(url)

	#进入车型配置页
    def product_param(self):
        self.click_base(*self.param)
        self.elem_display(2,*self.check1)        

    #进入车型图片页
    def product_pic(self):      
        self.click_base(*self.pic)
        self.elem_display(2,*self.check2)           

    #进入车型价格页
    def product_price(self):
        self.click_base(*self.price)
        self.elem_display(2,*self.check3)   

    #进入车型文章页
    def product_article(self):       
        self.click_base(*self.article)
        self.elem_display(2,*self.check4)           

    #进入车型论坛页
    def product_bbs(self):
        self.click_base(*self.bbs)
        self.elem_display(1,*self.check5)

    #进入车型服务站页
    def product_service(self):
        self.click_base(*self.service)
        self.elem_display(2,*self.check6)  
