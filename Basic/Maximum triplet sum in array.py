'''

Given an array, the task is to find maximum triplet sum in the array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the maximum triplet sum in new line.

Constraints:
1<=T<=100
3<=N<=106
-105<=A[i]<=105

Example:
Input:
2
6
1 0 8 6 4 2
7
1 2 3 0 -1 8 10
Output:
18
21

'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    A.sort(reverse = True)

    b = A[0] + A[1] + A[2]

    print(b)
