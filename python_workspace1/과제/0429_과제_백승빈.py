
# #문제1
words = ["assembly", "java", "rain", "notebook", "north","south", "hospital", "programming", "house", "hour"]

result = filter(lambda e: len(e) >= 6 , words)
print(list(result))

# #문제2

upper = map(lambda word: word.upper(), words)
print(list(upper))


#문제3
words.sort(key= lambda x : len(x))
print(words)

# #문제4
words.sort(key= lambda x : x , reverse=True ) 
print(words)

#문제5
word = filter(lambda x : "o" in x , words)
print (len(list(word)))

#x에 전달되는건 string타입이다. len(x) 문자열 길이
#파이썬의 람다는 한줄만가능, 다른언어는 2줄이상도 많음
#인텐테이션(들여쓰기)를 통해 블럭 코드의 시작 끝을 알수있는 한계점