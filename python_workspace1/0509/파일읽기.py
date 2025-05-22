# #파일을 읽기로 열때는 파일이 존재해야한다.
# f = open("데이터파일.txt", "r")
# data = f.read() #파일을 통으로 읽는다.
# print(type(data))
# f.close() #파일을 연다. 파일
# f = open("데이터파일.txt", "r")
# data = f.readlines() #반환값이 list타입이다
# print(type(data))
# print((data))
# f.close()


f = open("데이터파일.txt", "r")
line = f.readlines() #반환값이 list타입이다
while line !="":
    print(type(line))
    print(line)
    line = f.readline()
f.close()
