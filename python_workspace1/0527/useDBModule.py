from DBModule import Database 

def output():
    db = Database() #객체만들면 이미 디비 접근 
    sql = "select * from tb_member"
    rows = db.executeAll(sql)
    for row in rows:
        print(row)
    db.close()
#회원가입
def member_register2(user_id): #
    db = Database() #객체만들면 이미 디비 접근
    sql = f"""
    select * from tb_member where user_id = '{user_id}'
    """
    result = db.executeOne(sql)
    if result:
        print("아이디가 이미존재합니다")
        return 1
    return 0

def idcheck(user_id=""):
    if user_id=="" or user_id=="test": #에러체크
        return False # 사용불가
    sql = """
    select count(*) cnt 
    from tb_member
    where user_id =%s"
    """
    db = Database()
    db.executeOne(sql,(user_id))
    row = db.executeOne(sql, (user_id))
    cnt = row["cnt"]
    db.close()
    if row["cnt"]== 0:
        return True
    return False
def member_register():
    db = Database() #객체만들면 이미 디비 접근
    while True:
        user_id=input("아이디 : ")
        if member_register2(user_id) == 0:
            break
    password = input("패스워드 : ")
    user_name=input("이름 : ")
    email=input("이메일 : ")
    phone=input("전화번호 : ")
    sql ="""
insert into tb_member(user_id, password, user_name,
email, phone, regdate) 
values(%s,%s,%s,%s,%s, now())
"""
    db.execute(sql, (user_id, password, user_name, email, phone))
    db.close()

#아이디 중복체크 -> 아이디 입력받고 나서 DB에 이미 존재하는지 존재하면
#이미존재하는아이디입니다. 하고 함수 종료
#사용가능한아이디입니다. 출력하고 나머지 입력받아 회원가입

# def member_register2(sql, user_id): #
#     db = Database() #객체만들면 이미 디비 접근
#     sql = f"""
#     select * from tb_table where user_id = '{user_id}'
#     """
#     result = db.executeone(sql)
#     print(result)


        # return row #결과를 반환해야 한다. 첫번째 레코드값 하나만 가져간다 

   
if __name__ == "__main__":
    member_register()
    output()
