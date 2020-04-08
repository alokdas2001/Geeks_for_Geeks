
'''
Given an array A of size N, construct a Product Array P (of same size) such that P is equal to the product of all the elements of A except A[i].

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line is N. The second line contains N elements separated by spaces. It is guranteed that the product of all the elements of the array will not exceed 1e18.

Output:
For every test case, print the product array in a new line.

Your Task:
You do not have to read input. Your task is to complete productExceptSelf() function and returns the Product vector P that holds product except for self at each index.

Constraints:
1 <= T <= 100
1 <= N <= 1000
0 <= Ai <= 200

Example:
Input:
2
5
10 3 5 6 2
2
12 0
Output:
180 600 360 300 900
0 12

Explanation:
Testcase1: For the product array P, at i=0 we have 3*5*6*2. At i=1 10*5*6*2. At i=2 we have 10*3*6*2. At i=3 we have 10*3*5*2. At i=4 we have 10*3*5*6
So P is 180 600 360 300 900

'''


def productExceptSelf(arr, n):
   
    B=[]
    
    
    pro0=1
    pro = 1
    count = 0
    C = []
    
    for k in arr:
        if k !=0:
            C.append(k)
        if k ==0:
            count +=1
    
    if count == 1:
        for k in C:
            pro0 = pro0 * k
    
    
    for i in arr:
        pro = pro * i
        
        
    for j in arr:
        if j!=0:
            B.append(pro//j)
        elif j==0 :
            if count==1:
                B.append(pro0)
            else:
                B.append(0)
    return(B)



# Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ans=productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends

