n = int(input('number : '))

for i in range(1, n+1):

    print(" "*(n-i), "*"*(2*i-1))
    
    
# while
list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)


# 정수 더하기
def sum_all(start, end):
    output = 0

    # range는 (끝 숫자 - 1) 을 하기 때문에 +1을 해줘야
    for i in range(start, end + 1):
        output += i
    return output

print(sum_all(0, 100))
print(sum_all(0, 1000))
print(sum_all(50, 100))
print(sum_all(50, 100))
