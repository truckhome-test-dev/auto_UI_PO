#coding=utf-8
import unittest
from testcase.product import *
import HTMLTestRunner
import os
import datetime

#相对路径
testcase_path = ".\\testcase\\bbs"
report_path = ".\\testreport\\bbs.html"
# testcase_path = ".\\testcase\\information"
# report_path = ".\\testreport\\information.html"
# nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# os.makedirs(os.getcwd()+'\\'+'TestReport'+'\\'+nowTime)
# report_path = ".\\testreport\\%s\\bbs.html"% nowTime

def creat_suite():
	uit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test2*_*.py")
	for test_suite in discover:
		for test_case in test_suite:
			uit.addTest(test_case)
	return uit

suite = creat_suite()
fp = open(report_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试结果",description="测试搜索结果")
runner.run(suite)
fp.close()


