#ucoding=utf-8
import xlrd
from common import mysql
from common import logoutput

class Upload():

    def __init__(self):
        try:
            data = xlrd.open_workbook('case.xlsx')
            self.table=data.sheet_by_index(0)
            self.db=mysql.Mysql()
            self.db.connect_mysql()
            self.lg=logoutput.Logger()

        except Exception as e:
            self.lg.error(e)
            self.lg.error("打开Excel表格失败！")

    def insert_case_name(self,data):
        res=self.casename_is_repetition(data)
        if res !=0:
            try:
                # cols=self.get_casename()
                for i in range(0,len(res)):
                    sql="insert into case_name(case_name,pid) values (\"{}\",\"{}\")".format(res["nameList"][i],res["pidList"][i])
                    self.db.cur.execute(sql)
                    self.lg.info("插入一条用例名称：{}".format(res["nameList"][i]))
            except self.db.IntegrityError as e:
                self.lg.error(e)
        else:
            return 2
        # except Exception as e:
        #     self.lg.error(e)
        # self.db.close_connect()

    def get_case_nameandpid(self):
        colsName=self.table.col_values(1)
        colsPlatform=self.table.col_values(0)
        data={}
        nameList=[]
        pidList=[]

        for name in colsName:
            nameList.append(name)

        for pid in colsPlatform:
            pidList.append(pid)
        newPidList=[]
        for num in pidList[1:]:
            newPidList.append(int(num))

        data["nameList"]=nameList[1:]
        data["pidList"]=newPidList
        return data

    # def get_casenameid(self):

    # def get_platform_id(self):
    #     cols=self.table.col_values(0)
    #     data=[]
    #     for col in cols:
    #         data.append(col)
    #     res=[]
    #     for d in data[1:]:
    #         res.append(int(d))
    #     return res



    def casename_is_repetition(self,data):
        caseName=data["nameList"]
        pidList=data["pidList"]
        data=[]
        newCaseName=[]
        newData={}
        # copyCaseName=casename.copy()
        # print(len(casename))
        i=0
        # iList=[]
        try:
            for name in caseName:
                sql="select case_name from case_name where case_name=\"{}\"".format(name)
                self.db.cur.execute(sql)
                selRes=self.db.cur.fetchone()
                if selRes is not None:
                    data.append(selRes)
                    pidList.remove(selRes)
                    # iList.append(i)
                    self.lg.info("含有重复用例名称{}".format(selRes))
                else:
                    newCaseName.append(name)
                i+=1
            # for j in iList:
            #     pidList.pop(j)
            if len(newCaseName) !=0:
                newData["nameList"]=newCaseName
                newData["pidList"]=pidList
                return newData
            else:
                return 0
        except Exception as e:
            self.lg.error(e)





up=Upload()
# name=up.get_case_name()
up.insert_case_name(up.get_case_nameandpid())
# print(name)
# up.casename_is_repetition(name)
up.db.close_connect()