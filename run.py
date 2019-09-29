#coding=utf-8
import unittest
from testcase.product import *
import HTMLTestRunner
import os
import datetime
import time
import sys
from multiprocessing import Pool
import pysnooper

def creat_suite(testcase_path):
	uit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test*_*.py")
	for test_suite in discover:
		for test_case in test_suite:
			uit.addTest(test_case)
	return uit

# @pysnooper.snoop()
def run(testcase_path, report_path,title):
    suite = creat_suite(testcase_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title)
    runner.run(suite)
    fp.close()




if __name__ == '__main__':
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.makedirs(os.getcwd()+'\\'+'TestReport'+'\\'+nowTime)
    # case目录和报告的目录，大列表中多个小列表
    L = [[".\\testcase\\bbs", ".\\testreport\\%s\\bbs.html"%nowTime,"论坛"],
         [".\\testcase\\information", ".\\testreport\\%s\\information.html"%nowTime,"资讯"],
         [".\\testcase\\product", ".\\testreport\\%s\\product.html"%nowTime,"产品库"]]
    # 进程数，大列表中有几个小列表就填几
    pool = Pool(3)
    # 下面的内容不要改
    for i in L:
        testcase_path = i[0]
        report_path = i[1]
        title = i[2]
        pool.apply_async(func=run, args=(testcase_path, report_path,title))
    pool.close()
    pool.join()
    os.system(r'C:\Users\dellmn\Desktop\web自动化\web_at\killchrome.bat')