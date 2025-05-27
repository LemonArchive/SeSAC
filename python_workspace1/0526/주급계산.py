# #주급계산 
# 아이디
# 이름
# 근무시간
# 시간당급여액
# 연장수당 - case when 문 근무시간> 20

# 테이블 각자만들기

import pymysql
class weekpey:

    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', 
                        user = 'root', 
                        password = '1234' ,
                        db = 'mydb', 
                        port=3306) 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)       


    def insert(self):
        name = input("이름 : ")
        worktime = input("근무시간 : ")
        perpay = input("시급 : ")
        
        sql = """
                insert into week_pay(sname,worktime,perpay, 
                regdate)
                values (%s, %s, %s, now())
            """
        self.curs.execute(sql, (name, worktime, perpay))
        self.conn.commit() #반드시 해야 한다

    def output(self):

        sql = """
        SELECT id, sname, worktime, perpay,(worktime*perpay) as total,
        case 
        when worktime > 20
        then (worktime*perpay) + (worktime - 20) * perpay * 0.5
        end as overpay
        FROM week_pay;
        """ # 실행 할 쿼리문 입력
        
        self.curs.execute(sql) # 쿼리문 실행

        self.rows = self.curs.fetchall() # 데이터 패치

        for row in self.rows :
            print(row)
        
if __name__ == "__main__":
    w= weekpey()

    w.insert()
    w.output()