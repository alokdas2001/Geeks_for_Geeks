'''

Given an array of integers, sort the first half of the array in ascending order and second half in descending order.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integers N.The next line consists of N spaced integers.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=N<=100
1<=a[i]<=1000

Example:
Input:
2
9
5 2 4 7 9 3 1 6 8
6
1 2 3 4 5 6

Output:
1 2 3 4 9 8 7 6 5
1 2 3 6 5 4

'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    b = n // 2

    A.sort()

    B = []


    for i in range(b):
        B.append(A[i])


    for j in range(n - 1, b-1, -1) :
        B.append(A[j])

    print(' '.join(map(str ,B)))
