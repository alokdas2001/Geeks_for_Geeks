'''
Given an array of integers, your task is to find the smallest and second smallest element in the array. If smallest and second smallest do not exist, print -1.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array.

Output:
Print the smallest and second smallest element if possible,else print -1.

Constraints:
1<=T<=100
1<=n<=100
1<=a[i]<=1000

Example:
Input :
3
5
2 4 3 5 6
6
1 2 1 3 6 7
2
1 1
Output :
2 3
1 2
-1

'''

t = int(input())

for i in range(t):
    n = int(input())
    
    A = list(map(int , input().split()))
    
    A = set(A)
    A = list(A)
    A.sort()
    
    if len(A) < 3:
        print("-1")
        
    else:
        print(A[0] , A[1])
