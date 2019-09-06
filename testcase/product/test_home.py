import unittest
from selenium import webdriver
from page.product.page_home import Pro_HomePage
import time


class Test1_Home(unittest.TestCase):
    # 打开浏览器——报价库首页
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "https://product.360che.com/"
        self.pro_home = Pro_HomePage(self.driver, self.url)
        self.pro_home.open_web(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

        # 进入子类车系综述页

    def test_01(self):
        self.pro_home.pro_zlzs()
        time.sleep(3)
        self.pro_home.pro_zlpz()
