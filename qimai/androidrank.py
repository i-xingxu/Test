# coding=utf-8

from base import webbase
from common import conf,logoutput,getxml,mysql
class GetAndroidRank():
    def __init__(self):
        setup=webbase.SetUp()
        dr=setup.web_setup()
        self.driver=webbase.Web(dr)
        self.cf=conf.Conf()
        # self.driver.get_url(self.cf.get_conf_data("qimai")["keywordlist"])
        self.lg=logoutput.Logger()
        self.getxml=getxml.XmlOperation()


    def open_url(self,url):

        self.driver.get_url(url)

    def get_table_count(self):
        rankTableElement=self.getxml.get_xml_data("android_rank_page","rank_table")
        rankTable=self.driver.get_elements(rankTableElement,waittime=3)
        rankTittleElement=self.getxml.get_xml_data("android_rank_page","rank_tittle")
        rankTittle=self.driver.get_text(rankTittleElement)
        self.lg.info(rankTittle)
        # for r in rankTable: print(r.text)
        return len(rankTable)



if __name__=="__main__":
    g=GetAndroidRank()
    g.open_url("https://www.qimai.cn/rank/marketRank/market/10/category/1/country/cn/collection/topselling_free")
    print(g.get_table_count())
