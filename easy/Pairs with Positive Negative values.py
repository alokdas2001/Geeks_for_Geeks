'''
Given an array of distinct integers, print all the pairs having positive value and negative value of a number that exists in the array.

NOTE: If there is no such pair in the array , print "0".

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer n.The next line of each test case consists of n spaced integers.

Output:
Print all the required pairs in the increasing order of their absolute numbers.

Constraints: 
1<=T<=100
1<=n<=1000
-1000<=a[i]<=1000

Example:
Input:
2
6
1 -3 2 3 6 -1
8
4 8 9 -4 1 -1 -8 -9

Output:
-1 1 -3 3 
-1 1 -4 4 -8 8 -9 9
'''



t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int , input().split()))
    
    B ,  C= [] , []
    
    for i in range(len(A)):
        B.append(abs(A[i]))
    B.sort()
    print(B)
    for i in range(1 , len(B)):
        
            if B[i] == B[i-1]:
                C.append(-(B[i]))
                C.append(B[i])
    if C == []:
        print(0)
        break
                
    C = ' '.join(map(str , C))
                 
    print(C)




