### ITSM

#### 部署文档

**创建数据库**
```
create database `codo_itsm` default character set utf8mb4 collate utf8mb4_unicode_ci;
```
**修改配置**
- 修改`settings.py`配置信息

**初始化数据**
```
python3 database.py
```

#### 使用
- POST/PUT/DELETE示例
```
{
  "fault_name": "yanghongfeitest02",
  "fault_level": "1",
  "fault_state": "1",
  "fault_penson":"yanghongfei",
  "processing_penson":"ops",
  "fault_report":"test",
  "fault_start_time":"20190101",
  "fault_end_time":"20190202"
}

```
- 返回结果
```
{
    "status": 0,
    "data": {
        "fault_name": "yanghongfeitest02",
        "fault_level": "1",
        "fault_state": "1",
        "fault_penson": "yanghongfei",
        "processing_penson": "ops",
        "fault_report": "test",
        "fault_start_time": "20190101",
        "fault_end_time": "20190202"
    },
    "datetime": "2019-01-28 11:19:02",
    "msg": "删除成功"
}

```

- 很多东西还没有完成。。。。

