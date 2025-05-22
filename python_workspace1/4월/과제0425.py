# 문제5) 문자열 연습하기 

# 5-1  변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
# 5-2 =>list타입으로 전환해서 
# 5-3 =>"서희" 가 몇번째에 있는지 
# 5-4 "이순신", "장영실" 존재여부 확인 
# 5-5 추가할사람 : "정도전", "정약용", "최치원" ....
# 5-6  "서희" => "김종서" 로 바꾸기 
# 5-7 장길산 => 김길산 첫글자만 바꾸기 

#5-1
names = "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
print(names , type(names))

nameList =  names.split(",") #전달된값으로 문자열을 쪼꺠서 list값으로 반환
print(nameList, len(nameList)) #list, 배열의길이

#인덱싱 list, string 경우에 각 요소를 숫자를 통해서 접근 가능하다
#0 1,2,3,4 ......

print(nameList[0])

#슬라이싱  [시작값:종료값:증감치] 각각 생략 가능하다
print(nameList[3:]) #3번째이후로
print(nameList[:3]) #0에서 3번방전까지
print(nameList[::-1]) # 역순으로
print(nameList[2:5]) #2번에서 5번방전까지

print("서희의 위치", nameList.index("서희"))

if nameList.count ("이순신") > 0: #if 조건식
    print(" 이순신은 존재합니다")
else :
    print(" 이순신은 존재하지 않습니다.")

if "장영실" in nameList: #nameList안에 "장영실" 의 존재하면 True 
    print("\"장영실\"은 존재한다")

else :
    print("\"장영실\"은 존재하지 않습니다.")


print(nameList.count ("이순신"), "장영실" in nameList)

nameList.append ("정도전") #첫번쨰방법 하나씩추가
nameList.append ("정약용")
nameList.append ("최치원")

nameList.extend(["정도전","정약용","최치원"]) #두번째방법 한번에추ㅜ가

print(nameList)


pos = nameList.index("서희") #서희의 위치값을찾아서반환
nameList[pos] = "김종서" #반환받은 값으로 김종서로 변경

print(nameList)


pos = nameList.index("장길산")

nameList[pos] = nameList[pos].replace("장" , "김")

print(nameList)


