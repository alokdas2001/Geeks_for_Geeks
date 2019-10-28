'''

Given a sorted array consisting 0’s and 1’s. The task is to find the index of first ‘1’ in the given array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated 0 and 1.

Output:
For each test case, in a new line print the index of first 1. If 1 is not present in the array then print “-1”.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Ai <= 1018

Example:
Input:
2
10
0 0 0 0 0 0 1 1 1 1
4
0 0 0 0

Output:
6
-1

Explanation:
Testcase 1: First index where 1 is presented is 6.

'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    for i in range(0 , n):
        if A[i] == 1:
            ans = i
            break
        else:
            ans = -1

    print(ans)
