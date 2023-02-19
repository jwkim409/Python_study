numbers = [1,3,3,4,6,5,6,6,3,3,4,5,3,4,5,5,5,5,5,6,8]
counter = {}

# (1) 출현한 숫자(요소) 확인하는 코드
for number in numbers:
#   counter[number] = "" 출력해보기
    counter[number] = 0

# (2) 출현한 숫자(요소) 빈도를 확인하는 코드 (위에 카운터 0으로 초기화 했으니 +=1)
for number in numbers:
    counter[number] += 1

print(counter)