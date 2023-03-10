n = int(input('number : '))

for i in range(1, n+1):

    print(" "*(n-i), "*"*(2*i-1))
    
    
# while
list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)
