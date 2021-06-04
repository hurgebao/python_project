# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:35:38 2021

@author: shi
"""
from jqdatasdk import * 
import numpy as np
import pandas as pd
import csv
import datetime
import time
import pymysql.cursors

def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday.strftime('%Y-%m-%d')

#jqdata登录账号
accountNo = '18515971269'
accountPwd = 'Xt123456'
#数据库地址
db_host = 'localhost'
db_user = 'tcuser'
db_password = '!Q2w3e4r'
db_database = 'tcdb'
db_port = '33306'
db_port_connect = 33306

t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#nowDate = t.strftime('%Y-%m-%d')
#nowDate='2021-06-03'
nowDate=getYesterday()
auth(accountNo, accountPwd)

#全量初始化
dfDBFinance=finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.link_id!='310005',finance.STK_HK_HOLD_INFO.share_ratio>=3,finance.STK_HK_HOLD_INFO.day==nowDate).order_by(finance.STK_HK_HOLD_INFO.day.desc()))

#dfDBFinance=finance.run_query(query(finance.STK_HK_HOLD_INFO).filter(finance.STK_HK_HOLD_INFO.link_id!='310005',finance.STK_HK_HOLD_INFO.share_ratio>=4,finance.STK_HK_HOLD_INFO.day==nowDate).order_by(finance.STK_HK_HOLD_INFO.day.desc()))



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
delSq1Finance="delete from jq_hk_hold_info where DATE_FORMAT(day, '%Y-%m-%d') = '" + nowDate + "'";
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
print('\n'+t+'  上市公司北向资金持仓数据 --> 数据库：清除当日'+nowDate+'已存数据 == 成功!! ===') 


#如果数据不为空,直接插入数据库
if len(dfDBFinance):
    # 链接MySQL: 插入保存数据  [conn = create_engine('mysql+mysqldb://用户名:密码@localhost:3306/databasename?charset=utf8') ]
    dbFinance = 'mysql+pymysql://'+db_user+':'+db_password+'@'+db_host+':'+db_port+'/'+db_database+'?charset=utf8'
    from sqlalchemy import create_engine
    engineFinance = create_engine(dbFinance)
    conFinance = engineFinance.connect()
    # 插入表
    dfDBFinance.to_sql('jq_hk_hold_info', con=engineFinance, if_exists = 'append', index = False, index_label = False)
    #用完close
    conFinance.close() 
    print('\n'+t+' 上市公司北向资金持仓数据 --> 数据库：插入当日最新数据 == 成功!! ===') 
else:
    print('\n'+t+' 上市公司北向资金持仓数据 --> 数据库：插入当日最新数据 --> 无数据 !! => ')  

print('\n'+t+' 上市公司北向资金持仓数据 -->  结束 --------------------')

########################### 上市公司北向资金持仓数据 End ################################
