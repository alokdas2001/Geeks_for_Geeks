'''
You are given an array of size N. Find the sum of distinct elements in an array.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input:
The first line is N, the size of array.
The second line contains N elements separated by spaces.

Output:
For each testcase, print the sum of all distinct elements.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 103

Example:
Input:
3
5
1 2 3 4 5
5
5 5 5 5 5
4
22 33 22 33
Output:
15
5
55

'''

t = int(input())

for i in range(t):
    n = int(input())
    
    arr = list(map(int , input().split()))
    
    arr = set(arr)
    
    total = 0
    
    for i in arr:
        total += i
        
    print(total)
