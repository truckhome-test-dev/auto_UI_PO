import unittest
from selenium import webdriver
from page.product.page_product import Pro_ProductPage
import time
from common import *

class Test_Home(unittest.TestCase):
    # 车型综述页

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/m192/48186_index.html"
        self.pro_product = Pro_ProductPage(self.driver, self.url)
        self.pro_product.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @checkexcept
    def test_01_param(self):
        self.pro_product.product_param()
        time.sleep(2)

    @checkexcept
    def test_02_pic(self):
        self.pro_product.product_pic()
        time.sleep(2)

    @checkexcept
    def test_03_price(self):
        self.pro_product.product_price()
        time.sleep(2)

    @checkexcept
    def test_04_article(self):
        self.pro_product.product_article()     
        time.sleep(2)

    @checkexcept
    def test_05_bbs(self):
        self.pro_product.product_bbs()
        time.sleep(2)     

    @checkexcept
    def test_06_service(self):
        self.pro_product.product_service()    
        time.sleep(2)
