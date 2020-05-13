# -*- coding: utf-8 -*-
"""
@author: Faircy
"""

#平台给的包，务必加载，地址：https://github.com/JoinQuant/jqdatasdk/archive/master.zip
from jqdatasdk import * 
import numpy as np
import pandas as pd
import csv
import datetime
import time
import pymysql.cursors


#jqdata登录账号
accountNo = '18515971269'
accountPwd = 'Xt123456'
#数据库地址
db_host = 'localhost'
db_user = 'tcuser'
db_password = '!Q2w3e4r'
db_database = 'tcdb'
db_port = '1601'
db_port_connect = 1601
#当前时间
t = datetime.datetime.now()
nowDate = t.strftime('%Y-%m-%d')
#nowDate = '2015-06-30'
#昨日
yestodayDate = ((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))
#print(yestodayDate)
#文件保存地址
path='D:/00.Python/ExcelDataCsv/'


print('jqdatasdk --> jqdata：导入第三方库 == 成功!! ===')
#依次输入账号、密码，链接到平台数据库
auth(accountNo, accountPwd)
print('\n jqdatasdk --> jqdata：登录账号 == 成功!! ===')

print('\n 获取所有股票数据 -->  开始 --------------------')
########################### 获取所有股票数据 Start ################################
##types：默认为stock,  date: 日期,获取某日期还在上市的股票信息,一个字符串默认值为 None, 表示获取所有日期的股票信息
stocks = get_all_securities(types=['stock'], date = nowDate)
#stocks = get_all_securities(types=['stock'], date=None)
#stocks = get_all_securities(types=['stock'], date=None)[:10]  #查询前10条
print('\n 获取所有股票数据 --> jqdata：读取列表数据 == 成功!! ===')


#excel文件存放位置
xlsxFilePath = (path + 'stocks-' + t.strftime('%Y%m%d%H%M%S')+'.xlsx')
#print(xlsxFilePath)
#写入到Excel中
if len(stocks):
    writer = pd.ExcelWriter(xlsxFilePath)
    stocks.to_excel(writer,'Sheet1')
    writer.save()  
    print('\n 获取所有股票数据 --> Execl：保存为Execl == 成功!! => ' + xlsxFilePath)  
else:
    print('\n 获取所有股票数据 --> Execl：无数据 !!') 
        


# 链接MySQL: 如果当日数据已存在, 则删除当日数据
##host='127.0.0.1',user='***',password='***',db='test'；星号号处填上数据库的对应口令即可，test是你要预先MySql中建立的库
#delDB = pymysql.connect(host='localhost',user='root',password='xt123456',db='python')
delConnect  = pymysql.Connect(
    host=db_host,
    port=db_port_connect,
    user=db_user,
    passwd=db_password,
    db=db_database,
	charset='utf8'
)
cur=delConnect.cursor()
delSq1="delete from t_jqdata_all_stocks where DATE_FORMAT(create_time, '%Y-%m-%d') = '" + t.strftime('%Y-%m-%d') + "'";
#print(delSq1)
try:
   # 执行SQL语句
   cur.execute(delSq1)
   # 提交修改
   delConnect.commit()
   #print("delete OK")                  
except:
   # 发生错误时回滚
   delConnect.rollback()
# 关闭连接
delConnect.close()
print('\n 获取所有股票数据 --> 数据库：清除当日已存数据 == 成功!! ===') 


#从Execl中读取数据
stocksDB = pd.read_excel(xlsxFilePath, sheet_name='Sheet1')
print('\n 获取所有股票数据 --> Execl：读取Execl最新数据 == 成功!! ===') 
if len(stocksDB):
    # 操作DataFrame行列名
    stocksDB.columns.values.tolist()
    #列名为空的更改为 指定列名 stock_code
    stocksDB = stocksDB.rename(columns={'Unnamed: 0':'stock_code'}) 

    # 链接MySQL: 插入保存数据  [conn = create_engine('mysql+mysqldb://用户名:密码@localhost:3306/databasename?charset=utf8') ]
    db = 'mysql+pymysql://'+db_user+':'+db_password+'@'+db_host+':'+db_port+'/'+db_database+'?charset=utf8'
    from sqlalchemy import create_engine
    engine = create_engine(db)
    con = engine.connect()
    # 插入表
    stocksDB.to_sql('t_jqdata_all_stocks',con=engine,if_exists = 'append',index = False,index_label = False)
    #用完close
    con.close()   
    print('\n 获取所有股票数据 --> 数据库：插入当日最新数据 == 成功!! ===') 
