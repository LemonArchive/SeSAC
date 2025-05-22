#이름, 국어, 영어, 수학성적을 입력받아 총점과 평균을 구하여 출력
#입력은 이름(문자열),국어, 영어, 수학
#출력 :총점, 평균

student_name = input("이름은?")
student_kor = int(input("국어?"))
student_eng = int(input("영어?"))
student_mat = int(input("수학?"))
#계산 - 수식 : 수학의 경우는 좌변과 우변변을 바꿀수 있다.
student_total = student_kor + student_eng + student_mat
student_avg = student_total//3
print(student_name , "님의 총 점수는", student_total , "평균은" , student_avg , "입니다") 
