'''
An array containing positive elements is given. ‘A’ and ‘B’ are two numbers defining a range. Write a function to check if the array contains all elements in the given range.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains space separated integers n, A and B which denotes the number of elements in the array a[] and the range [A, B]. Next line contains space separated n elements in the array a[].

Output:
Print "Yes" if all the elements in the range are present else print "No".

Constraints:
1<=T<=100
1<=n<=1000
1<= A < B<=1000
1<=a[i]<=1000​

Example:
Input:
1
7 2 5
1 4 5 2 7 8 3

Output:
Yes

'''

t = int(input())

for i in range(t):
    n , A , B = input().split()
    
    arr = list(map(int , input().split()))
    
    A = int(A)
    B = int(B)
    n = int(n)
    C = []
    count = 0
    
    for i in range(A , B+1):
        C.append(i)
        D = len(C)
    
    for j in range(n):
        if arr[j] in C:
            count += 1
                
    
    if count == D:
        print("Yes")
    elif count != D:
        print("No")
        
    
