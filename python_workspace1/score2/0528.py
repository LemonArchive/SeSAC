# lastname firstname name으로만들고 concat이겟지? 테이블은 customer address
#address 
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

theEngine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/sakila",
    pool_size=10,
    max_overflow=5,
    pool_recycle=3600
)

def output():
        with theEngine.begin() as conn:
            sql = text("""
                select concat(c.last_name," ",c.first_name) as name,
                a.postal_code, a.address,a.district,a.phone
                from customer c
                join address a on c.address_id = a.address_id 
                limit 10
            """)
            
            result = conn.execute(sql)
            for r in result.mappings().all():
                print(f"이름: {r['name']} 우편주소: {r['postal_code']} 주소 : {r['address']} 구역 :{r['district']} 전화번호 :{r['phone']}")


if __name__ == "__main__":
    output()
