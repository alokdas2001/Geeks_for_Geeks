'''

Given an array Arr[] of N distinct integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test case follows. First line of each test case contains a single integer N which denotes the number of elements in the array. Second line of each test case contains N space separated integers.

Output:
For each test case print the given array in such a way that the first element is first maximum and second element is first minimum and so on.

Constraints:
1<=T<=100
1<=N<=104
1<=Arr[i]<=105

Example:
Input:
2
7
7 1 2 3 4 5 6
8
1 6 9 4 3 7 8 2
Output:
7 1 6 2 5 4 3
9 1 8 2 7 3 6 4

'''

t = int(input())

for i in range(t):
    n = int(input())

    A = list(map(int , input().split()))

    B = []

    A.sort()

    while(len(A)>0):
        if (len(B)%2 == 0):
            B.append(A.pop())
        else:
            B.append(A.pop(0))

    B = ' '.join(map(str , B))


    print(B)
