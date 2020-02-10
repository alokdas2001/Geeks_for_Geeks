'''
A step array is an array of integer where each element has a difference of at most k with its neighbor.
Given a key x, we need to find the index value of k if multiple elements exist, return the first occurrence of the key.

Input:
The first line of the input contains an integer T, the number of test cases. For each test case,
the first line contains two integer n & k denoting the size of array arr and the maximum difference
between adjacent elements respectively. Next line contains n space separated integers denoting the
elements of the array arr with at most k difference between adjacent elements.
Next line contains an integer x which is to be found in the array arr.

Output:
For each test case, the output is an integer displaying the index of the element x in the array arr. If the element is not present in the array return -1.

Constraints:
1<=T<=100
1<=n<=50
1<=k<=30
1<=x<=1000

Example:
Input:
2
5 1
4 5 6 7 6
6
6 20
20 40 50 70 70 60
60
Output:
2
5

Explanation:
1. The first index of 6 is 2.
2. The index of 60 is 5.

'''

t = int(input())

for i in range(t):
    n , k = input().split()
    A = list(map(int , input().split()))
    x = int(input())
    n = int(n)
    flag = 0
    for i in range(n):
        if A[i] == x:
            flag = 1
            break
        else:
            flag = 0
        
    if flag == 1:
        print(i)
    else:
        print(-1)
