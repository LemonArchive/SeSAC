# def toDouble(x):
#     x = x*2
#     print(x)
# a= 10           #a라는 변수와 함수의 매개변수인 x는 서로 다른 공간이다.
# toDouble(a)     #x라는 변수에 값을 복사해가고 함수 수행하면서 복사된 x값은 수정된다.그러나 함수
# print(a)        #외부와는 아무런 관계도 없다. call by value 함수를 값 복사로 호출한다.
#                 #dict타입이란 list타입의 경우에는 함수내부에서 값 변환이 가능하다.
#                 #함수에 dict이나 list는 주소를 전달하는 방식이다.
# def toDouble2(mydic):
#     mydic["x"] *= 2
#     mydic["y"] *= 2
# mydic={"x":1 , "y":1}
# toDouble2(mydic)
# print(mydic)

#파이썬의 경우는 오버로딩을지원하지 않는다. 오버로딩은 동일한ㅇ ㅣ름인데 매개변수등 개수나 타입등을 이용해서
#여러개를 만들수있다.
#변수에 탕비이 없다. 그냥 막 쓰니까 매개변수의 개수나 타입으로 호출할 함수가 뭔지를 알길이없다.
#매개변수에 기본값을 줄 수 있다. 그래서 마치 오버로딩효과를 낼수있다.
#함수의 매개변수에 기본값을 주면 값을 전달안하면 기본값이 적용됨
def myadd(x=0, y=0, z=0):
    return x, y, z

result = myadd(1,2,3)
print(myadd)

result = myadd()
print(result)
print(myadd(1))
print(myadd(1,2))
print(myadd(1,2,3))

#모든 매게변수에 기본값을 줘야 하는것은 아니고, 기본값 주기 시작했으면 나머지매개변수도 다 줘야한다.
def myfuntion(a,b,c=0,d=0,e=0):
    print(f"a={a} b={b} c={c} d={d} e={e}")
    return a+b+c+d+e

print(myfuntion(4,5))

def sigma(limit=10):
    s=0
    for i in range(i, limit+1):
        s+=1
    return s

print(sigma())
print(sigma(5))
print(sigma(100))