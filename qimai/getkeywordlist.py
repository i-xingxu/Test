#coding=utf-8
import time
from base import webbase
from common import conf,logoutput,getxml
class GetKeywordlist():
    def __init__(self):
        setup=webbase.SetUp()
        dr=setup.web_setup()
        self.driver=webbase.Web(dr)
        self.cf=conf.Conf()
        self.driver.get_url(self.cf.get_conf_data("qimai")["keywordlist"])
        self.lg=logoutput.Logger()
        self.getxml=getxml.XmlOperation()

    def get_keywords(self):

        keywords=self.getxml.get_xml_data("web_page","web_keywordlist_keyword")
        self.driver.wait_element(keywords)
        wordList=self.driver.get_text(keywords,waittime=2).split('\n')
        newWordList=[]
        for i in range(27,len(wordList),5):
            newWordList.append(wordList[i])

        newWordList.pop(-1)
        self.lg.info(newWordList)
        return newWordList
    def click_next(self):

        n=self.getxml.get_xml_data("web_page","web_keywordlist_nextbtn")
        # nd=self.getxml.get_xml_data("web_page","web_keywordlist_nextbtndisable")
        nextClass=self.driver.get_attribute(n,"class")
        if n["value"]==nextClass:
            self.driver.click(n)
            return 1
        else:
            # self.driver.click(n)
            return 0


    def get_all_keyword(self):
        allKeyword=[]
        self.get_keywords()
        while self.click_next()==1:
            time.sleep(1)
            key=self.get_keywords()
            for k in key:
                allKeyword.append(k)

        self.lg.info(allKeyword)
        return allKeyword




gk=GetKeywordlist()
gk.get_all_keyword()
gk.driver.driver.quit()