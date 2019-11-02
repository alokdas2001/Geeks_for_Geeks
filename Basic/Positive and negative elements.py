'''
Given an array containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, in a new line print the arranged array.

Constraints:
1 <= T <= 300
2 <= N <= 105
-105 <= A[i] <= 105

Example:
Input:
2
6
-1 2 -3 4 -5 6
4
-3 2 -4 1
Output:
2 -1 4 -3 6 -5
2 -3 1 -4
'''
t = int(input())

for i in range(t):
    n = int(input())
    
    A = list(map(int , input().split()))
    
    B = []
    
    e = 0
    o = 1
    
    for i in range(n):
        if A[i] > 0:
            B.insert(e , A[i])
            e = e + 2
        elif A[i] < 0:
            B.insert(o , A[i])
            o = o + 2
        
    B = ' '.join(map(str , B))
    print(B)
        
