# coding=utf-8
import time
import xlrd
from common import conf
from common import logoutput

class Time():
    '''
    工具模块，时间类
    '''
    def get_now_time(self):
        '''
        获取当前时间，以字符串格式返回
        :return:
        '''
        nowtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        return nowtime

class Excel():
    '''
    用来操作Excel
    '''
    def __init__(self):
        self.lg=logoutput.Logger()

    def excelRead(self,path):
        CONF_NAME_EXCELPATH="ExcelPath"
        CONF_NAME_XLSNAME="xlsname"
        CONF_NAME_SHEETNAME="sheetname"

        '''

        :param path: 配置文件所在路径
        :return:返回table
        '''
        try:
            cf=conf.Conf()
            d=cf.get_conf_data(CONF_NAME_EXCELPATH)
            # os.chdir(d["xfpath"])
            data = xlrd.open_workbook(CONF_NAME_XLSNAME)
            table = data.sheet_by_name(CONF_NAME_SHEETNAME)  #通过名称获取
            return table
        except Exception as e:
            self.lg.error(e)