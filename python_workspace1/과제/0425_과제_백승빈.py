#숫자를 10개 입력받아 각각 짝수의 홀수의 합과 평균을 구하는 프로그램을 작성하시오

odd = 0
odd_count = 0

even = 0
even_count = 0

for i in range(10):

    b = int(input("숫자를 입력해주세요 "))

    if b % 2 == 0 :

        even += b
        even_count += 1

    else: odd += b 
    odd_count += 1
  
odd_avg = odd / odd_count
even_avg = even / even_count


print(f" 홀수의 합은 {odd} 홀수의 평균은 {odd_avg} 짝수의 합은 {even} 짝수의 평균은 {even_avg} 입니다.")
