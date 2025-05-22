#지방 노동청에 신고가 들어옴 회사가 성별간 임금차별 성별과 연봉이 들어온다. 
#직원 전체 10명이고, 성별하고 연봉을 입력받음 남자 평균 , 여자평균을 구하라
# 입력 성별 연봉
# 출력 남자평균 여자평균

ppList=[]

manP = 0  
manC = 0  
wP = 0    
wC = 0    

for i in range(10):
    pp={}
    pp["gender"] = input("남자 or 여자 : ")
    pp["pay"] = int(input("연봉 : "))
    ppList.append(pp)
  
    if pp["gender"] == "남자":
     manP += pp["pay"]
     manC += 1

    else :
     wP += pp["pay"]
     wC += 1

mA = manP / manC
wA = wP  / wC

print(f"남자의 평균연봉은 {mA} 여자의 평균연봉은 {wA} 입니다. ")


