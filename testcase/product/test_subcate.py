import unittest
from selenium import webdriver
from page.product.page_subcate import Pro_SubcatePage
import time
from common import *

class Test_Home(unittest.TestCase):
    # 子类车系系列

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/s15/3997_64_index.html"
        self.pro_subcate = Pro_SubcatePage(self.driver, self.url)
        self.pro_subcate.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    #对比标题
    def contrastitle(self,expectitle):
        self.pro_subcate.swithc_browser()
        realtitle = self.pro_subcate.get_title()
        self.assertEqual(realtitle,expectitle)

    @checkexcept
    def test_01_param(self):
        self.pro_subcate.subcate_param()
        expectitle = u"【解放J6L载货车】2019新款解放J6L载货车参数配置|价格对比_一汽解放_卡车之家"
        self.contrastitle(expectitle)
    
    @checkexcept
    def test_02_pic(self):
        self.pro_subcate.backpage()
        self.pro_subcate.subcate_pic()
        expectitle = u"【解放J6L载货车】2019新款解放J6L载货车图片_一汽解放_卡车之家"
        self.contrastitle(expectitle)        
        time.sleep(2)

    @checkexcept
    def test_03_price(self):
        self.pro_subcate.backpage()
        self.pro_subcate.subcate_price()
        expectitle = u"【解放J6L载货车】2019新款解放J6L载货车报价多少钱_价格_一汽解放_卡车之家"
        self.contrastitle(expectitle)       
        time.sleep(2)

    @checkexcept
    def test_04_article(self):
        self.pro_subcate.backpage()
        self.pro_subcate.subcate_article()
        expectitle = u"2019一汽解放J6L载货车文章_卡车之家"
        self.contrastitle(expectitle)         
        time.sleep(2)

    @checkexcept
    def test_05_video(self):
        self.pro_subcate.backpage()        
        self.pro_subcate.subcate_video()
        expectitle = u"【解放J6L载货车视频】解放J6L载货车新车评测视频 解放J6L载货车试驾视频_一汽解放_卡车之家"
        self.contrastitle(expectitle)           
        time.sleep(2)

    @checkexcept
    def test_06_bbs(self):
        self.pro_subcate.backpage()         
        self.pro_subcate.subcate_bbs()
        expectitle = u"【解放J6L载货车论坛】_ 卡车之家论坛"
        self.pro_subcate.swithc_browser()
        realtitle = self.pro_subcate.get_title()
        self.assertEqual(realtitle,expectitle)        
        time.sleep(2)

    @checkexcept
    def test_07_service(self):
        self.pro_subcate.close_browser()        
        self.pro_subcate.subcate_service() 
        expectitle = u"【解放J6L载货车】2019解放J6L载货车全国维修|服务站|地址电话_卡车之家"
        self.contrastitle(expectitle)          
        time.sleep(2)

    @checkexcept
    def test_08_taotruck(self):          
        self.pro_subcate.twotruck()
        time.sleep(2)