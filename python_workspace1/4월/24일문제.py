# # # # 문제1) m은 km와 m로 전환하기
# # # # 2300미터는 2km 와 300m입니다
# # # # 미터를 입력 받아서 각각 km와 m으로 전환해서 출력하세요
# # # # 힌트) 몫구하는 연산자 // 나머지 구하는 연산자 %
# # #숫자 문자를 섞어서 출력할떄 + 말고 포맷을 활용한다.
# # #fstring , python 3.6부터 추가
# # #f 를 붙이고 {변수명 또는 수식}

# # mm = int(input("거리를 입력하세요"))


# # disK = str(mm // 1000 )
# # disM = str(mm % 1000 )

# # print(f" {disK} KM {disM} M 입니다")


# # # # 문제2) 사다리꼴이 면적 구하기
# # # # 사다리꼴 면적 : (윗변 + 아랫변) * 높이 /2

# # x1 = int(input("윗변의 길이? "))
# # x2 = int(input("아랫변의 길이? "))
# # y = int(input("높이? "))

# # answer = ((x1 + x2) * y /2 )

# # print(answer)

# # # 문제3) 철수가 식료품점에 가서 과일을 샀다 사과와 배를 샀는데
# # #         한개에 5000원이고 배는 10000원이다. 각각 사과와 배의 개수를
# # #         입력받아 총금액을 구하는 프로그램을 작성하시오.

# # apple_amount = int(input("사과의 갯수"))
# # pear_amount = int(input("배의 갯수"))

# # money = (apple_amount * 5000 + pear_amount * 10000)

# # print (money)

# #문제4) 거스름돈 계산하기 - 10만원 짜리를 넣고 거스름돈 받기
#     물건값이 총 : 27560
#     거스름돈 : 72440
#     50000 -- 1 장
#     10000 -- 2 장
#      5000 -- 0 장
#      1000 -- 4 장
#       500 -- 0 개
#       100 -- 4 개
#        50 -- 0 개
#        10 -- 4 개

inputmoney = int(input("넣은 지폐"))
price = int(input("물건의 가격은?"))

change1 = inputmoney - price

m50000 = change1 // 50000
change2 = change1 % 50000
m10000 = change2 // 10000
change3 = change2 % 10000
m5000 = change3 // 5000
change4 = change3 % 5000
m1000 = change4 // 1000
change5 = change4 % 1000
m500 = change5  // 500
change6 = change5 % 500
m100 = change6 // 100
change7 = change6 % 100
m50 = change7 // 50
change8 = change7 % 50
m10 = change7 // 10


print(f"거스름돈은 {change1} \n 5만원권 {m50000}장 \n 1만원권 {m10000}장 \n 5000원권 {m5000}장 \n 1000원권 {m1000}장 \n 500원 {m500}개 \n 100원 {m100}개 \n 50원 {m50}개 \n 10원 {m10}개 \n 입니다")



# 문제5) 문자열 연습하기 

# 5-1  변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
# 5-2 =>list타입으로 전환해서 
# 5-3 =>"서희" 가 몇번째에 있는지 
# 5-4 "이순신", "장영실" 존재여부 확인 
# 5-5 추가할사람 : "정도전", "정약용", "최치원" ....
# 5-6  "서희" => "김종서" 로 바꾸기 
# 5-7 장길산 => 김길산 첫글자만 바꾸기 

#5-1
a = ("홍길동", "임꺽정", "장길산", "최영", "윤관", "강감찬", "서희", "이순신", "남이")
#5-2
a = list()
a.append ("홍길동")
a.append ("임꺽정") 
a.append ("장길산")
a.append ("최영")
a.append ("윤관")
a.append ("강감찬")
a.append ("서희")
a.append ("이순신")
a.append ("남이")
 #5-3
a.index ("서희")
#5-4
a.count ("이순신")
a.count ("장영실")
#5-5
a.append ("정도전")
a.append ("정약용")
a.append ("최치원")
#5-6

a[7] = "김종서"
#5-7

a[3] = "김길산"