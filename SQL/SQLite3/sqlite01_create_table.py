# 导入
import sqlite3

# 创建连接
con = sqlite3.connect("C:\MyCode\SQL\SQLite3\demo.db")

# 创建游标
cur = con.cursor()

# sql语句
sql = """
    create table t_person(
        pno INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER
    )
"""
# 执行sql语句
try:
    cur.execute(sql)
    con.commit()
    print("创建成功")

# 执行失败
except Exception as e:
    print(e)
    con.rollback()
    print("创建失败")

# 关闭连接
finally:
    con.close()