#coding=utf-8

from base import appbase
from common import getxml
import time

class News():

    def __init__(self):

        setup=appbase.SetUp()
        dr=setup.app_setup()
        self.driver=appbase.App(dr)
        gx=getxml.XmlOperation()
        self.gx=gx

    def click_my(self):

        # time.sleep(10)

        sixiangElement=self.gx.get_xml_data("news_page","my_icon")
        self.driver.wait_element(sixiangElement)
        self.driver.click(sixiangElement)
        # self.driver.driver.switch_to.context('WEBVIEW')
        self.switch_webview()
        myPointElement=self.gx.get_xml_data("news_page","study_point_icon")
        self.driver.click(myPointElement)

    def switch_webview(self):

        contextList=self.driver.get_contests()
        if len(contextList)==2:
            webview=contextList[1]
            native=contextList[0]
        # print(self.driver.driver.contexts)
            self.driver.driver.switch_to.context(webview)
        else:
            return False

    def get_news_list(self):
        elemYaowen=self.gx.get_xml_data("news_page","yaowen_link")
        self.driver.wait_element(elemYaowen)
        self.driver.click(elemYaowen)
        elemNewsList=self.gx.get_xml_data("news_page","news_list")
        self.driver.wait_element(elemNewsList)
        newsList = self.driver.get_elements(elemNewsList)
        print(len(newsList))


if __name__=="__main__":
        n=News()
        try:
            # n.click_my()
            n.get_news_list()
        finally:
            n.driver.driver.quit()

