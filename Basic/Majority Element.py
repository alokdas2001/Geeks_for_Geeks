'''
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:  
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output: 
For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
'''

t = int(input())

for i in range(t):
    n = int(input())
    
    A = list(map(int , input().split()))
    
    count = 0
    
    m = {} 
    for i in range(n): 
        if A[i] in m: 
            m[A[i]] += 1
        else: 
            m[A[i]] = 1
    count = 0
    for j in m: 
        if m[j] > n / 2: 
            count = 1
            print(j) 
            break
    if(count == 0): 
        print(-1) 
