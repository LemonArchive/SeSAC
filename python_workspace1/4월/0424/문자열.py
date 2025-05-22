s = "Python String"

s2 = 'hello'

#여러줄에 걸칠때는 """ ~ """ , ''' ~ '''

s3 = """
        동해물과 백두산이
        마르고 닳도록
        하느님이 보우하사
        우리나라 만세
"""

print(s)
print(s2)
print(s3)

#인덱싱 - 0 번부터 시작해서 0,1,2 ....

# print(s[20]) IndexError: string index out of range
#슬라이싱 [시작:종료:증감치] 시작위치부터 증감치만큼 증가 도는 감소하면서 종료 보다 하나적게

print(s[0:3]) #0,1,2,3개만 출력력
print(s[0:6]) #0,1,2,3,4,5 증감치를 생략하면 +1로 생각함
print(s[0:6:2]) #0,2,4
print(s[7:]) 
print(s[len(s)-1:0:-1])
print(s[len(s)-1:-1:-1]) #파이썬 버젼에 따라서 에러메시지가 뜨기도 하고 지금처럼
print(s[len(s)-1::-1])
print(s[len(s)::-1]) #생략하면 알아서 처리한다. - 역순으로 출력한다