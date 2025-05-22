colors = {"red":"빨간색", "blue":"파란색", "green":"초록색"}
#키값은 문자열을 주로 사용한다. 만일에 같은 키값을 두번쓰면 두번째꺼로 업데이트된다.
#인덱싱, 슬라이싱 불가능
print(colors["red"])
print(colors["blue"])
print(colors["green"])

print(colors.keys())#키값들의 목록을 보여준다

#추가
colors["black"] = "검은색"
print(colors.keys())
#업데이트
colors["red"] = "핏빛빨강"
print(colors.keys())

#없는 키값의 경우 파이썬이 어떻게 동작하는지
if "pink" in colors.keys():
    print(colors['pink'])
else:
    print("pink is not exist")

print(colors.items())
print(colors.values())


#특정키삭제 - pop(키값)
colors.pop("red") #red키 삭제

colors.clear() #전체삭제
print(colors)

