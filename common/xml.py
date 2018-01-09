# coding=utf-8
import xml.etree.cElementTree
from common import  conf

class XmlOperation():
    """
    操作Xml文件
    """
    def get_xml_data(self, page, element):
        '''
        获取xml数据，传入二级节点名称，三级节点名称，xml文件路径，以字典格式返回
        :param page:二级页面名称
        :param element:元素名称
        :param path:xml文件地址
        :return: 返回元素信息
        '''
        try:
            cf=conf.Conf()
            print("从配置文件获取xml地址")
            p=cf.get_conf_data("XmlPath")
            x = xml.etree.cElementTree.parse(p["path"])
            root = x.getroot()
            print("获取节点信息")
            a = root.find(page)
            b = a.find(element)
            return b.attrib
        except Exception as e:
            print(e)

# x = XmlOperation()
# a = x.get_xml_data("index", "usr_in", r"D:\svn\Test\自动化测试\frame\UItest\code\demo\demo\object\fzbd.xml")
# print(a)
