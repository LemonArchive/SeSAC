workerList = [
    {"name" : "홍길동" , "workTime" : "30" , "perPay" : "20000"},
    {"name" : "김길동" , "workTime" : "20" , "perPay" : "30000"},
]   #공용변수로 존재해야 한다
def process(worker): #dic 가져와서 반환하는방법 매개변수로 값ㄷ을 받아오면 외부로 전달을 안된다.
    worker["pay"] = int(worker["workTime"]) * int(worker["perPay"])

def process_main():
    for w in workerList:
        process(w)

def append(): #데이터추가함수
    worker={} #dict 타입 객체
    worker["name"] = input("이름 : ")
    worker["workTime"] = input("근무시간 : ")
    worker["perPay"] = input("시급 : ")
    worker["pay"] = 0       
    workerList.append(worker)# 목록에 추가하기

def output():
    for w in workerList:
        print(f'{w["name"]}', end="\t")
        print(f'{w["workTime"]}', end="\t")
        print(f'{w["perPay"]}', end="\t")
        print(f'{w["pay"]}', end="\t")
        print() #줄바꿈

def main():
    #return 함수를 종료하면서 함수의 작업내용을 함수 외부로 전달한다.
    #return 값을 안주면 그냥 함수 종료의 의미이다.
    while(True): #무한루프 종료를 하지않는다.
        print("1.추가")
        print("2.출력")
        print("3.계산")
        print("0.종료")
        sel = input("선택 : ")
        if sel == "1":# 사용자가 1을 입력했을때
            append() #추가함수호출
        elif sel =="2": # 출력함수호출
            output()
        elif sel =="3": # 출력함수호출
            process_main()
        elif sel == "0": 
            print("프로그램을 종료합니다")
            return #함수종료
        else : print("잘못선택하셨습니다")

main()

#문법적으로 javascipt에 JSON 데이투구조하고 동일
#MYSQL 속도가 너무 느려서 빅데이터 몽고디비 -JSON 형태로 데이터 저장을한다
#판다스 -> 데이터 프레임 : dict- dataframe형태로 바꾸기 싶다.