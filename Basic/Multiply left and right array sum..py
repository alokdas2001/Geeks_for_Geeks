'''
Pitsy needs help in the given task by her teacher. The task is to divide a array into two sub array (left and right) containing n/2 elements each and do the sum of the subarrays and then multiply both the subarrays.

Input:
First line consists of T test cases. Only line of every test case consists of an integer N.​

Output:
Print the answer by dividing array into left and right array and add their elements individually and then multiply both the array

Constraints:
1<=T<=100
1<=N<=1000
1<=Ai<=100

Example:
Input:
2
4
1 2 3 4
3
4 5 6
Output:
21
44
'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    B = len(A) // 2



    num = 0
    num1 = 0
    ans = 1

    for k in range(0 , B ):
        num += A[k]

    for j in range(B , len(A) ):
        num1 += A[j]

    ans = num * num1

    print(ans)




        
