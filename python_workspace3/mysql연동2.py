import pymysql
import pymysql.cursors
conn = pymysql.connect(
    host='localhost', #ip localhost=127.0.0.1
     user='root',
      password='1234',
       db='mydb',
        port=3306
)

print("접속성공")

cursor = conn.cursor(pymysql.cursors.DictCursor)
print('커서 불러오기')

ename = "SCOTT"
sql = "select * from emp where ename = '"+ename+"'"
print(sql)
cursor.execute(sql)
rows = cursor.fetchall()

print("데이터개수",len(rows))

for row in rows:
    print(row["empno"], row["ename"], row["sal"])

#insert는 ?'
sql = """
    insert into emp(empno,ename,sal)
    values(%s,%s,%s)
"""
#max함수가 데이터가 한건도 없을떄 null을 갖고온다.
sql = "select ifnull(max(empno), 0)+1 from emp"
cursor.execute(sql)
row = cursor.fetchone()
print(row)
cursor.execute(sql,(row['id'],'백승빈',6000))

conn.commit() #연결객체 commit 반드시 해줘야 함

conn.close()
