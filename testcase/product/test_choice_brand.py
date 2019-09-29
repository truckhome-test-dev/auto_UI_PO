from selenium import webdriver
from page.product.page_choice_brand import Pro_BrandPage
import time
from common import *
import unittest

class Test_Brand(unittest.TestCase):
    # 品牌首页

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/BrandList.html"    #品牌页
        self.pro_brand = Pro_BrandPage(self.driver,self.url)
        self.pro_brand.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 对比标题
    def contrastitle(self,expectitle):
        self.pro_brand.swithc_browser()
        realtitle = self.pro_brand.get_title()
        self.assertEqual(realtitle,expectitle)
        self.pro_brand.close_browser()    

    @checkexcept
    def test_01_brand(self):
        self.pro_brand.brand_brand()
        expectitle = u"【奔驰】奔驰报价|服务站电话|经销商大全_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_02_brand1(self):
        self.pro_brand.brand_brand1()
        expectitle = u"【奔驰】奔驰报价|服务站电话|经销商大全_卡车之家"
        self.contrastitle(expectitle)


    @checkexcept
    def test_03_series(self):
        self.pro_brand.brand_series()
        expectitle = u"【奔驰新Actros重卡】奔驰新Actros报价|配置|图片_奔驰_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_04_serprice(self):
        self.pro_brand.brand_serprice()
        expectitle = u"【奔驰新Actros经销商报价】奔驰新Actros多少钱|经销商价格_奔驰_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_05_serpic(self):
        self.pro_brand.brand_serpic()
        expectitle = u"【奔驰新Actros重卡图片】奔驰新Actros图片大全_奔驰_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_06_serbbs(self):
        self.pro_brand.brand_serbbs()
        expectitle = u"【奔驰论坛】_ 卡车之家论坛"
        self.contrastitle(expectitle)

    @checkexcept
    def test_07_group(self):
        self.pro_brand.brand_group()
        expectitle = u"【东风股份】东风汽车报价及图片_东风股份汽车大全_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_08_hot(self): 
        self.pro_brand.brand_hot()
        expectitle = u"【牵引车哪个牌子好】2019年牵引车销量排名_牵引车排行榜_卡车之家"
        self.contrastitle(expectitle)

    @checkexcept
    def test_09_kctype(self):   
        self.pro_brand.brand_kctype()
        time.sleep(2)

    @checkexcept
    def test_10_pktype(self):
        self.pro_brand.brand_pktype()
        time.sleep(2)

    @checkexcept
    def test_11_ddkctype(self):
        self.pro_brand.brand_ddkctype()
        time.sleep(2)
    
    @checkexcept
    def test_12_fbhctype(self):
        self.pro_brand.brand_fbhctype()
        time.sleep(2)

    @checkexcept
    def test_13_wxtype(self):
        self.pro_brand.brand_wxtype()
        time.sleep(2)

    @checkexcept
    def test_14_pjtype(self):
        self.pro_brand.brand_pjtype()
        time.sleep(2)

    @checkexcept
    def test_15_gcctype(self):
        self.pro_brand.brand_gcctype()
        time.sleep(2)

    @checkexcept
    def test_16_zyctype(self):
        self.pro_brand.brand_zyctype()
        time.sleep(2)

    @checkexcept
    def test_17_gctype(self):
        self.pro_brand.brand_gctype()
        time.sleep(2)
