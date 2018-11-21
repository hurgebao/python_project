select * from monitordb.m_securities_trader_site_info sts left join monitordb.a_securities_trader_info sti on sts.securities_trader_name=sti.sec_trader_name;

select * from  monitordb.m_securities_trader_site_info;


update monitordb.m_securities_trader_site_info set securities_trader_name='太平洋证券' where securities_trader_name='太平洋';

update monitordb.m_securities_trader_site_info set securities_trader_name='新时代证券' where securities_trader_name='新时代';

update monitordb.m_securities_trader_site_info set securities_trader_name='西藏同信证券' where securities_trader_name='西藏同信';
update monitordb.m_securities_trader_site_info set securities_trader_name='中泰证券' where securities_trader_name='齐鲁证券';
update monitordb.m_securities_trader_site_info set securities_trader_name='联储证券' where securities_trader_name='众成证券';


update monitordb.m_securities_trader_site_info sts,monitordb.a_securities_trader_info sti 
set sts.securities_trader_no=sti.sec_trader_no
where sts.securities_trader_name=sti.sec_trader_name;


select * from monitordb.m_securities_trader_site_info sts 
left join monitordb.a_securities_trader_info sti on sts.securities_trader_no=sti.sec_trader_no
where  sts.securities_trader_name!=sti.sec_trader_name;

select * from monitordb.m_securities_trader_software_url;
desc monitordb.m_securities_trader_software_url;
select * from monitordb.a_securities_trader_info;

select * from monitordb.m_securities_trader_software_url   m1 
inner join monitordb.a_securities_trader_info m2 on
 m1.securities_trader_no=m2.sec_trader_no
 where  m1.securities_trader_name<>m2.sec_trader_name
;
 
 update monitordb.m_securities_trader_software_url m1,monitordb.a_securities_trader_info m2
 set  m1.securities_trader_no=m2.sec_trader_no
 where  m1.securities_trader_name=m2.sec_trader_name;
 
 
 select sec_trader_no,sec_trader_name from monitordb.a_securities_trader_info m2 where sec_trader_no not in (
 select securities_trader_no from monitordb.m_securities_trader_software_url
 );
 
 
 show tables in apdb;

select * from apdb.a_securities_trader_yybid;
select * from apdb.a_securities_trader_info;


alter table apdb.a_securities_trader_yybid add column securities_trader_name varchar(50) comment "券商名称";

truncate table apdb.a_securities_trader_yybid;


select * from apdb.a_securities_trader_yybid sty 
left join apdb.a_securities_trader_info sti 
on sty.securities_trader_name = sti.sec_trader_name;


update apdb.a_securities_trader_yybid  set securities_trader_name='新时代证券' where securities_trader_name='新时代';

update apdb.a_securities_trader_yybid sty,apdb.a_securities_trader_info sti 
set sty.securities_trader_no=sti.sec_trader_no
where sty.securities_trader_name = sti.sec_trader_name;