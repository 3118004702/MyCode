# 导入
import sqlite3

# 连接数据库
con = sqlite3.connect("C:\MyCode\SQL\SQLite3\demo.db")

# 创建游标
cur = con.cursor()

# sql语句
sql = "select * from t_person"

# 执行sql语句
try:
    cur.execute(sql)
    person_all = cur.fetchall()
    for person in person_all:
        print(person)
    print("查询成功")

# 执行失败
except Exception as e:
    print(e)
    print("查询失败")

# 断开连接
finally:
    con.close()