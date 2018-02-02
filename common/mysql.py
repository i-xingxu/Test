# coding=utf-8
import pymysql
from common import conf
from common import logoutput

class Mysql():
    '''
    Mysql类
    '''
    def __init__(self):
        self.lg=logoutput.Logger()
        self.cf=conf.Conf()
        self.IntegrityError=pymysql.IntegrityError

    def connect_mysql(self):
        CONF_NAME_SQL="SqlInfo"
        CONF_NAME_IP="ip"
        CONF_NAME_PORT="port"
        CONF_NAME_USR="usr"
        CONF_NAME_PSW="password"
        CONF_NAME_DB="database"
        '''
        连接数据库方法,传入配置文件地址，获取连接数据库信息，返回游标对象
        :param mysqinfo: 数据库连接信息
        :return:
        '''

        mysqlInfo=self.cf.get_conf_data(CONF_NAME_SQL)
        try:
            db = pymysql.connect(host=mysqlInfo[CONF_NAME_IP], port=int(mysqlInfo[CONF_NAME_PORT]), user=mysqlInfo[CONF_NAME_USR],
                                 passwd=mysqlInfo[CONF_NAME_PSW], db=mysqlInfo[CONF_NAME_DB], charset='utf8')
            self.cur = db.cursor()
            self.lg.info("成功连接%s数据库" % mysqlInfo["ip"])

        except Exception as e:
            self.lg.error("数据库连接失败！")
            self.lg.error(e)

    def close_connect(self):
        '''
        关闭数据库连接
        :return:
        '''
        try:
            self.cur.close()
            self.lg.info("成功关闭连接！")
        except Exception as e:
            self.lg.error(e)

    def get_mysql_data(self, casename):
        CONF_SEC_PLAT="Platform"
        CONF_OPT_PLAT="platform"
        platNum=self.cf.get_conf_data(CONF_SEC_PLAT)[CONF_OPT_PLAT]
        '''
        获取数据库数据
        :return:
        '''
        # select id from case_name where case_name=casename
        sql = "select id from case_name where case_name=\'" + casename + "\'"+"and pid="+platNum
        try:
            self.cur.execute(sql)
            caseId = self.cur.fetchone()[0]
            dataSql = "select * from test_data where cid=" + str(caseId)
            try:
                self.cur.execute(dataSql)
                data = self.cur.fetchall()
                caseDatas = []
                for d in data:
                    caseData = []
                    for i in range(0, len((d[2]).split(";"))):
                        caseData.append((d[2]).split(";")[i])
                    caseData.append(d[3])
                    caseDatas.append(caseData)
                return caseDatas
            except Exception as a:
                self.lg.error(a)
                self.lg.error("执行sql语句%s出错" % dataSql)
        except Exception as e:
            self.lg.error(e)
            self.lg.error("执行sql语句%s出错" % sql)


# mysqlinfo = {"ip": "192.168.2.157", "port": "3306", "usr": "root", "password": "root", "database": "autotest"}

# m = Mysql()
# c = m.connect_mysql()
# data = m.get_mysql_data("测试")
# print(data)
# m.close_connect()
