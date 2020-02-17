'''
Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number.
(A proper divisor of a number is a positive factor of that number other than the number itself.

Input: 
The first line consists of an integer T i.e. the number of test cases.
First and the last line of each test case consists of two integers x and y.

Output:
Print '1' if the following pair is amicable pair otherwise print '0'.

Constraints:
1 <= T <= 100
1 <= x,y <= 105

Examples:
Input:
2
220 284
1 2
Output : 
1
0

Explanation :
Test Case 1 : Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110.
Sum of these is 284. Proper divisors of 284 are 1, 2, 4, 71 and 142 with sum 220.
'''
t = int(input())

for i in range(t):
    x , y = input().split()
    x = int(x)
    y = int(y)
    total1 , total2 , flag  = 0 , 0 , 0
    
    for i in range(1 , (x//2)+1):
        if x%i == 0:
            total1 += i
            
    if y ==total1:
        for i in range(1 , (y//2)+1):
            if y % i ==0:
                total2 +=i
        if total2 == x:
            flag = 1
        else:
            flag = 0
    else:
        flag = 0
        
    if flag ==1:
        print(1)
    else:
        print(0)
