

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
data = [("1",'乐创四门冰箱商用立式厨房冰柜冷藏柜冷冻平冷工作台大容量保鲜柜','8299','static/image/floor/floor1-1.jpg'),
        ("2",'王牌液晶电视机家用','7333','static/image/floor/floor1-2.jpg'),
        ("3",'酒店宾馆洗衣房设备 全自动工业水洗机 滚筒式洗脱两用工业洗衣机','17333','static/image/floor/floor1-3.jpg'),
        ("4",'小米1.5匹 新一级能效 变频冷暖 智能自清洁 巨省电 壁挂式卧室空调挂机','6333','static/image/floor/floor1-4.jpg'),
        ("5",'方太13升天然气燃气热水器 家用强排式 智能变频恒温 高层抗风Max系列低水压启动','1333','static/image/floor/floor1-5.jpg'),
        ("6",'荣耀MagicBook X16 战斗版 12代酷睿标压i5 16G 512G 16吋高清护眼屏 轻薄本笔记本电脑 智慧互联','7899','static/image/floor/floor2-1.jpg'),
        ("7",'Apple/苹果 iPhone 15 Pro Max (A3108) 256GB 蓝色钛金属 支持移动联通电信5G 双卡双待手机','8333','static/image/floor/floor2-2.jpg'),
        ("8",'HUAWEI MatePad 2023款标准版华为平板电脑11.5英寸120Hz护眼全面屏学生学习娱乐平板8+128GB 深空灰','1399','static/image/floor/floor2-3.jpg'),
        ("9",'松典（SONGDIAN）数码相机学生高中生迷你ccd小卡片机高清微单校园照相机 仙女粉 32G内存','433','static/image/floor/floor2-4.jpg'),
        ("10",'胜粒type-c数据线快充线6A闪充电器','29','static/image/floor/floor2-5.jpg'),
        ("11",'艾珠儿（Aizhuer）连衣裙2024夏季女装新款','99','static/image/floor/floor3-1.jpg'),
        ("12",'新款加大加宽棒球帽帽子男女大头围显脸小春夏秋冬字母百搭棒球帽 刺绣款-黑色','9','static/image/floor/floor3-2.jpg'),
        ("13",'SOO行李箱男万向轮拉杆箱耐磨抗摔26英寸A330旅行箱密码箱女商务黑色','199','static/image/floor/floor3-3.jpg'),
        ("14",'易旅旅行包 行李包 ','33','static/image/floor/floor3-4.jpg'),
        ("15",'红豆内衣男士秋衣秋裤纯棉套装圆领棉毛衫薄款打底保暖内衣','53','static/image/floor/floor3-5.jpg'),
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
