# coding=utf-8
import time

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
