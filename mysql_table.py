from mysql_util import MysqlUtil

db = MysqlUtil()
sql = """
CREATE TABLE `category_temp` (
  `id` varchar(50) NOT NULL,
  `cname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

category = db.insert(sql)  # 获取多条记录

print("ok")