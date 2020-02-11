'''
Given a positive number N. The task is to round N to nearest multiple of 10. Number can be so big and can contains 1000 of digits.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a positive number N.

Output:
For each test case, print the nearest multiple of 10 in new line.

Constraints:
1 <= T <= 100
1 <= |Number length| <= 1000

Example:
Input:
2
15
29
Output:
10
30

'''
t = int(input())

for i in range(t):
    A = int(input())
    
    B = A%10
    
    if A %10 == 0:
        print(A)
        
    
    if B <=5:
        for i in range(1 , 6):
            a = A-i
            if (a) % 10 == 0:
                print(a)
                
    else:
        for i in range(1 , 5):
            b = A+i
            if (b) % 10 == 0:
                print(b)
        
