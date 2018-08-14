#coding=utf-8

from base import webbase
from common import conf,logoutput
class GetRank():
    def __init__(self):
        setup=webbase.SetUp()
        dr=setup.web_setup()
        self.driver=webbase.Web(dr)
        self.cf=conf.Conf()
        self.driver.get_url(self.cf.get_conf_data("qimai")["RankUrl"])
        self.lg=logoutput.Logger()

    def close_driver(self):
        self.driver.driver.quit()

    def get_page_source(self):
        return  self.driver.get_page_source()

gf=GetRank()
try:
    print(gf.get_page_source())

except Ellipsis as e:
    gf.lg.error("执行错误！")
finally:
    gf.close_driver()
