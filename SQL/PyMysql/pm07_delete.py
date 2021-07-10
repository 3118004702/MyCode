# 导入
import pymysql

# 连接数据库
con = pymysql.connect(host="localhost",user="3118004702",password="990225Zhxb.",database="py_database")

# 创建游标
cur = con.cursor()

# sql语句
sql = "delete from t_student where sname = %s"
# 执行sql语句
try:
    cur.execute(sql,("张三丰",))
    con.commit()
    print("删除成功")

# 执行失败
except Exception as e:
    print(e)
    con.rollback()
    print("删除失败")

# 关闭连接
finally:
    con.close()