from selenium.webdriver.common.by import By
from page import base

class BBsPage(base.BasePage):

	#定位器
	bbs_jinhua = (By.XPATH,"/html/body/div[4]/span/a[1]")
	bbs_news = (By.XPATH,"/html/body/div[4]/span/a[2]")
	bbs_hot = (By.XPATH,"/html/body/div[4]/span/a[3]")
	ten_hot1 = (By.XPATH,"//*[@id='tab-title-1']/li[1]/a")
	ten_hot2 = (By.XPATH,"//*[@id='tab-title-1']/li[2]/a")
	new_note1 = (By.XPATH,"//*[@id='tab-title-2']/li[1]/a")
	new_note2 = (By.XPATH,"//*[@id='tab-title-2']/li[2]/a")
	#卡车工具
	tool_1 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[1]/a")
	tool_2 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[2]/a")
	tool_3 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[3]/a")
	tool_4 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[4]/a")
	tool_5 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[5]/a")
	tool_6 = (By.XPATH,"/html/body/div[9]/div[3]/ul/li[6]/a")
	#第三条广告上方tab
	tab_1 = (By.XPATH,"/html/body/div[10]/a[1]")
	tab_2 = (By.XPATH,"/html/body/div[10]/a[2]")
	tab_3 = (By.XPATH,"/html/body/div[10]/a[3]")

	#第三条广告下方内容
	ad_1 = (By.XPATH,"/html/body/div[12]/ul/li[1]/a[1]/img")
	ad_2 = (By.XPATH,"/html/body/div[12]/ul/li[2]/a[1]/img")
	ad_3 = (By.XPATH,"/html/body/div[12]/ul/li[3]/a[1]/img")
	ad_4 = (By.XPATH,"/html/body/div[12]/ul/li[4]/a[1]/img") 
	ad_5 = (By.XPATH,"/html/body/div[12]/ul/li[5]/a[1]/img")
	#热门车型
	hot_car1 = (By.XPATH,"//*[@id='tab-title-3']/li[1]/a")
	hot_car2 = (By.XPATH,"//*[@id='tab-title-3']/li[2]/a")
	hot_car3 = (By.XPATH,"//*[@id='tab-title-3']/li[3]/a")
	#卡车之家商城
	car = (By.XPATH,"/html/body/div[20]/div[1]/a/img")
	#产品中心
	pr_centre1 = (By.XPATH,"/html/body/div[22]/ul/li[1]/p/a")
	pr_centre2 = (By.XPATH,"/html/body/div[22]/ul/li[2]/p/a")
	pr_centre3 = (By.XPATH,"/html/body/div[22]/ul/li[3]/p/a")
	pr_centre4 = (By.XPATH,"/html/body/div[22]/ul/li[4]/p/a")
	pr_centre5 = (By.XPATH,"/html/body/div[22]/ul/li[5]/p/a")
	pr_centre6 = (By.XPATH,"/html/body/div[22]/ul/li[6]/p/a")
	#友情链接
	friendly_1 = (By.XPATH,"/html/body/div[23]/div[2]/a[1]")
	friendly_2 = (By.XPATH,"/html/body/div[23]/div[2]/a[2]")
	friendly_3 = (By.XPATH,"/html/body/div[23]/div[2]/a[3]")
	friendly_4 = (By.XPATH,"/html/body/div[23]/div[2]/a[4]")
	friendly_5 = (By.XPATH,"/html/body/div[23]/div[2]/a[5]")
	friendly_6 = (By.XPATH,"/html/body/div[23]/div[2]/a[6]")
	friendly_7 = (By.XPATH,"/html/body/div[23]/div[2]/a[7]")
	friendly_8 = (By.XPATH,"/html/body/div[23]/div[2]/a[8]")
	friendly_9 = (By.XPATH,"/html/body/div[23]/div[2]/a[9]")
	friendly_10 = (By.XPATH,"/html/body/div[23]/div[2]/a[10]")
	friendly_11 = (By.XPATH,"/html/body/div[23]/div[2]/a[11]")
	friendly_12 = (By.XPATH,"/html/body/div[23]/div[2]/a[12]")
	friendly_13 = (By.XPATH,"/html/body/div[23]/div[2]/a[13]")
	friendly_14 = (By.XPATH,"/html/body/div[23]/div[2]/a[14]")
	friendly_15 = (By.XPATH,"/html/body/div[23]/div[2]/a[15]")
	friendly_16 = (By.XPATH,"/html/body/div[23]/div[2]/a[16]")
	friendly_17 = (By.XPATH,"/html/body/div[23]/div[2]/a[17]")
	friendly_18 = (By.XPATH,"/html/body/div[23]/div[2]/a[18]")
	friendly_19 = (By.XPATH,"/html/body/div[23]/div[2]/a[19]")
	friendly_20 = (By.XPATH,"/html/body/div[23]/div[2]/a[20]")
	friendly_21 = (By.XPATH,"/html/body/div[23]/div[2]/a[21]")
	friendly_22 = (By.XPATH,"/html/body/div[23]/div[2]/a[22]")
	friendly_23 = (By.XPATH,"/html/body/div[23]/div[2]/a[23]")
	friendly_24 = (By.XPATH,"/html/body/div[23]/div[2]/a[24]")
	friendly_25 = (By.XPATH,"/html/body/div[23]/div[2]/a[25]")
	friendly_26 = (By.XPATH,"/html/body/div[23]/div[2]/a[26]")
	friendly_27 = (By.XPATH,"/html/body/div[23]/div[2]/a[27]")
	friendly_28 = (By.XPATH,"/html/body/div[23]/div[2]/a[28]")
	friendly_29 = (By.XPATH,"/html/body/div[23]/div[2]/a[29]")
	friendly_30 = (By.XPATH,"/html/body/div[23]/div[2]/a[30]")
	friendly_31 = (By.XPATH,"/html/body/div[23]/div[2]/a[31]")
	friendly_32 = (By.XPATH,"/html/body/div[23]/div[2]/a[32]")
	friendly_33 = (By.XPATH,"/html/body/div[23]/div[2]/a[33]")
	friendly_34 = (By.XPATH,"/html/body/div[23]/div[2]/a[34]")
	friendly_35 = (By.XPATH,"/html/body/div[23]/div[2]/a[35]")
	friendly_36 = (By.XPATH,"/html/body/div[23]/div[2]/a[36]")
	friendly_37 = (By.XPATH,"/html/body/div[23]/div[2]/a[37]")
	friendly_38 = (By.XPATH,"/html/body/div[23]/div[2]/a[38]")
	friendly_39 = (By.XPATH,"/html/body/div[23]/div[2]/a[39]")


	#打开页面
	def open(self):
		self.open_page(self.url)

	#查找元素并输入内容	
	def search_content(self,content):
		content1 = self.find_element(*self.bbs_home)
		content1.send_keys(content)

	#找到元素并点击
	def btn_click(self):
		btn1 = self.find_element(*self.bbs_home)
		btn1.click()

	#检查title	
	def check_title(self):
		self.get_title()

	#切换窗体
	def swithc_br(self,browser):
		swithc = self.swithc_browser(browser)

	#关闭当前窗体
	def close_br(self,browser):
		close = self.close_browser(browser)

	#切换浏览器后关闭
	def close_swcl(self,browser):
		close = self.swcl_browser(browser)

	#进入精选帖子
	def bbs_into_jinhua(self):
		home = self.find_element(*self.bbs_jinhua)
		home.click()

	#进入最新帖子
	def bbs_into_news(self):
		page = self.find_element(*self.bbs_news)
		page.click()

	#进入往日十大热帖
	def bbs_into_hot(self):
		new = self.find_element(*self.bbs_hot)
		new.click()

	#进入十大热帖
	def bbs_ten_hot1(self):
		hot1 = self.find_element(*self.ten_hot1)
		hot1.click()

	#进入十大热文
	def bbs_ten_hot2(self):
		hot2 = self.find_element(*self.ten_hot2)
		hot2.click()

	#进入最新帖子
	def bbs_ten_note1(self):
		note1 = self.find_element(*self.new_note1)
		note1.click()

	#进入最新热帖
	def bbs_ten_note2(self):
		note2 = self.find_element(*self.new_note2)
		note2.click()

	#进入简易版车速计算器
	def bbs_tool_1(self):
		tool_1 = self.find_element(*self.tool_1)
		tool_1.click()

	#进入专业车速计算器
	def bbs_tool_2(self):
		tool_2 = self.find_element(*self.tool_2)
		tool_2.click()

	#进入二手车评估计算器
	def bbs_tool_3(self):
		tool_3 = self.find_element(*self.tool_3)
		tool_3.click()

	#进入车险计算器
	def bbs_tool_4(self):
		tool_4 = self.find_element(*self.tool_4)
		tool_4.click()

	#查看经销商
	def bbs_tool_5(self):
		tool_5 = self.find_element(*self.tool_5)
		tool_5.click()

	#查服务站
	def bbs_tool_6(self):
		tool_6 = self.find_element(*self.tool_6)
		tool_6.click()

	#点击卡家二手车
	def bbs_tab_1(self):
		tab_1 = self.find_element(*self.tab_1)
		tab_1.click()

	#点击最新卡车报价在这里
	def bbs_tab_2(self):
		tab_1 = self.find_element(*self.tab_2)
		tab_1.click()

	#点击卡车之家商城能买什么？在这里
	def bbs_tab_3(self):
		tab_2 = self.find_element(*self.tab_3)
		tab_2.click()

	#广告1
	def bbs_ad_1(self):
		ad_1 = self.find_element(*self.ad_1)
		ad_1.click()

	#广告2
	def bbs_ad_2(self):
		ad_2 = self.find_element(*self.ad_2)
		ad_2.click()

	#广告3
	def bbs_ad_3(self):
		ad_3 = self.find_element(*self.ad_3)
		ad_3.click()

	def bbs_ad_4(self):
		ad_4 = self.find_element(*self.ad_4)
		ad_4.click()

	def bbs_ad_5(self):
		ad_5 = self.find_element(*self.ad_5)
		ad_5.click()

	def bbs_hot_car1(self):
		hot_car1 = self.find_element(*self.hot_car1)
		hot_car1.click()

	def bbs_hot_car2(self):
		hot_car2 = self.find_element(*self.hot_car2)
		hot_car2.click()

	def bbs_hot_car3(self):
		hot_car3 = self.find_element(*self.hot_car3)
		hot_car3.click()

	def bbs_car(self):
		car = self.find_element(*self.car)
		car.click()

	def bbs_pr_centre1(self):
		pr_centre1 = self.find_element(*self.pr_centre1)
		pr_centre1.click()

	def bbs_pr_centre2(self):
		pr_centre2 = self.find_element(*self.pr_centre2)
		pr_centre2.click()

	def bbs_pr_centre3(self):
		pr_centre3 = self.find_element(*self.pr_centre3)
		pr_centre3.click()

	def bbs_pr_centre4(self):
		pr_centre4 = self.find_element(*self.pr_centre4)
		pr_centre4.click()

	def bbs_pr_centre5(self):
		pr_centre5 = self.find_element(*self.pr_centre5)
		pr_centre5.click()

	def bbs_pr_centre6(self):
		pr_centre6 = self.find_element(*self.pr_centre6)
		pr_centre6.click()

	def bbs_friendly_1(self):
		friendly_1 = self.find_element(*self.friendly_1)
		friendly_1.click()

	def bbs_friendly_2(self):
		friendly_2 = self.find_element(*self.friendly_2)
		friendly_2.click()

	def bbs_friendly_3(self):
		friendly_3 = self.find_element(*self.friendly_3)
		friendly_3.click()

	def bbs_friendly_4(self):
		friendly_4 = self.find_element(*self.friendly_4)
		friendly_4.click()

	def bbs_friendly_5(self):
		friendly_5 = self.find_element(*self.friendly_5)
		friendly_5.click()

	def bbs_friendly_6(self):
		friendly_6 = self.find_element(*self.friendly_6)
		friendly_6.click()

	def bbs_friendly_7(self):
		friendly_7 = self.find_element(*self.friendly_7)
		friendly_7.click()

	def bbs_friendly_8(self):
		friendly_8 = self.find_element(*self.friendly_8)
		friendly_8.click()

	def bbs_friendly_9(self):
		friendly_9 = self.find_element(*self.friendly_9)
		friendly_9.click()

	def bbs_friendly_10(self):
		friendly_10 = self.find_element(*self.friendly_10)
		friendly_10.click()