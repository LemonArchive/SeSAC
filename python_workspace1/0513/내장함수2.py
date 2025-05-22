print(abs(-4))
print(abs(4))

print(all([1,2,3,4]))   # 요소 전체가 True이며 True "0" False ""False
print(all([1,2,3,4,0]))


print(all(["a","b","c"]))
print(all(["a","b",""]))

print(any([1,2,3,4])) #지금 전달받은 요소중에 0이 아닌것이 하나라도 
print(any([1,2,3,4,0]))#존재하면 True

print(dir([1,2,3,4,5,6,7]))
print(dir(dict))

#몫과 나머지를 tuple로 보낸다
mok,nmg = divmod(5,3)
print(mok)
print(nmg)

for i, c in enumerate("Life is egg"):
    print(i,c)

result = eval("1+10+3")
print(result)

result = eval("(1+10)*2-3")
print(result)


a = [3,4,-1,2,9,8,7,12,15,21]
#음수만 filter의 첫번째 매개변수는 함수여야한다.
#두번째 매개변수로 전달된 요소하나를 매개변수로 하고 반환은, True or Fasle
def isPositive(x):
    if x > 0: 
        return True
    return False

po_list = list(filter(isPositive, a))
print(po_list)

#한번 만들어서 쓰고 버리는 함수인 람다를 사용하자

po_list = list(filter(lambda x :x > 0, a))
print(po_list)

print(f" 최대값 {max(a)} 최소값 {min(a)}" )
print(pow(2,4))

import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)
print(day1)
print(day2)

day3 = day2-day1    #timedelta 객체로 바뀌고 날짜를 갖고있다.
print(day3.days)    

#말일까지 몇일이 남았는가
day4 = datetime.date(2025,5,13)
day5 = datetime.date(2025,12,31)
day6 = day4-day5
print(day6.days)

import calendar
from datetime import date
#오늘 날짜를 구한다
today = date.today()
year = today.year
month= today.month
#tuple 해당월의 첫째날과 마지막날을 반환
last_day = calendar.monthrange(year, month)[1]
print(last_day)

day1 = datetime.date(year,month, last_day)
print( (day1 - today).days)

#오늘은 무슨요일인지
print(today.weekday())
#0 1 2 3 4 5 6 월 화 수 목 금 토 일

#문제 날짜를 입력받아서 그날이 무슨요일인지 반환하는 함수 ㅏㅁㅈㄴ들기
#"2025-05-11"

print()

#딥러닝때 shutil 사용함
import shutil 
shutil.copy("./내장함수.py", "./내장함수2.py")

import glob
filelist = glob.glob("c:/*")
print(filelist)

filelist = glob.glob("./*")
print(filelist)

import os
print(os.environ)
print(os.environ['PATH'])

print(os.getcwd())

#파이썬에서 os명령어를 쓰고 싶을때
os.system("dir/w")