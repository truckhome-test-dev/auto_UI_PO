#coding=utf-8
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest

class BasePage():

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
    def click_base(self,*elem):
        self.find_element(*elem).click()

    #获取title
    def get_title(self):
        return self.driver.title

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

    #切换页签
    def swithc_browser(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for newhandle in handles:
            if newhandle!=handle:
                self.driver.switch_to_window(newhandle)

    #关闭打开的页签
    def close_browser(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for newhandle in handles:
            if newhandle == handle:
                self.driver.switch_to_window(newhandle)
                self.driver.close()
                self.driver.switch_to_window(handles[0])

    #切换浏览器后关闭
    def swcl_browser(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for newhandle in handles:
            if newhandle!=handle:
                self.driver.switch_to_window(newhandle)
                self.driver.close()
                self.driver.switch_to_window(handles[0])

    #返回上一页
    def backpage(self):
        self.driver.back() 

    #下一页
    def forwardpage(self):
        self.driver.forward()

    #刷新本页面
    def refreshpage(self):
        self.driver.refresh()

    #获取当前页面的url
    def get_url(self):
        url = self.current_url()
        return url

    #判断页面元素是否存在
    def elem_display(self,num,*elem):
        if num == 1:
            self.swithc_browser()  

        ele = self.find_element(*elem)
        r = ele.is_displayed()

        if num == 1:
            self.close_browser()
        elif num == 2:
            self.backpage()
        return r


