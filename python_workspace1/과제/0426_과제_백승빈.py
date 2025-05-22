# 문제1
def ABC():
    num = int(input())
    if num % 2 == 0 :
        return True

    else : False

print(ABC())

#문제2

def leapYear():
    year = int(input())
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
print(leapYear())
