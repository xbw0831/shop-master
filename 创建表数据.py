

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
data = [("1",'乐创四门冰箱','8299','static/image/floor/floor1-1.jpg'),
        ("2",'王牌液晶电视机家用','7333','static/image/floor/floor1-2.jpg'),
        ("3",'酒店宾馆洗衣机','17333','static/image/floor/floor1-3.jpg'),
        ("4",'小米1.5匹壁挂式卧室空调挂机','6333','static/image/floor/floor1-4.jpg'),
        ("5",'方太13升天然气燃气热水器','1333','static/image/floor/floor1-5.jpg'),
        ("6",'荣耀MagicBook电脑 ','7899','static/image/floor/floor2-1.jpg'),
        ("7",'Apple/苹果 iPhone 15 Pro Max','8333','static/image/floor/floor2-2.jpg'),
        ("8",'HUAWEI MatePad 2023款标准版华为平板电脑 深空灰','1399','static/image/floor/floor2-3.jpg'),
        ("9",'松典（SONGDIAN）数码相机','433','static/image/floor/floor2-4.jpg'),
        ("10",'胜粒type-c数据线快充线6A闪充电器','29','static/image/floor/floor2-5.jpg'),
        ("11",'艾珠儿（Aizhuer）连衣裙2024夏季女装新款','99','static/image/floor/floor3-1.jpg'),
        ("12",'新款加大加宽棒球帽帽子男女','9','static/image/floor/floor3-2.jpg'),
        ("13",'SOO行李箱男万向轮拉杆箱','199','static/image/floor/floor3-3.jpg'),
        ("14",'易旅旅行包 行李包 ','33','static/image/floor/floor3-4.jpg'),
        ("15",'红豆内衣男士秋衣秋裤纯棉','53','static/image/floor/floor3-5.jpg'),
        ("16",'三只松鼠大礼包','88','static/image/floor/floor4-1.jpg'),
        ("17",'鲜京采 原切西冷牛排','20.9','static/image/floor/floor4-2.jpg'),
        ("18",'谷言 预制菜 料理包','109','static/image/floor/floor4-3.jpg'),
        ("19",'上鲜 鸡翅中 1kg 冷冻 出口级','30.9','static/image/floor/floor4-4.jpg'),
        ("20",'纽仕兰3.5g蛋白质高钙全脂纯牛奶','7333','static/image/floor/floor4-5.jpg'),
        ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into product_temp(id, pname, old_price, images) values (%s,%s,%s,%s)", data)
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
