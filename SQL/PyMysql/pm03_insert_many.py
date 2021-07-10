# 导入
import pymysql

# 连接数据库
con = pymysql.connect(host="localhost",user="3118004702",password="990225Zhxb.",database="py_database")

# 创建游标
cur = con.cursor()

# 编写数据库语句
sql = "insert into t_student(sname,age,score) values(%s,%s,%s)"

# 执行sql语句
try:
    cur.executemany(sql,[('小明',19,99.8),('小红',18,99.9),('小花',19,19.9)])
    con.commit()
    print("插入成功")

# 执行失败
except Exception as e:
    print(e)
    con.rollback()
    print("插入失败")

# 断开连接
finally:
    con.close()