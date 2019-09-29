import unittest
from selenium import webdriver
from page.product.page_series import Pro_SeriesPage
import time
from common import *


class Test_Home(unittest.TestCase):
    # 子类车系系列

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/s12/3169_index.html"
        self.pro_series = Pro_SeriesPage(self.driver, self.url)
        self.pro_series.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    #对比标题
    def contrastitle(self,expectitle):
        realtitle = self.pro_series.get_title()
        self.assertEqual(realtitle,expectitle)

    @checkexcept
    def test_01_price(self):
        self.pro_series.series_price()
        expectitle = u"【奔驰新Actros经销商报价】奔驰新Actros多少钱|经销商价格_奔驰_卡车之家"
        self.contrastitle(expectitle)
        time.sleep(2)

    @checkexcept
    def test_02_pic(self):
        # self.pro_series.backpage()
        self.pro_series.series_pic()
        expectitle = u"【奔驰新Actros重卡图片】奔驰新Actros图片大全_奔驰_卡车之家"
        self.contrastitle(expectitle)
        time.sleep(2)

    @checkexcept
    def test_03_article(self):
        # self.pro_series.backpage()        
        self.pro_series.series_article()
        expectitle = u"【奔驰新Actros重卡文章】奔驰新Actros促销|养车|评测_奔驰_卡车之家"
        self.contrastitle(expectitle)        
        time.sleep(2)

    @checkexcept
    def test_04_video(self):
        # self.pro_series.backpage()               
        self.pro_series.series_video()
        # self.pro_series.swithc_browser()
        expectitle = u"【奔驰新Actros视频】奔驰新Actros新车评测视频 奔驰新Actros试驾视频 _奔驰_卡车之家"
        self.contrastitle(expectitle)          
        time.sleep(2)

    @checkexcept
    def test_05_bbs(self):  
        self.pro_series.series_bbs()
        expectitle = u"【新Actros论坛】_ 卡车之家论坛"
        self.pro_series.swithc_browser()
        realtitle = self.pro_series.get_title()
        self.assertEqual(realtitle,expectitle)              
        time.sleep(2)

    @checkexcept
    def test_06_service(self):
        self.pro_series.close_browser()          
        self.pro_series.series_service()
        expectitle = u"【奔驰新Actros服务站】奔驰新Actros售后维修店|地址电话_奔驰_卡车之家"
        self.contrastitle(expectitle)   
        time.sleep(2)

    @checkexcept
    def test_07_taotruck(self):          
        self.pro_series.twotruck()
        time.sleep(2)