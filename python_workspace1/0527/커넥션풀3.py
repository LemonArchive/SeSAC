from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/mydb",
    pool_size=10,
    max_overflow=5,
    pool_recycle=3600
)
#1. 데이터가져오기(모두 한줄씩 출력 SQL 문만 바꾸면댐)
# with engine.connect() as conn:
#     sql = """
#     select empno, ename, sal  
#     from emp
#     """
#     result = conn.execute(text(sql))
#     for row in result.all():
#         print(row)

#     #dict
#     result = conn.execute(text(sql))
#     rows = result.mappings().all()
#     for row in rows:
#         print(dict(row))

#2. 검색어를 전달할때
# ename = "조승연" #키보드입력으로변경

# with engine.connect() as conn:
#     sql = """
#         select empno, ename , sal
#         from emp
#         where ename=:name
# """
#     result = conn.execute(text(sql),[{"name":ename}])
#     temp = result.all()
#     if len(temp) == 0:
#         print("없음")
#     else:
#         for row in temp:
#             print(row)

# 3. insert - 트랜잭션 처리 - 트랜잭션처리가 안되는경우

# with engine.connect() as conn:
#     sql = """
#     select ifnull(max(id),0)+1     from test1
#     """
#     result = conn.execute(text(sql)) #[()]
#     id = result.all()[0][0]
#     sql = """
#         insert into test1 values(:id, :field)
#     """
#     conn.execute(text(sql), [{"id":id, "field":"test"}])
#     conn.commit() #커밋반드시

# 트랜잭션 처리가 필요할 경우에
# ACID(atomic,consistancy,isolation,Durability)
with engine.begin() as conn:
    sql = """
    select ifnull(max(id),0)+1     from test1
    """
    result = conn.execute(text(sql)) #[()]
    id = result.all()[0][0]
    sql = """
        insert into test1 values(:id, :field)
    """
    conn.execute(text(sql), [{"id":id, "field":"test"}])
  
