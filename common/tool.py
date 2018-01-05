# coding=utf-8
import time
import xlrd
import xlwt
import os
from common import conf

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
    def excelRead(self,path):
        '''

        :param path: 配置文件所在路径
        :return:返回table
        '''
        try:
            cf=conf.Conf()
            d=cf.get_conf_data(path,"excelPath")
            # os.chdir(d["xfpath"])
            data = xlrd.open_workbook(d["xlsname"])
            table = data.sheet_by_name(d["sheetname"])  #通过名称获取
            return table
        except Exception as e:
            print(e)