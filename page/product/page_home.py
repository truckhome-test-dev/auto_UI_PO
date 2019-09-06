#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_HomePage(BasePage):


    zlzs = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/h2/a")   #子类车系综述页
    zlpz = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/div/a[2]")  #子类车系配置页
    zltp = (By.XPATH,u"")

    def open_web(self,url):
        self.open_page(url)

	#首页进入子类车系综述页
    def pro_zlzs(self):
        zileizs = self.find_element(*self.zlzs)
        zileizs.click()

    #首页进入子类车系配置页
    def pro_zlpz(self):
        zileipz = self.find_element(*self.zlpz)
        zileipz.click()

    #首页进入子类车系配置页
    def pro_zlpz(self):
        zileipz = self.find_element(*self.zlpz)
        zileipz.click()


