# coding=utf-8
from common import conf
from common import tool
from common import logoutput
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import allure
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class SetUp():
    '''
    appbase中setup类，用来启动app，返回一个driver对象
    '''

    def __init__(self):
        # self.CONF_PATH = CONF_PATH
        self.lg=logoutput.Logger()
        self.cf = conf.Conf()

    def web_setup(self):
        try:
            CONF_FIREFOX="FirefoxPath"
            CONF_FIR_PATH_NAME="path"
            print(self.cf.get_conf_data(CONF_FIREFOX)[CONF_FIR_PATH_NAME])
            binary = FirefoxBinary(self.cf.get_conf_data(CONF_FIREFOX)[CONF_FIR_PATH_NAME])
            # binary = FirefoxBinary(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            driver=webdriver.Firefox(firefox_binary=binary)
            return driver
        except Exception as e:
            self.lg.error(e)
class Web():
    def __init__(self,driver):
        CONF_NAME_SCRPATH="ScreenShotPath"
        CONF_NAME_PATH="path"
        self.lg=logoutput.Logger()
        self.driver = driver
        cf=conf.Conf()
        self.SCR_PATH = cf.get_conf_data( CONF_NAME_SCRPATH)[CONF_NAME_PATH]

    def get_element(self, elementinfo, waittime=1):
        '''
        获取元素对象，传入元素信息返回元素
        :param elementinfo:
        :param waittime:
        :return:
        '''
        time.sleep(waittime)
        try:
            element = self.driver.find_element(elementinfo["type"], elementinfo["value"])
            if element == None:
                self.lg.info("定位元素失败:%s" % elementinfo["desc"])
                self.driver.quit()
            else:
                return element
            # for i in range(60):
            #     if i>=59:
            #         self.lg.error("定位元素超时：%s"%elementinfo["desc"])
            #     try:
            #         if self.driver.find_element(elementinfo["type"], elementinfo["value"]):
            #             return self.driver.find_element(elementinfo["type"], elementinfo["value"])
            #     except:
            #         self.lg.error("未找到元素：%s"%elementinfo["desc"])
        except Exception as e:
            self.lg.error(e)
            self.lg.error("未定位到元素:%s" % elementinfo["desc"])
            self.get_screenshot()

    def wait_element(self, elementinfo, waittime=8):
        '''
        等待元素出现
        :param elementinfo:
        :param waittime:
        :return:
        '''
        self.get_element(elementinfo)
        try:
            WebDriverWait(self.driver, waittime).until(
                lambda x: x.find_element(elementinfo["type"], elementinfo["value"]))
            self.lg.info("元素出现：%s" % elementinfo["desc"])
            return True
        except Exception as e:
            self.lg.error(e)
            self.lg.error("元素未出现：%s" % elementinfo["desc"])
            self.get_screenshot()
            return False

    def click(self, elementinfo,waittime=1):
        '''
        点击操作
        :param elementinfo:
        :return:
        '''
        e = self.get_element(elementinfo,waittime)
        try:
            e.click()
            self.lg.info("点击：%s" % elementinfo["desc"])
        except Exception as e:
            self.lg.error(e)
            self.lg.error("未点击成功：%s" % elementinfo["desc"])
            self.get_screenshot()

    def get_elements(self, elementinfo, waittime=1):
        '''
        定位一组对象
        :param elementinfo:
        :param waittime:
        :return:
        '''
        time.sleep(waittime)
        try:
            element = self.driver.find_elements(elementinfo["type"], elementinfo["value"])
            if element == None:
                self.lg.info("定位元素失败:%s" % elementinfo["desc"])
                self.driver.quit()
            else:
                return element
        except Exception as e:
            self.lg.error(e)
            self.lg.error("未定位到元素:%s" % elementinfo["desc"])
            self.get_screenshot()

    def get_screenshot(self):
        '''
        获取截图
        :return:
        '''
        try:
            t = tool.Time()
            picNam = t.get_now_time() + ".jpg"
            self.lg.info("保存图片：%s" % picNam)
            os.chdir(self.SCR_PATH)
            self.driver.save_screenshot(picNam)
            f = open(picNam,'rb').read()
            allure.attach('This is a picture',f,allure.attach_type.PNG)
        except Exception as e:
            self.lg.error(e)
            self.lg.error("获取截图失败！")

    def send_keys(self, elmentinfo, data):
        '''
        输入内容
        :param elmentinfo:
        :param data:
        :return:
        '''

        try:
            self.lg.info("输入内容：%s" % data)
            self.get_element(elmentinfo).send_keys(data)
        except Exception as e:
            self.lg.error(e)
            self.lg.error("输入内容失败！")
    def get_url(self,url):
        try:
            self.driver.set_page_load_timeout(30)
            self.lg.info("打开url:%s"%url)
            self.driver.get(url)
        except Exception as e:
            self.lg.error(e)
            self.lg.error("打开url失败！")
            self.get_screenshot()

    def get_text(self,elementinfo,waittime=1):

        try:
            self.lg.info("获取：“{}”的值".format(elementinfo["desc"]))
            return self.get_element(elementinfo,waittime).text

        except Exception as e:
            self.lg.error(e)
            self.lg.error("未获取到：“{}”的值".format(elementinfo["desc"]))


