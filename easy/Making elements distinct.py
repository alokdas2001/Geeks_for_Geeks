'''
Given a sorted integer array. We need to make array elements distinct by increasing values and keeping array sum minimum possible. We need to print the minimum possible sum as output.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The first line of each test case contains N. followed by N separate integers. 

Output:
For each test caseprint the minimum possible sum.

Constraints:
1 ≤ T ≤ 100
2 ≤ N ≤ 10^4
1 ≤ A[i] ≤ 10^3

Example:
Input:
2
5
2 2 3 5 6
2
20 20
Output:
20
41

Explanation :
Test Case 1: We make the array as {2, 3, 4, 5, 6}. Sum becomes 2 + 3 + 4 + 5 + 6 = 20

Test Case2 : We make the array as  {20, 21 } .sum = 41
'''

t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    for i in range(1 , n):
        if A[i-1] >= A[i]:
            A[i] = A[i-1] + 1
            
    A = sum(A)
            
    print(A)
