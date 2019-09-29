#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_SubcatePage(BasePage):
    #子类车系页

    param = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[2]/a")  #子类车系配置页
    pic = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[3]/a")   #子类车系图片页
    price = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[4]/a")  #子类车系报价页
    article = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[5]/a")  #子类车系文章页
    video = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[6]/a")  #子类车系视频页
    bbs = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[7]/a")  #子类车系论坛页
    service = (By.XPATH,u"/html/body/div[4]/div[5]/ul/li[8]/a")  #子类车系服务站页
    taotruck = (By.XPATH,u"/html/body/div[4]/div[4]/div[1]/div[2]/ul/li[9]/a/span")  #二手车
    check1 = (By.XPATH,u"/html/body/div[1]/div/div[1]/div[1]/h1/a")


    #打开网页
    def open_web(self,url):
        self.open_page(url)

	#进入子类车系配置页
    def subcate_param(self):
        self.click_base(*self.param)

    #进入子类车系图片页
    def subcate_pic(self):
        self.click_base(*self.pic)

    #进入子类车系价格页
    def subcate_price(self):
        self.click_base(*self.price)

    #进入子类车系文章页
    def subcate_article(self):
        self.click_base(*self.article)

    #进入子类车系视频页
    def subcate_video(self):
        self.click_base(*self.video)

    #进入子类车系论坛页
    def subcate_bbs(self):
        self.click_base(*self.bbs)

    #进入子类车系服务站页
    def subcate_service(self):
        self.click_base(*self.service)

    #进入二手车
    def twotruck(self):
        self.click_base(*self.taotruck)
        self.elem_display(0,*self.check1)        

