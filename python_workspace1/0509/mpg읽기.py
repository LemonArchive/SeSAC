#파이썬 버전이 낮을경우에 거듭해서 파일을 여는것은안된다.
with open("mpg.csv", "r") as f:
    lines = f.readlines()
    print(lines[:3])


