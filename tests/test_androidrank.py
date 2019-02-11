#coding=utf-8

import pytest
import allure
from qimai import androidrank
from common import mysql


class TestAndroidRandk():

    testCase=mysql.Mysql().get_mysql_data("安卓榜单")
    def setup_class(self):
        pass


    @pytest.allure.feature("安卓榜单")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("url,expect", testCase)
    def test_android_rank(self,url,expect):
        ar=androidrank.GetAndroidRank()
        ar.open_url(url)
        self.dr=ar.driver
        res=ar.get_table_count()
        if res>1:
            flag="True"
        else:
            flag="False"
        assert expect==flag



    def teardown(self):
        self.dr.driver.quit()


