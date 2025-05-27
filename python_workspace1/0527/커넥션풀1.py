#conda activate myenv1
#pip install sqlalchemy
#버전 2.0 이상
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:1234@localhost/mydb",
    pool_size=10,
    max_overflow=5,
    pool_recycle=3600
)

try:
    conn = engine.connect() # 연결객체를 얻는다.
    print("데이터베이스 연결 성공")
except SQLAlchemyError as e:
    print("데이터베이스 연결 실패:", e)

#2.0 이전 버전 conn.execute(쿼리)
result = conn.execute(text("select * from emp"))
for row in result: #tuple로 출력한다.
    print(row)
conn.close()

#dictype으로 출력
# rows= result.mappings().all()
# sql = 

#데이터 추가하기 파라미터 추가방식
conn = engine.connect()
sql = text("""
           insert into emp(empno,enname,sal)
           values(:empno,:ename,:sal""")
conn.execute(sql,[{"empno":10000,
                   "ename": "우즈",
                   "sal" : 8000}])
conn.commit()
conn.close()