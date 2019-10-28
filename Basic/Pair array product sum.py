'''
Given a array a[] of non-negative integers. Count the number of pairs (i, j) in the array such that a[i] + a[j] < a[i]*a[j]. (the pair (i, j) and (j, i) are considered same and i should not be equal to j)

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains n space separated integers respectively forming the array.

Output:
Print the total number of pairs possible in the array according to the problem statement.

Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5

Example:
Input:
2
3
3 4 5
3
1 1 1

Output:
3
0
'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    count = 0

    for i in range(0, n):
        for j in range(i+1 , n):
            if(A[i] * A[j] > A[i] + A[j]):
                count += 1


    print(count)
