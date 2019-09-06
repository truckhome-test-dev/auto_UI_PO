import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class BasePage(object):

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    #打开网页
    def open_page(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    #查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,20).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s"%(self,loc))

    #定义script方法，用于执行js脚本
    def script(self,src):
        self.driver.execute_script(src)

    #输入内容
    def input_base(self,elem,text):
        self.find_element(*elem).send_keys(text)

    #点击元素
    def click_base(self,elem):
        self.find_element(*elem).click()

    #获取title
    def get_title(self):
        return self.driver.title()

    #关闭浏览器
    def teardown(self):
        self.driver.quit()

    #截图
    def screenshot(self,picpath):
        screenpic = self.driver.get_screenshot_as_file(picpath)
        return screenpic

    #清空内容
    def clear_text(self,elem):
        self.driver.find_element(*elem).clear()

    #获取当前页面url
    def get_url(self):
        nowurl = self.driver.current_url()
        return nowurl

    #切换浏览器
    def swithc_browser(self,browser):
        handle = browser.current_window_handle
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle!=handle:
                browser.switch_to_window(newhandle)

    #关闭打开的浏览器
    def close_browser(self,browser):
        handle = browser.current_window_handle
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle == handle:
                browser.switch_to_window(newhandle)
                browser.close()
                browser.switch_to_window(handles[0])

    #切换浏览器后关闭
    def swcl_browser(self,browser):
        handle = browser.current_window_handle
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle!=handle:
                browser.switch_to_window(newhandle)
                browser.close()
                browser.switch_to_window(handles[0])