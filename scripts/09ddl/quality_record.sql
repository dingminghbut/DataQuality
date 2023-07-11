--表：数据异常类型（data_quality_issue_types）
CREATE TABLE data_quality_issue_types (
    issue_type_id INT PRIMARY KEY COMMENT '异常类型ID',
    issue_type_name VARCHAR(100) COMMENT '异常类型名称'
) COMMENT = '数据异常类型表';

--表：数据异常记录（data_quality_issues）
CREATE TABLE data_quality_issues (
    issue_id INT PRIMARY KEY COMMENT '异常记录ID',
    issue_type_id INT COMMENT '异常类型ID',
    timestamp TIMESTAMP COMMENT '异常发生时间',
    description VARCHAR(255) COMMENT '异常描述',
    column_name VARCHAR(100) COMMENT '异常列名',
    record_id INT COMMENT '记录ID'
) COMMENT = '数据异常记录表';

--表：数据异常统计（data_quality_summary）
CREATE TABLE data_quality_summary (
    issue_type_id INT PRIMARY KEY COMMENT '异常类型ID',
    total_count INT COMMENT '总异常数量',
    latest_timestamp TIMESTAMP COMMENT '最近异常发生时间'
) COMMENT = '数据异常统计表';

