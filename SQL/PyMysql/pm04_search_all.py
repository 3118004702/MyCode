# 导入
import pymysql

# 创建连接
con = pymysql.connect(host="localhost",user="3118004702",password="990225Zhxb.",database="py_database")

# 创建游标
cur = con.cursor()

# 编写sql语句
sql = "select * from t_student where age=18"

# 执行sql
try:
    cur.execute(sql)
    students = cur.fetchall()
    # print(students)
    for student in students:
        sno = student[0]
        sname = student[1]
        age = student[2]
        score = student[3]
        print("sno:",sno,"sname:",sname,"age:",age,"score:",score)
# 执行失败
except Exception as e:
    print(e)
    print("查询失败")

# 关闭连接
finally:
    con.close()