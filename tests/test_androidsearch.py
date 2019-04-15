#coding=utf-8

import pytest
import allure
from qimai import androidsearch
from common import mysql


class TestAndroidSearch():

    testCase=mysql.Mysql().get_mysql_data("安卓搜索")
    def setup_class(self):
        print("开始测试")


    @pytest.allure.feature("安卓搜索")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("url,expect", testCase)
    def test_android_rank(self,url,expect):
        ar=androidsearch.GetAndroidSearchResult()
        ar.get_url(url)
        self.dr=ar.driver
        res=ar.get_list()
        assert expect==str(res)



    def teardown(self):
        self.dr.driver.quit()