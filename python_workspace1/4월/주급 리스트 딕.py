#주급 리스트 딕.py

# 이름 국어 영어 수학 총점 평균 / 평균에 대해서 수(90) 우(80) 미(70) 양(60) 가(50)
student={}
studentList=[]

for i in range(1):
    student["name"] = input("이름 : ")
    student["lan"] = int(input("국어 : "))
    student["eng"] = int(input("영어 : "))
    student["math"] = int(input("수학 : "))
    studentList.append(student)
  

for student in studentList:
    avg = (student["lan"] + student["eng"] + student["math"]) / 3


    if avg >= 90:
        grade = "수"
    elif avg >= 80:
        grade = "우"
    elif avg >= 70:
        grade = "미"
    elif avg >= 60:
        grade = "양"
    elif avg >= 50:
        grade = "가"
    
print(f"{student["name"]} 님의 평균은 {avg} 이고 등급은 {grade} 입니다")