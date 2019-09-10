# coding=utf-8
import unittest
from testcase.product import *
import HTMLTestRunner
import os
import datetime
from multiprocessing import Pool


# 相对路径
# testcase_path = ".\\testcase\\bbs"
# nowTime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# os.makedirs(os.getcwd()+'\\'+'TestReport'+'\\'+nowTime)
# report_path = ".\\testreport\\%s\\bbs.html"% nowTime
# report_path = ".\\testreport\\bbs.html"

def creat_suite(testcase_path):
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test*_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


def run(testcase_path, report_path):
    suite = creat_suite(testcase_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试结果", description="测试搜索结果")
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    # case目录和报告的目录，大列表中多个小列表
    L = [[".\\testcase\\bbs", ".\\testreport\\bbs.html"],
         [".\\testcase\\information", ".\\testreport\\information.html"]]
    # 进程数，大列表中有几个小列表就填几
    pool = Pool(2)
    # 下面的内容不要改
    for i in L:
        testcase_path = i[0]
        report_path = i[1]
        pool.apply_async(func=run, args=(testcase_path, report_path))
    pool.close()
    pool.join()
