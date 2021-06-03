
create table tcdb.jq_hk_hold_info(
id bigint(10) PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
day date COMMENT '日期',
link_id	 bigint(8) COMMENT '市场通编码三种类型：310001沪股通，310002深股通，310005港股通',
link_name		varchar(32)	COMMENT	'市场通名称 三种类型：沪股通，深股通，港股通',
code	varchar(12) COMMENT '股票代码',			
name	varchar(100) COMMENT '股票名称',			
share_number bigint(20) COMMENT '持股数量 单位：股，于中央结算系统的持股量',
share_ratio	 decimal(10,4) COMMENT '持股比例 单位：％',
create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
)comment '沪股通持仓信息表';