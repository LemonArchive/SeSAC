from datetime import datetime,date
#오늘 날짜를 구한다
# today = date.today()

# #오늘은 무슨요일인지
# print(today.weekday())
# #0 1 2 3 4 5 6 월 화 수 목 금 토 일

# #문제 날짜를 입력받아서 그날이 무슨요일인지 반환하는 함수 ㅏㅁㅈㄴ들기
# #"2025-05-11"

# print(date.today())
# a = input("날짜를 입력하세요")
# a.strip('"')
# today = a.split("-")

# print(today)

# day1 = datetime.strptime("2025-05-11", "%Y-%m-%d")
# print(day1.weekday())

def getWeekday(s):
    day1 = datetime.strptime(s, "%Y-%m-%d")
    weekday = day1.weekday()
    titles=["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    return titles[weekday]

print(getWeekday("2025-04-11"))