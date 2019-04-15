# coding=utf-8

from base import webbase
from common import conf,logoutput,getxml

class GetAndroidSearchResult():
    def __init__(self):
        setup=webbase.SetUp()
        dr=setup.web_setup()
        self.driver=webbase.Web(dr)
        self.cf=conf.Conf()
        # self.driver.get_url("https://www.qimai.cn/search/android/market/3/search/%E5%BE%AE%E4%BF%A1")
        self.lg=logoutput.Logger()
        self.getxml=getxml.XmlOperation()


    def get_url(self,url):

        self.driver.get_url(url)


    def get_list(self):

        elementResultList=self.getxml.get_xml_data("android_search_page","android_search_list")
        if self.driver.wait_element(elementResultList):
            resultList=self.driver.get_elements(elementResultList)
            # print(len(resultList))
            if len(resultList)>2:
                return True
        else:
            self.driver.get_screenshot()
            return False

    def get_tittle(self):

        elementTittle=self.getxml.get_xml_data("android_search_page","android_search_tittle")
        self.driver.wait_element(elementTittle)
        tittle=self.driver.get_text(elementTittle)
        return tittle




if __name__=="__main__":
    g=GetAndroidSearchResult()
    g.get_url("https://www.qimai.cn/search/android/market/3/search/%E5%BE%AE%E4%BF%A1")
    print(g.get_list())
    print(g.get_tittle())
