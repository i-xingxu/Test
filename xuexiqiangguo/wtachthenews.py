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


        # print(self.driver.driver.page_source)



        # print(el)

        # self.driver.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()


if __name__=="__main__":
        n=News()
        n.click_my()