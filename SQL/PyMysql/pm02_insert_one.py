# 导入
import pymysql

# 连接数据库
con = pymysql.connect(host="localhost",user="3118004702",password="990225Zhxb.",database="py_database")

# 创建游标
cur = con.cursor()

# 编写插入数据的sql语句->sno是自增长的，不用输入
sql = "insert into t_student(sname,age,score) values(%s,%s,%s)"

# 执行sql
try:
    # 执行sql
    cur.execute(sql,("小强",18,99.9))
    # 提交事务
    con.commit()
    print("插入成功")
# 执行失败
except Exception as e:
    print(e)
    con.rollback()
    print("插入失败")
# 关闭连接
finally:
    con.close()
