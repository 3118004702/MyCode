# 导入
import sqlite3

# 连接数据库
con = sqlite3.connect("C:\MyCode\SQL\SQLite3\demo.db")

# 创建游标
cur = con.cursor()

# sql语句
sql = "delete from t_person where pno=?"

# 执行语句
try:
    cur.execute(sql,(1,))
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