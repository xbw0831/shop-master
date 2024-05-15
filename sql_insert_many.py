import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '',  # 数据库密码
    db = 'test',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

# 数据列表
data = [("1",'家用电器'),
        ("2",'数码'),
        ("3",'服装箱包'),
        ("4",'食品生鲜'),
        ("5","饮料酒水"),
        ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into category_temp(id, cname) values (%s,%s)", data)
    # 提交数据
    connectiont.commit()
except:
    # 发生错误时回滚
    print("发生错误时回滚")
    connectiont.rollback()

print("ok")
connectiont.commit()
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接