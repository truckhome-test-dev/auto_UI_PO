#coding=utf-8
import time
from selenium.webdriver.common.by import By
from page.base import *

class Pro_HomePage(BasePage):
    #条件选择页

    zlzs = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/h2/a")   #子类车系综述页
    check1 = (By.XPATH,u"/html/body/div[2]/span/a")  #综述页卡车之家的标识
    zlpz = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/div/a[2]")  #子类车系配置页
    check2 = (By.XPATH,u"//*[@id=\"mybody\"]/div[3]/span/a")  #配置页卡车之家的标识    
    zltp = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/div/a[3]")   #子类车系图片页
    zljxs = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[1]/div/a[4]")  #子类车系经销商页               
    cxzs =  (By.XPATH,u"//*[@id=\"productList\"]/li[2]/div[2]/div/table/tbody/tr/td[1]/a")  #车型综述页
    pfbz = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[2]/p[4]/a[2]")   #排放标准进入配置页
    qjdw = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[2]/p[6]/a[1]")    #前进档位进入配置页
    zdml = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[2]/p[3]/a[2]")   #最大马力进入配置页
    qdxs = (By.XPATH,"//*[@id=\"productList\"]/li[1]/div[1]/div[2]/p[1]/a[1]")    #驱动形式进入配置页
    fdj =  (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/div[2]/p[2]/a[1]")    #发动机进入配置页
    xdj = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[2]/div/table/tbody/tr/td[4]/a") #进入询底价页
    check3 = (By.XPATH,"/html/body/div[2]/span")    
    jg = (By.XPATH,u"//*[@id=\"productList\"]/li[1]/div[1]/span/em/a") #价格进入报价页
    zx = (By.XPATH,u"/html/body/div[2]/div[3]/div[6]/div[1]/div[2]/ul[2]/li[1]/a")     #资讯列表进入文章
    check4 = (By.XPATH,u"/html/body/div[2]/h2/a")
    lt = (By.XPATH,u"/html/body/div[2]/div[3]/div[6]/div[2]/div[2]/ul[1]/li[1]/a")   #帖子列表进入论坛
    check5 = (By.XPATH,"//*[@id=\"nv_forum\"]/div[6]/a[1]")
    cx = (By.XPATH,u"/html/body/div[2]/div[3]/div[6]/div[3]/div[2]/ul[1]/li[1]/a")   #车型列表进入车型

    def open_web(self,url):
        self.open_page(url)

	#首页进入子类车系综述页
    def pro_zlzs(self):
        self.click_base(*self.zlzs)
        self.elem_display(1,*self.check1)

    #首页进入子类车系配置页
    def pro_zlpz(self):  
        self.click_base(*self.zlpz)
        self.elem_display(1,*self.check2)       

    #首页进入子类车系图片页
    def pro_zltp(self):
        self.click_base(*self.zltp)
        self.elem_display(1,*self.check1)       

    #首页进入子类车系经销商页
    def pro_zljxs(self):
        self.click_base(*self.zljxs)
        self.elem_display(1,*self.check1)       

    #首页进入车型综述页
    def pro_zlcx(self):
        self.click_base(*self.cxzs)
        self.elem_display(1,*self.check1)    

    #首页排放标准进入配置页
    def pro_pfbz(self):
        self.click_base(*self.pfbz)
        self.elem_display(1,*self.check2)      

    #首页前进档位进入配置页
    def pro_qjdw(self):
        self.click_base(*self.qjdw)
        self.elem_display(1,*self.check2)            

    #首页最大马力进入配置页
    def pro_zdml(self):
        self.click_base(*self.zdml)
        self.elem_display(1,*self.check2) 

    #首页驱动形式进入配置页
    def pro_qdxs(self):
        self.click_base(*self.qdxs)
        self.elem_display(1,*self.check2)            

    #首页发动机进入配置页
    def pro_fdj(self):
        self.click_base(*self.fdj)
        self.elem_display(1,*self.check2)    

    #首页进入询底价页
    def pro_xdj(self):
        self.click_base(*self.xdj)
        self.elem_display(1,*self.check3)   

    #首页价格进入报价页
    def pro_jg(self):
        self.click_base(*self.jg)
        self.elem_display(1,*self.check1)            

    #首页帖子列表进入论坛页
    def pro_lt(self):
        self.click_base(*self.lt)
        self.elem_display(1,*self.check5)    

    #首页文章列表进入资讯页
    def pro_zx(self):
        self.click_base(*self.zx)
        self.elem_display(1,*self.check4)    
   
    #首页车型列表进入车型页
    def pro_cx(self):
        self.click_base(*self.cx)
        self.elem_display(1,*self.check1)        



        
