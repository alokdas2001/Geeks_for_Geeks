'''
Given three distinct numbers, find the number with value in middle (Try to do it with minimum comparisons).

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain three distinct numbers a, b and c.


Output:
Print middle of three numbers.


Constraints: 
1 <= T <= 100
-1000 <= a, b, c <= 1000

Example:
Input:
2
20 30 40
12 32 11

Output:
30
12

'''
t = int(input())
for i in range(t):
    A = list(map(int , input().split()))
    
    A.sort()
    
    print(A[1])
