'''

Given two arrays of A and B respectively of sizes N1 and N2, the task is to calculate the product of maximum element of first array and minimum element of second array.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains 4 lines. First line contains size of the first array N1, next line contains elements of the first array separated by spaces. Third line contains size of the second array N2 and next line contains elements of the second array separated by spaces.

Output:
For each testcase, output the product of the max element of the first array and the minimum element of the second array.

Constraints:
1 <= T <= 100
1 <= N1, N2 <= 106
-108 <= Ai <= 108

Example:
Input:
2
6
5 7 9 3 6 2
6
1 2 6 -1 0 9
6
1 4 2 3 10 2
6
4 2 6 5 2 9

Output:
-9
20

Explanation:
Testcase 1: The first array is 5 7 9 3 6 2. The max element among these elements is 9. The second array is 1 2 6 -1 0 9. The min element among these elements is -1. The product of 9 and -1 is 9*-1=-9.

'''

t = int(input())

for i in range(t):
    n1 = int(input())

    N1 = list(map(int , input().split()))

    n2 = int(input())

    N2 = list(map(int , input().split()))

    max_N1 = N1[0]
    min_N2 = N2[0]

    for i in range(1 , len(N1)):
        if N1[i] > max_N1:
            max_N1 =  N1[i]

    for j in range(1 , len(N2)):
        if N2[j] < min_N2:
            min_N2 = N2[j]

    pro = min_N2 * max_N1

    print(pro)
