scoreList=[]
def process_main(): #계산과정
    for score in scoreList:
        score["avg"] = (score["lan"] + score["eng"] + score["math"]) / 3
        if score["avg"]  >= 90:
            score["grade"] = "수"
        elif score["avg"]  >= 80:
            score["grade"] = "우"
        elif score["avg"]  >= 70:
            score["grade"] = "미"
        elif score["avg"]  >= 60:
            score["grade"] = "양"
        else: score["grade"] = "가"

def append(): #데이터추가함수
    
    score={}    
    score["name"] = input("이름 : ")
    score["lan"] = int(input("국어 : "))
    score["eng"] = int(input("영어 : "))
    score["math"] = int(input("수학 : "))
    score["avg"] = int(0)
    score["grade"] = "미정"
    scoreList.append(score) # 목록에 추가하기

def output():
    for score in scoreList:
        print()
        print(f'{score["name"]}님', end="\t")
        print(f'국어 {score["lan"]}', end="\t")
        print(f'영어 {score["eng"]}', end="\t")
        print(f'수학 {score["math"]}', end="\t")
        print(f'평균 {score["avg"]}', end="\t")
        print(f'등급은 {score["grade"]}', end="\t")
        print() #줄바꿈e} 입니다")

def main():
    #return 함수를 종료하면서 함수의 작업내용을 함수 외부로 전달한다.
    #return 값을 안주면 그냥 함수 종료의 의미이다.
    while(True): #무한루프 종료를 하지않는다.
        print("1.점수 추가")
        print("2.계산")
        print("3.출력")
        print("0.종료")
        sel = input("선택 : ")
        if sel == "1":# 사용자가 1을 입력했을때
            append() #추가함수호출
        elif sel =="2": # 계산함수호출
            process_main()
        elif sel =="3": # 출력함수호출
            output()
        elif sel == "0": 
            print("프로그램을 종료합니다")
            return #함수종료
        else : print("잘못 선택하셨습니다")

main()



   