#coding=utf-8

from base import webbase
from common import conf,logoutput,getxml
class GetRank():
    def __init__(self):
        setup=webbase.SetUp()
        dr=setup.web_setup()
        self.driver=webbase.Web(dr)
        self.cf=conf.Conf()
        self.driver.get_url(self.cf.get_conf_data("taobao")["url"])
        self.lg=logoutput.Logger()
        self.gx=getxml.XmlOperation()

    def click_ljpj(self):
        self.driver.scroll_page()
        ljpj=self.gx.get_xml_data("tb_product","product_ljpl_link")
        self.driver.click(ljpj)


    def close_driver(self):
        self.driver.driver.quit()

    def get_pl(self):
        pl=self.gx.get_xml_data("tb_product","product_pl_text")
        plTest=self.driver.get_elements(pl)
        for p in plTest:
            self.lg.info(p.text)


gf=GetRank()
try:
    gf.click_ljpj()
    gf.get_pl()

except Ellipsis as e:
    gf.lg.error("执行错误！")
finally:
    gf.close_driver()
