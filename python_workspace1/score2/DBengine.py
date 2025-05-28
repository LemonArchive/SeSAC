from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#SQLAlchemy가 PyMySQL을 내부적으로 사용하며 pool 지원
theEngine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/mydb",
    pool_size=10,
    max_overflow=5,
    pool_recycle=3600
)