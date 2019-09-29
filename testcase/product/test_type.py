from selenium import webdriver
from page.product.page_type import Pro_TypePage
import time
from common import *
import unittest

class Test_Brand(unittest.TestCase):
    # 品牌首页

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/BrandCategory.html"    #a按类型查找页
        self.pro_type = Pro_TypePage(self.driver,self.url)
        self.pro_type.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 对比标题
    def contrastitle(self,expectitle):
        self.pro_type.swithc_browser()
        realtitle = self.pro_type.get_title()
        self.assertEqual(realtitle,expectitle)
        self.pro_type.close_browser() 

    @checkexcept
    def test_01_qyche(self):
        self.pro_type.qyche_exist()
        time.sleep(2)

    @checkexcept
    def test_02_zhche(self):
        self.pro_type.zhche_exist()
        time.sleep(2)

    @checkexcept
    def test_03_zxche(self):
        self.pro_type.zxche_exist()
        time.sleep(2)

    @checkexcept
    def test_04_zzzh(self):
        self.pro_type.zzzhou_exist()
        time.sleep(2)

    @checkexcept
    def test_05_gcche(self):
        self.pro_type.gcche_exist()
        time.sleep(2)

    @checkexcept
    def test_06_wxche(self):
        self.pro_type.wxche_exist()
        time.sleep(2)

    @checkexcept
    def test_07_zyche_(self):
        self.pro_type.zyche_exist()
        time.sleep(2)

    @checkexcept
    def test_08_pk(self):
        self.pro_type.pk_exist()
        time.sleep(2)

    @checkexcept
    def test_09_dshc(self):
        self.pro_type.dshc_exist()
        time.sleep(2)

    @checkexcept
    def test_10_pj(self):
        self.pro_type.pj_exist()
        time.sleep(2)

    @checkexcept
    def test_11_fb(self):
        self.pro_type.fb_exist()
        time.sleep(2)

    @checkexcept
    def test_12_fb(self):     
        self.pro_type.frist_subcate()
        time.sleep(2)

    @checkexcept
    def test_13_fb(self):
        self.pro_type.second_price()
        time.sleep(2)

    @checkexcept
    def test_14_fb(self):
        self.pro_type.third_pic()
        time.sleep(2)

    @checkexcept
    def test_15_fb(self):
        self.pro_type.fourth_bbs()
        time.sleep(2)

    @checkexcept
    def test_16_fb(self):
        self.pro_type.gcfir_subcate()
        time.sleep(2)

    @checkexcept
    def test_17_fb(self):
        self.pro_type.gcse_price()
        time.sleep(2)

    @checkexcept
    def test_18_fb(self):
        self.pro_type.pkfir_subcate()
        time.sleep(2)