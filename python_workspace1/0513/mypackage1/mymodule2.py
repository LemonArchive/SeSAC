
def isEven(even):
    if even % 2 == 0:
        return True
    else :
        return False
    
def toUpper(s):
    result = ""
    for a in s:
        if 'a' <= a <= 'z':
            result += chr(ord(a)-32)
        else:
            result += a
    return result

    
    

# print(isEven(6))

# print(ord("A"))
# print(ord('a')) # 대소문 자 차이 32
# print(ord("Z"))
# print(ord('z'))