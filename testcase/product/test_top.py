from selenium import webdriver
from page.product.page_top import Pro_TopPage
import time
from common import *
import unittest

class Test_Brand(unittest.TestCase):
    # 品牌首页

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://top.360che.com/zhka/"    #品牌页
        self.pro_top = Pro_TopPage(self.driver,self.url)
        self.pro_top.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    
    @checkexcept
    def test_01_firsub(self):
        self.pro_top.first_subcate()
        time.sleep(2)

    @checkexcept
    def test_02_hotbrand(self):
        self.pro_top.hot_brand()
        time.sleep(2)

    @checkexcept
    def test_03_hotproduct(self):
        self.pro_top.hot_product_tab()
        self.pro_top.hot_product()     
        time.sleep(2)

    @checkexcept
    def test_04_prolist(self):
        self.pro_top.list_product()
        time.sleep(2)

    @checkexcept
    def test_05_firpro(self):
        self.pro_top.first_product()
        time.sleep(2)

    @checkexcept 
    def test_06_brandlist(self):
        self.pro_top.list_brand()
        time.sleep(2)
 
    @checkexcept  
    def test_07_firbrand(self):
        self.pro_top.first_brand()
        time.sleep(2)   

    @checkexcept  
    def test_08_hotsub(self):   
        self.pro_top.hot_subcate()
        time.sleep(2)   

    @checkexcept  
    def test_09_hotbbs(self):     
        self.pro_top.hot_bbs()
        time.sleep(2)

    @checkexcept  
    def test_10_hotarticle(self):       
        self.pro_top.hot_article_tab()
        self.pro_top.hot_article()
        time.sleep(2)       

    @checkexcept
    def test_11_hotsales(self):       
        self.pro_top.new_sales_tab()
        self.pro_top.new_sales()
        time.sleep(2)          
