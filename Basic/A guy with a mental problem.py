'''
A guy has to reach his home and does not want to be late. He takes train to reach home. He has a mental illness, so he always switches train at every station.
For eg: If he starts with train A then at station 2 he will switch his train to train B and so on. Similarly, if he starts with train B then he will switch to train A at station 2 and so on. Please help him to find the minimum total time he would take to reach his home.

Input:
The first line of the input contains an integer T denoting the number of test cases. T test cases follow. Each testcase contains three lines of input. The first line contains a positive integer N - the number of tasks to be completed. The second line contains N space-separated positive integers representing the time taken in seconds by train A to reach next Stations. The third line contains N space-separated positive integers representing the time taken in seconds by train B to reach next Stations.

Output:
For each testcase, print the minimum total time in seconds to reach home.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai, Bi <= 1010

Example:
Input:
1
3
2 1 2
3 2 1
Output:
5

Explanation:
Testcase1:
If he chose train A initially, then time to reach home will be : 2 + 2 + 2 = 6
If he Chose train B initially, then time to reach home will be : 3 + 1 + 1 = 5
5 is minimum hence the answer.


'''

t = int(input())

for i in range(t):
    n = int(input())

    t1 =input().split()
    t2 = input().split()

    sum1 = 0
    sum2 = 0

    for i in range(1 ,len(t1) , 2):
        t1[i], t2[i] = t2[i] , t1[i]

    for i in t1:
        sum1 = sum1 + int(i)

    for i in t2:
        sum2 = sum2 + int(i)

    print(min(sum1 , sum2))
