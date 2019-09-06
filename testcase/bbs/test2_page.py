import unittest
from selenium import webdriver
from page.bbs.page_page import BBsPage
import time

class Test2_Page(unittest.TestCase):
	#打开浏览器
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.url = "https://bbs.360che.com/#pvareaid=1010101"
		self.page_page = BBsPage(self.driver,self.url)
		self.page_page.open()
		
	@classmethod
	def tearDownClass(self):
		self.driver.quit()

	#执行case
	def test_01(self):
		self.page_page.bbs_into_jinhua()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【论坛精华帖】_ 卡车之家论坛")
		except AssertionError as e:
			raise

	def test_02(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_into_news()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【卡车新帖子】_ 卡车之家论坛")
		except AssertionError as e:
			raise
		
	def test_03(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_into_hot()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"卡车十大热帖排行_卡车论坛_卡车之家论坛")
		except AssertionError as e:
			raise

	def test_04(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_ten_hot1()
		time.sleep(3)

	def test_05(self):
		self.page_page.bbs_ten_hot2()
		time.sleep(3)

	def test_06(self):
		self.page_page.bbs_ten_note1()
		time.sleep(3)

	def test_07(self):
		self.page_page.bbs_ten_note2()
		time.sleep(3)
		
	def test_08(self):
		self.page_page.bbs_tool_1()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【车速计算器】卡车车速计算器_卡车之家")
		except AssertionError as e:
			raise

	def test_09(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tool_2()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【车速计算器】卡车车速计算器V2.0_卡车之家")
		except AssertionError as e:
			raise

	def test_10(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tool_3()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"二手卡车评估_ 免费二手卡车估价计算器_手机卡车之家")
		except AssertionError as e:
			raise

	def test_11(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tool_4()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"大货车保险_卡车保险免费获取报价_车险官方网_卡车之家")
		except AssertionError as e:
			raise

	def test_12(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tool_5()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【一汽解放经销商大全】经销商地址|电话|优惠促销_卡车之家")
		except AssertionError as e:
			raise

	def test_13(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tool_6()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【北京服务站大全】全国最新卡车维修网_货车维修厂_卡车之家")
		except AssertionError as e:
			raise

	def test_14(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tab_1()
		time.sleep(5)
		self.page_page.close_swcl(self.driver)


	def test_15(self):
		self.page_page.bbs_tab_2()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【卡车报价库】2019新款卡车价格及图片大全_卡车之家")
		except AssertionError as e:
			raise

	def test_16(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_tab_3()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"卡车之家正品配件商城")
		except AssertionError as e:
			raise

	def test_17(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_ad_1()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_18(self):
		self.page_page.bbs_ad_2()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_19(self):
		self.page_page.bbs_ad_3()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_20(self):
		self.page_page.bbs_ad_4()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_21(self):
		self.page_page.bbs_ad_5()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_22(self):
		self.page_page.bbs_hot_car1()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_23(self):
		self.page_page.bbs_hot_car2()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_24(self):
		self.page_page.bbs_hot_car3()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_25(self):
		self.page_page.bbs_car()
		self.page_page.close_swcl(self.driver)
		time.sleep(5)

	def test_26_产品中心(self):
		self.page_page.bbs_pr_centre1()
		time.sleep(5)
		self.page_page.close_swcl(self.driver)

	def test_27_产品中心(self):
		self.page_page.bbs_pr_centre2()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【牵引车报价】2019新款牵引车价格及图片大全_卡车之家")
		except AssertionError as e:
			raise

	def test_28_产品中心(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_pr_centre3()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【自卸车报价】2019新款自卸车价格及图片大全_卡车之家")
		except AssertionError as e:
			raise

	def test_29_产品中心(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_pr_centre4()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【载货车报价】2019新款载货车价格及图片大全_卡车之家")
		except AssertionError as e:
			raise

	def test_30_产品中心(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_pr_centre5()
		time.sleep(5)

	def test_31_产品中心其他(self):
		self.page_page.bbs_pr_centre6()
		time.sleep(5)
		self.page_page.close_swcl(self.driver)

	def test_32_友情链接_货车(self):
		self.page_page.bbs_friendly_1()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【货车之家】厢式货车_货车报价|大货车图片_卡车之家")
		except AssertionError as e:
			raise

	def test_33_友情链接_汽车票网上订票(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_friendly_2()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"畅途网:长途汽车票网上订票官网_客车时刻表查询_汽车票预订")
		except AssertionError as e:
			raise

	def test_34_友情链接_汽车新闻(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_friendly_3()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"汽车行业新闻，最新汽车新闻，汽车新闻网 – 车主之家")
		except AssertionError as e:
			raise

	def test_35_友情链接_货车网(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_friendly_4()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【货车之家】厢式货车_货车报价|大货车图片_卡车之家")
		except AssertionError as e:
			raise

	def test_36_友情链接_皮卡(self):
		self.page_page.close_br(self.driver)
		self.page_page.bbs_friendly_5()
		time.sleep(5)
		try:
			self.page_page.swithc_br(self.driver)
			title = self.driver.title
			self.assertEqual(title,u"【皮卡之家】皮卡车大全 资讯 报价 视频 论坛_卡车之家")
		except AssertionError as e:
			raise

