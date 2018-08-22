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
        plText=self.driver.get_elements(pl)
        for p in plText:
            self.lg.info(p.text)

    def get_color(self):
        c=self.gx.get_xml_data("tb_product","product_color_text")
        colorText=self.driver.get_elements(c)
        for p in colorText:
            try:
                data=p.text
                data=data.split("\n")
                color=data[0].split("：")[-1]
                jinghanliang=data[-1].split("：")[-1]
                self.lg.info(color)
                self.lg.info(jinghanliang)
            except Exception as  e:
                self.lg.error(e)

    def click_next(self):
        n=self.gx.get_xml_data("tb_product","product_next_link")
        self.driver.click(n)

    def is_next_click(self):
        n = self.gx.get_xml_data("tb_product", "product_next_link")
        attr=self.driver.get_attribute(n,"class")
        if attr=="rate-page-next":
            return  False
        else:
            return  True


gf=GetRank()
try:
    while (1):
        gf.click_ljpj()
        gf.get_pl()
        gf.get_color()
        gf.click_next()
        flag=gf.is_next_click()
        if flag:
            pass
        else:
            break

except Ellipsis as e:
    gf.lg.error("执行错误！")
finally:
    gf.close_driver()
