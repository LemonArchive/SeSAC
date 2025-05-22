try:
    x = int(input("정수 : "))
    y = int(input("정수 : "))
    z = x/y

    print(f"x={x} y={y} z-={z}")
except ZeroDivisionError as e:
    print(e)#에러메시지를 가져온다.
    print("0으로 왜나눌려고함???????")  
finally:
    print("이걸하네")

#주로 파일, 데이터베이스,네트워크 처리등에 많이 사용한다.
#파일, 데이터베이스, 네트워크연결 ..... 오류발생 close

