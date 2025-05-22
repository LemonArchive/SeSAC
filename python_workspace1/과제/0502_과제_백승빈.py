import random
gametry = 0
win = 0
lose = 0

def main():
    global win, lose
    
    while(True): #무한루프 종료를 하지않는다.
        print("1.게임시작")
        print("2.통계")
        print("3.통계초기화")
        print("0.종료")
        sel = input("선택 : ")
        if sel == "1":# 사용자가 1을 입력했을때
            game() #추가함수호출
        elif sel =="2": # 출력함수호출
            stats()
        elif sel =="3":
            win = 0
            lose = 0
        elif sel == "0": 
            print("프로그램을 종료합니다")
            return #함수종료
        else : print("잘못선택하셨습니다")

def game():
    computer = random.sample(range(1,10),3)
    while True:
        global gametry, win, lose
        a = input("x,x,x 형태로 입력해주세요 : ")
        b = a.split(",")
        intb= list(map(int,b))
        cb = list(computer)
        strike = 0
        ball = 0
        out = 0

        for i in range(0,3):
            if intb[i] == cb[i] :
                strike += 1
            elif intb[i] in cb:
                ball += 1
            else: out += 1
                
        gametry += 1
        if gametry == 6:
         print("게임오버!")
         lose += 1
         return

        print(f"{gametry}회차 시도입니다.")
        print(f"{strike} strike {ball} ball {out} out")    
        if strike == 3:
            win += 1
            print(f"정답은 {computer} 입니다. 정답입니다!")
            return 
def stats():
    return print(f"{win}승 {lose}패 입니다.")


main()