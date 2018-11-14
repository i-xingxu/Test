#coding=utf-8

import time
from base import webbase
from common import conf,logoutput,getxml,mysql

class Trousers():

    def __init__(self):
        setup = webbase.SetUp()
        dr = setup.web_setup()
        self.driver = webbase.Web(dr)
        self.cf = conf.Conf()
        self.driver.get_url(self.cf.get_conf_data("taobao")["trousersurl"])
        self.lg = logoutput.Logger()
        self.gx = getxml.XmlOperation()
        self.db = mysql.Mysql()
        self.db.connect_mysql()
        self.cur = self.db.cur

    def create_tables(self):
        '''
        创建表
        :return:
        '''
        stime = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        sql_1 = """create table product_info{nowtime} (id int(5) NOT NULL auto_increment,biaoti varchar(500),price char (10),pic_src varchar (500),store_url varchar (5000),PRIMARY KEY (`id`))""".format(
            nowtime=stime)
        self.cur.execute(sql_1)
        self.tableName="product_info"+str(stime)

    def get_data(self):
        self.scroll_page()
        time.sleep(3)
        t=self.gx.get_xml_data("trousers","product_picture")
        tFather=self.gx.get_xml_data("trousers","procuct_pic_father")
        elements=self.driver.get_elements(t)
        elementsFather=self.driver.get_elements(tFather)
        for i in range(0,len(elements)):
            biaoti=elements[i].get_attribute("alt")
            pic_src=elements[i].get_attribute("data-src")
            store_url=elementsFather[i].get_attribute("href")
            price=elementsFather[i].get_attribute("trace-price")
            self.insert_table(biaoti,price,pic_src,store_url)

    def insert_table(self,biaoti,price,pic_src,store_url):
        self.lg.info(biaoti)
        self.lg.info(price)
        self.lg.info(pic_src)
        self.lg.info(store_url)

        sql="insert into {tablename}(biaoti,price,pic_src,store_url) values (\'{biaoti}\',\'{price}\',\'{pic_src}\',\'{store_url}\');".format(tablename=self.tableName,biaoti=biaoti,price=price,pic_src=pic_src,store_url=store_url)
        self.cur.execute(sql)
        self.db.db.commit()

    def click_next(self):
        n=self.gx.get_xml_data("trousers","next_btn")
        self.driver.click(n)

    def is_next_click(self):
        n = self.gx.get_xml_data("trousers", "next_btn_isnoclick")
        f=self.driver.is_exist(n)
        if f:
            return False
        else:
            return True

    def close_driver(self):
        self.driver.driver.quit()
        self.db.close_connect()

    def scroll_page(self):
        self.driver.scroll_page()

    def enter_taobao(self):
        i=self.gx.get_xml_data("trousers","index_input")
        b=self.gx.get_xml_data("trousers","index_search")
        self.driver.send_keys(i,"男裤 抽绳")
        self.driver.click(b)



if __name__=="__main__":
    trousers=Trousers()
    trousers.create_tables()
    trousers.enter_taobao()

    try:
        while (1):
            trousers.get_data()
            flag=trousers.is_next_click()

            if flag:
                pass
            else:
                break

            trousers.click_next()
    except Exception as e:
        trousers.lg.error(e)
    finally:
        trousers.close_driver()
