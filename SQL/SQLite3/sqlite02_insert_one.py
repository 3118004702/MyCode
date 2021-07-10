# 导入
import sqlite3

# 连接数据库
con = sqlite3.connect("C:\MyCode\SQL\SQLite3\demo.db")

# 创建游标
cur = con.cursor()

# sql语句
sql = "insert into t_person(pname,age) values(?,?)"

# 执行sql语句
try:
    cur.execute(sql,("张三",23))
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