'''
Given an array, cyclically rotate an array by one.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array.

Output:
Output the cyclically rotated array by one.

Constraints:
1<=T<=1000
1<=N<=1000
0<=a[i]<=1000

Example:
Input:
2
5
1 2 3 4 5
8
9 8 7 6 4 2 1 3

Output:
5 1 2 3 4
3 9 8 7 6 4 2 1

'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    B = []

    B.append(A[n-1])

    for i in range(0 , n-1):
        B.append(A[i])


    B = ' '.join(map(str , B))

    print(B)
