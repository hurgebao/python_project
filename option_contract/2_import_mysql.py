# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Fri Dec 28 15:39:41 2018

@author: admin
"""
#"合约编码"	"contract_id"	"varchar(8)"
#"数据日期"	"date_date"	"date"
#"合约交易代码"	"contract_tx_id"	"varchar(17)"
#"合约简称"	"contract_symbol"	"varchar(100)"
#"标的券名称及代码"	"security_id"	"varchar(20)"
#"标的券名称"	"security_name"	"varchar(100)"
#"类型"	"call_or_put"	"char(1)"
#"行权价"	"exercise_price"	"decimal(16,4)"
#"合约单位"	"contract_unit"	"decimal(16,4)"
#"期权行权日"	"exercise_date"	"date"
#"行权交收日"	"delivery_date"	"date"
#"到期日"	"expire_date"	"date"
#"新挂"	"new_contract"	"char(1)"
#"涨停价格"	"daily_up_limit_price"	"decimal(16,4)"
#"跌停价格"	"daily_down_limit_price"	"decimal(16,4)"
#"前结算价"	"pre_settle_price"	"decimal(16,4)"
#"调整"	"change_flag"	"char(1)"
#"停牌"	"delist_flag"	"char(1)"
#"市场(沪、深)"	"trade_market"	"char(1)"
#"到期年"	"expire_year"	"int(4)"
#"到期月份：用于显示该合约的到期月份列表"	"expire_month"	"int(11)"
#"实际剩余天数（自然日）"	"actual_remain_days"	"int(11)"
#"本系统到期日：本系统的到期日，提前一个交易日，用于前端显示和交易控制"	"local_remain_days"	"int(11)"
#"本系统到期日：本系统的到期日，提前一个交易日，用于前端显示和交易控制"	"local_expire_date"	"date"
import pymysql 
from optionContract import optioncontract

db = pymysql.connect('10.1.50.105','tcuser','!Q2w3e4r','tcdb')

cur=db.cursor();
oc=optioncontract('1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',1,1,'20181224','20181224','20181224','20181224')

sql = 'insert into tcdb.t_option_contract (' + \
    ',contract_id' + \
    ',contract_tx_id'+ \
    ',contract_symbol'+ \
    ',security_id'+ \
    ',security_name'+ \
    ',call_or_put'+ \
    ',exercise_price'+ \
    ',contract_unit'+ \
    ',new_contract'+ \
    ',daily_up_limit_price'+ \
    ',daily_down_limit_price'+ \
    ',pre_settle_price'+ \
    ',change_flag'+ \
    ',expire_year'+ \
    ',expire_month'+ \
    ',trade_market'+ \
    ',delist_flag'+ \
    ',date_date'+ \
    ',exercise_date'+ \
    ',delivery_date'+ \
    ',expire_date) '+ \
    'values ('+ \
    '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%d,'+ \
   '%d,'+ \
   '%s,'+ \
   '%d,'+ \
   '%d,'+ \
   '%d,'+ \
   '%s,'+ \
   '%d,'+ \
   '%d,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s,'+ \
   '%s'+ \
     ')' % \
    (
     oc.contract_id,  \
     oc.contract_tx_id, \
     oc.contract_symbol, \
     oc.security_id, \
     oc.security_name, \
     oc.call_or_put, \
     oc.exercise_price, \
     oc.contract_unit, \
     oc.new_contract, \
     oc.daily_up_limit_price, \
     oc.daily_down_limit_price, \
     oc.pre_settle_price, \
     oc.change_flag, \
     oc.expire_year, \
     oc.expire_month, \
     oc.trade_market, \
     oc.delist_flag, \
     oc.date_date, \
     oc.exercise_date, \
     oc.delivery_date, \
     oc.expire_date)
print(sql)
cur.execute(sql)
db.commit
cur.close
db.close