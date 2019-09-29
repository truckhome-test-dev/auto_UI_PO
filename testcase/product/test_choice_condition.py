import unittest
from selenium import webdriver
from page.product.page_choice_condition import Pro_HomePage
import time
from common import *

class Test_Home(unittest.TestCase):
    # 报价库条件页
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/"
        self.pro_home = Pro_HomePage(self.driver, self.url)
        self.pro_home.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @checkexcept
    def test_01_zlzs(self):
        self.pro_home.pro_zlzs()
        time.sleep(2)

    @checkexcept
    def test_02_zlpz(self):
        self.pro_home.pro_zlpz()    
        time.sleep(2)

    @checkexcept
    def test_03_zltp(self):      
        self.pro_home.pro_zltp()            
        time.sleep(2)

    @checkexcept
    def test_04_zljxs(self):      
        self.pro_home.pro_zljxs()
        time.sleep(2)

    @checkexcept
    def test_05_zlcx(self):
        self.pro_home.pro_zlcx()       
        time.sleep(2)

    @checkexcept
    def test_06_pfbz(self):
        self.pro_home.pro_pfbz()
        time.sleep(2)

    @checkexcept
    def test_07_qjdw(self):
        self.pro_home.pro_qjdw()
        time.sleep(2)

    @checkexcept
    def test_08_zdml(self):
        self.pro_home.pro_zdml()
        time.sleep(2)

    @checkexcept
    def test_09_qdxs(self):
        self.pro_home.pro_qdxs()
        time.sleep(2)

    @checkexcept
    def test_10_fdj(self):
        self.pro_home.pro_fdj()
        time.sleep(2)

    @checkexcept
    def test_11_xdj(self):
        self.pro_home.pro_xdj()
        time.sleep(2)

    @checkexcept
    def test_12_jg(self):
        self.pro_home.pro_jg()
        time.sleep(2)

    @checkexcept
    def test_13_zx(self):       
        self.pro_home.pro_zx()
        time.sleep(2)

    @checkexcept
    def test_14_lt(self):  
        self.pro_home.pro_lt()
        time.sleep(2)

    @checkexcept
    def test_15_cx(self):
        self.pro_home.pro_cx()
        time.sleep(2)

