# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Fri Dec 28 16:57:13 2018

@author: admin
"""
class optioncontract:
    contract_id=''
    date_date=''
    contract_tx_id=''
    contract_symbol=''
    security_id=''
    security_name=''
    call_or_put=''
    exercise_price=0
    contract_unit=0
    exercise_date=''
    delivery_date=''
    expire_date=''
    new_contract=''
    daily_up_limit_price=''
    daily_down_limit_price=''
    pre_settle_price=''
    change_flag=''
    delist_flag=''
    trade_market=''
    expire_year=''
    expire_month=''
    def __init__(self,contract_id,date_date,contract_tx_id,
                 contract_symbol,
                 security_id,security_name,
                 call_or_put,exercise_price,
                 contract_unit,exercise_date,delivery_date,expire_date,
                 new_contract,
                 daily_up_limit_price,daily_down_limit_price,
                 pre_settle_price,change_flag,delist_flag,
                 trade_market,expire_year,expire_month):
        self.contract_id=contract_id
        self.date_date= date_date
        self.contract_tx_id=contract_tx_id 
        self.contract_symbol= contract_symbol
        self.security_id =security_id 
        self.security_name=security_name 
        self.call_or_put = call_or_put
        self.exercise_price = exercise_price
        self.contract_unit= contract_unit
        self.exercise_date =exercise_date 
        self.delivery_date= delivery_date
        self.expire_date=expire_date 
        self.new_contract =new_contract 
        self.daily_up_limit_price= daily_up_limit_price
        self.daily_down_limit_price=daily_down_limit_price 
        self.pre_settle_price=pre_settle_price 
        self.change_flag= change_flag
        self.delist_flag=delist_flag 
        self.trade_market= trade_market
        self.expire_year=expire_year 
        self.expire_month= expire_month