else:
    print('\n 获取所有股票数据 --> 数据库：插入当日最新数据 --> 无数据 !! => ')  

print('\n 获取所有股票数据 -->  结束 --------------------')
########################### 获取所有股票数据 End ################################








########################### 上市公司分红送股（除权除息）数据 Start ################################
print('\n 上市公司分红送股（除权除息）数据 -->  开始 --------------------')

#说明 finance.STK_XR_XD.xxx是查询条件,其中xxx是字段名, 多个查询条件用逗号分隔,   limit(3000): 查询多少条
financeResult = query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date == yestodayDate, finance.STK_XR_XD.board_plan_bonusnote != '不分配不转增').limit(3000)
#financeResult = query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date >= '2020-01-01', finance.STK_XR_XD.board_plan_bonusnote != '不分配不转增').limit(3000)
dfDBFinance = finance.run_query(financeResult)
#print(dfDBFinance)


#excel文件存放位置
xlsxFilePathFinance = (path + 'finance-' + t.strftime('%Y%m%d%H%M%S')+'.xlsx')
#print(xlsxFilePath)
#写入到Excel中
if len(dfDBFinance):
    writer = pd.ExcelWriter(xlsxFilePathFinance)
    dfDBFinance.to_excel(writer,'Sheet1')
    writer.save()  
    print('\n 上市公司分红送股（除权除息）数据 --> Execl：保存为Execl == 成功!! => ' + xlsxFilePathFinance)  
else:
    print('\n 上市公司分红送股（除权除息）数据 --> Execl：保存为Execl --> 无数据 !!')    



# 链接MySQL: 如果当日数据已存在, 则删除当日数据
##数据库 配置 host='127.0.0.1',user='***',password='***',db='test'；星号号处填上数据库的对应口令即可，test是你要预先MySql中建立的库
delFinanceDB  = pymysql.Connect(
    host = db_host,
    port = db_port_connect,
    user = db_user,
    passwd = db_password,
    db = db_database,
	charset = 'utf8'
)
curFinance=delFinanceDB.cursor()
delSq1Finance="delete from t_jqdata_finance where DATE_FORMAT(create_time, '%Y-%m-%d') = '" + t.strftime('%Y-%m-%d') + "'";
try:
   # 执行SQL语句
   curFinance.execute(delSq1Finance)
   # 提交修改
   delFinanceDB.commit()                  
except:
   # 发生错误时回滚
   delFinanceDB.rollback()
# 关闭连接
delFinanceDB.close()
print('\n 上市公司分红送股（除权除息）数据 --> 数据库：清除当日已存数据 == 成功!! ===') 


#如果数据不为空,直接插入数据库
if len(dfDBFinance):
    # 链接MySQL: 插入保存数据  [conn = create_engine('mysql+mysqldb://用户名:密码@localhost:3306/databasename?charset=utf8') ]
    dbFinance = 'mysql+pymysql://'+db_user+':'+db_password+'@'+db_host+':'+db_port+'/'+db_database+'?charset=utf8'
    from sqlalchemy import create_engine
    engineFinance = create_engine(dbFinance)
    conFinance = engineFinance.connect()
    # 插入表
    dfDBFinance.to_sql('t_jqdata_finance', con=engineFinance, if_exists = 'append', index = False, index_label = False)
    #用完close
    conFinance.close() 
    print('\n 上市公司分红送股（除权除息）数据 --> 数据库：插入当日最新数据 == 成功!! ===') 
else:
    print('\n 上市公司分红送股（除权除息）数据 --> 数据库：插入当日最新数据 --> 无数据 !! => ')  

print('\n 上市公司分红送股（除权除息）数据 -->  结束 --------------------')

########################### 上市公司分红送股（除权除息）数据 End ################################



















