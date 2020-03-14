'''
Generate all prime numbers between two given numbers.

Input:

The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing two space separated integers m and n.
Output:

For every test case print all prime numbers p such that m <= p <= n, space separated. Separate the answers for each test case by a new line.

Constraints:
1<=T<=60
1 <= m <= n <= 100000,
n - m <= 100000

Example:

Input:

2

1 10

3 5

Output:

2 3 5 7

3 5
'''
t = int(input())
for i in range(t):
    m , n = input().split()
    m = int(m)
    n = int(n)
    a = []
    flag = 0
    for i in range(m, n+1,1):
        if i > 2:
            for j in range(2, i):
                if (i % j) == 0:
                    flag =0
                    break
                else:
                    flag =1
            if flag ==1:
                a.append(i)
                
        elif i==2:
            a.append(i)
    a = ' '.join(map(str , a))        
    print(a)
