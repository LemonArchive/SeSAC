#    컴퓨터활용능력 시험
# 이름 필기(400) 워드(200) 스프레드시트(200)프레젠테이션(200)
# 등급은 800이상 A 800미만 600이상 B 600~400 C 400미만 D (재시험요망)


name = input("이름을 입력하세요")
written = int(input("필기 점수를 입력해주세요"))
word = int(input("워드 점수를 입력해주세요"))
sheets = int(input("시트 점수를 입력해주세요"))
ppt = int(input("프레젠테이션 점수를 입력해주세요"))
score = written + word + sheets + ppt

if score >= 800:
    print(f"총점은 {score}이며 A 입니다.")
elif score >= 600:
    print(f"총점은 {score}이며 B 입니다.")
elif score >= 400:
    print(f"총점은 {score}이며 C 입니다.")
else:
    print(f"총점은 {score}이며 D 재시험 대상입니다.")