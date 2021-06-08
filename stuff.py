'''

start = 20
end = 40



for Number in range (start, end):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number)

'''


'''
import random
for i in range (10):
    n = random. randint(0,100) 
    print(n)
'''


'''
import random
for i in range (10):
    n = random. randint(0,100) 
    if(n/5==0):
        print(n, " is divisable by 5")
    else:
        print(n, " is not divisable by 5")
'''

n = 6
k = 5

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j, end=' ')
    print()