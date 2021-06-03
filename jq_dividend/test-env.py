from jqdatasdk import *
import datetime
auth('18515971269', 'Xt123456')
# 查询是否连接成功
is_auth = is_auth()
print(is_auth)
q_count=get_query_count()
print(q_count)
t = datetime.datetime.now()
nowDate = t.strftime('%Y-%m-%d')
fdata=finance.run_query(query(finance.STK_XR_XD).filter(finance.STK_XR_XD.a_registration_date == '2021-03-23').order_by(finance.STK_XR_XD.report_date).limit(10))
print(fdata)
