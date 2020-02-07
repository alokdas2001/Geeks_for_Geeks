'''
Given two numbers, p and q. Find the number of common divisors of p and q. 

Input: 

Each input consists of T,the number of test cases. Each test case consists of two integers p and q.
Output:

Output consists of a single line denoting the number of common divisiors of p and q.

Constraints:

1<=T<=100000

1<=p,q<=1000
Example:

Input:

2
2 4
3 5

Output:

2
1

'''
t  = int(input())

for i in range(t):
    n = 2
    A = list(map(int , input().split()))
    a = A[0]
    b = A[1]
    c = 0
    for i in range(1 , min(a, b)+1):
        if a % i == 0 and b % i == 0:
            c += 1
            
    print(c)
        
