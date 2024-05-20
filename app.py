import os
import random
import pandas as pd
from flask import Flask,render_template, request,redirect,url_for,session,jsonify
from mysql_util import MysqlUtil
app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/')
def index():

    db = MysqlUtil()
    sql = 'SELECT * FROM category_temp'
    categorys = db.fetchall(sql)

    db = MysqlUtil()
    sql = 'SELECT * FROM product_temp  WHERE uid >=1  AND uid <=5 '
    products1 = db.fetchall(sql)  # 获取多条记录
    print(products1)

    db = MysqlUtil()
    sql = 'SELECT * FROM product_temp  WHERE uid >=6  AND uid <=10 '
    products2 = db.fetchall(sql)  # 获取多条记录
    print(products2)

    db = MysqlUtil()
    sql = 'SELECT * FROM product_temp  WHERE uid >=11  AND uid <=15 '
    products3 = db.fetchall(sql)  # 获取多条记录
    print(products3)

    db = MysqlUtil()
    sql = 'SELECT * FROM product_temp  WHERE uid >=16  AND uid <=20 '
    products4 = db.fetchall(sql)  # 获取多条记录
    print(products4)
    return render_template("index.html", categorys=categorys, products1=products1, products2=products2,products3=products3,products4=products4)

@app.route('/bashboard')
def bashboard():

    db = MysqlUtil()
    sql = 'SELECT * FROM category_temp'
    categorys = db.fetchall(sql)

    db = MysqlUtil()
    sql = 'SELECT * FROM product_temp'
    products = db.fetchall(sql)  # 获取多条记录
    print(products)

    return render_template("product_board.html",categorys=categorys,products=products)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'png','jpeg',"bmp"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_product',methods=['GET','POST'])
def add_product():
    db = MysqlUtil()
    sql = 'SELECT * FROM category_temp'
    categorys = db.fetchall(sql)  # 获取多条记录
    if (request.method == "POST"):
        pname = request.form.get("pname")
        pDesc = request.form.get("pDesc")
        counts = request.form.get("counts")
        uid= request.form.get("uid")
        old_price = request.form.get("old_price")
        new_price = request.form.get("new_price")
        print(pname)
        print(pDesc)
        print(counts)
        print(uid)
        print(old_price)
        print(new_price)

        file = request.files['file']
        if file.filename == '':
            return '没有选择文件', 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file_name, file_ext = os.path.splitext(os.path.basename(filename))
            # print(file_name)
            print(file_ext)
            dir_name = "./static/image/product_test/"
            new_name = str(random.randint(1,10000)) + file_ext
            print(dir_name)
            images_path = os.path.join(dir_name, new_name)
            print(images_path)
            file.save(images_path)

        id = "%d" % random.randint(0,1000000000)
        # images_path = "/static/product_test/2.jpg"
        db = MysqlUtil() # 实例化数据库操作类
        sql = "INSERT INTO product_temp(id,pname,old_price,new_price,counts,uid,images) \
               VALUES ('%s', '%s', '%s','%s','%s','%s','%s')" % (id,pname,old_price,new_price,counts,uid,images_path) # 插入数据的SQL语句
        db.insert(sql)
        return redirect(url_for('bashboard'))
    else:
        return render_template("add_product.html", categorys=categorys)

@app.route('/show')
def show():

    return render_template('job.html')

@app.route('/delete_product/<string:id>', methods=['POST'])
def delete_product(id):
    db = MysqlUtil() # 实例化数据库操作类
    sql = "DELETE FROM product_temp WHERE id = '%s'" % (id) # 执行删除笔记的SQL语句
    db.delete(sql) # 删除数据库
    return redirect(url_for('bashboard'))


@app.route('/register', methods=['GET','POST'])
def register():

    if (request.method == "POST"):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        print(username)
        print(password)
        print(email)


        db = MysqlUtil()
        sql = "INSERT INTO user_table(username,password,email) \
        VALUES ('%s', '%s', '%s')" % (username,password,email) # 插入数据的SQL语句

        product_list = db.insert(sql)  # 获取多条记录

        print(product_list)

        # insert_data(username, password, email)
        # return render_template("index.html")
        return redirect(url_for('index'))

    else: #GET
         return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if (request.method == "POST"):
        print("ok")
        username = request.form['username']
        password_candidate = request.form['password']
        print(username)
        sql = "SELECT * FROM user_table  WHERE username = '%s'" % (username)  # 根据用户名查找user表中记录
        db = MysqlUtil()  # 实例化数据库操作类
        result = db.fetchone(sql)  # 获取一条记录
        print(password_candidate)
        print(result)
        db_password = result['password']  # 用户填写的密码
        if password_candidate == db_password:
            # 写入session
            session['logged_in'] = True
            session['username'] = username

            # return "登录成功"# 跳转到控制台
            return redirect(url_for('index'))
        else:
            print("密码错误")
            return render_template("login.html")

    else: #GET
         return render_template("login.html")

@app.route('/get_company', methods=['GET'])
def get_company():
    db = MysqlUtil()
    sql = 'SELECT COUNT(*) AS num_products FROM category_temp'

    result = db.fetchone(sql)
    if result:
        num_products = result['num_products']
    else:
        num_products = 0

    db = MysqlUtil()
    sql = 'SELECT COUNT(*) AS num_products1 FROM product_temp'

    result = db.fetchone(sql)
    if result:
        num_products1 = result['num_products1']
    else:
        num_products1 = 0

    db = MysqlUtil()
    sql = 'SELECT AVG(old_price) AS num_products2 FROM product_temp'

    result = db.fetchone(sql)
    if result:
        num_products2 = result['num_products2']
    else:
        num_products2 = 0


    json = request.json
    print('recv:', json)
    re_data = {
        'company_num': num_products,
        'job_num': num_products1,
        'avg_salary': num_products2,
    }

    return jsonify(re_data)

@app.route('/get_industry', methods=['GET'])
def get_industry():
    # 读取CSV文件
    # df = pd.read_csv('./csv/data.csv')
    df = pd.read_csv('./csv/data3.csv', encoding="GB2312")
    # 访问特定的列（例如，'Column1'）
    # print(df['industry_type'])
    industry_type_list = df['industry_type']
    industry_type_value_list = df['industry_type_value']

    industry_type_list = industry_type_list.tolist()
    # industry_type_value_list = json.dumps(industry_type_value_list.tolist())
    industry_type_value_list = industry_type_value_list.tolist()
    re_data = {
           # 'industry_type': ["广东", "广东", "广东"],
           'industry_type': industry_type_list,
           'industry_type_value':  industry_type_value_list,
    }
    print(re_data)
    # re_data = {
    #        'industry_type': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    #        'industry_type_value':  [120, 200, 150, 80, 70, 110, 130],
    # }
    return jsonify(re_data)

@app.route('/logout')
def logout():
    session.clear() # 清除Session
    return redirect(url_for('index'))

app.run(debug=True, port=8000)