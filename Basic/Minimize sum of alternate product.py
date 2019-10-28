'''
Given an array of even size consisting of positive integers. Your task is to find the sum after sorting the array, such that the sum of product of alternate elements is minimum.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. Then in the next line are N space separated array elements.

Output:
For each test case, print the minimum sum.

Constraints:
1 <= T <= 100
2 <= N <= 107
1 <= Ai <= 109

Example:
Input:
2
8
9 2 8 4 5 7 6 0
4
1 2 3 4

Output:
74
10

Explanation:
Testcase 1: Required sum can be obtained as 9*0 + 8*2 + 7*4 + 6*5 which is equal to 74.
'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    A.sort()

    s , j= 0 , n-1

    for i in range(0 , n):
        if(i < j):
            a = A[j] * A[i]
            s = s + a
            j = j -1

    print(s)
