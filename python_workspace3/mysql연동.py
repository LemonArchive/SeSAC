#conda activate myenv1
#pip install pymysql
#mysql 8부터 문제있을경우 pip install cryptography 를 입력
#1.DB연결
#2.데이터읽고쓰기
#3.연결끊기
import pymysql
import pymysql.cursors
conn = pymysql.connect(
    host='localhost', #ip localhost=127.0.0.1
     user='root',
      password='1234',
       db='mydb',
        port=3306)
print("접속성공")

cursor = conn.cursor() #커서를 가져와야한다
print('커서불러오기')
#커서를 통해
# sql = "select * from emp"
# cursor.execute(sql) #select 쿼리를 실행하고나서 내부에 갖고있다. 
# rows = cursor.fetchall() # 데이터를 tuple 타입으로 가져온다
# for row in rows:
#         print(type(row), row)
sql = "select * from emp where empno=8001"
cursor.execute(sql) # 다시 DB가져오기 
rows = cursor.fetchall()
print(rows)

sql = "select * from emp where empno<8000"
cursor.execute(sql)
rows = cursor.fetchmany(3)
for row in rows:
    print(row)


#데이터를 tuple타입으로 가져오면서 인덱싱과 슬라이싱만 지원
#row["ename"] -> 데이터를 가져올때 dict타입으로 가져오기
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()