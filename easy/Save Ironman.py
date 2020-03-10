'''
Jarvis is weak in computing palindromes for Alphanumeric characters.
While Ironman is busy fighting Thanos, he needs to activate sonic punch
but Jarvis is stuck in computing palindromes.
You are given a string S containing alphanumeric characters.
Find out whether the string is a palindrome or not.
If you are unable to solve it then it may result in the death of Iron Man.

Input:
The first line of the input contains T, the number of test cases. T testcases follow.
Each line of the test case contains string 'S'.

Output:
Each new line of the output contains "YES" if the string is palindrome and "NO"
if the string is not a palindrome.

Constraints:
1<=T<=100
1<=|S|<=100000
Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and whitespaces.

Example:
Input:
2
I am :IronnorI Ma, i
Ab?/Ba

Output:
YES
YES
'''
t = int(input())

for i in range(t):
    n = input()
    b = []
    a = []
    for i in range(len(n)):
        if (n[i] >='a' and n[i] <='z') or (n[i] >= 'A' and n[i] <='Z'):
            b.append(n[i])
        elif n[i] >='0' and n[i]<='9':
            b.append(n[i])
            
    for j in range(len(b)-1, -1 , -1):
        
        a.append(b[j])
    a = str(a)
    b = str(b)
    A = a.lower()
    B = b.lower()
    
    for k in range(len(a)):
        if A[k] == B[k]:
            flag = 1
        else:
            flag = 0
            break
    
            
    if flag==1:
        print("YES")
    elif flag==0:
        print("NO")
        
        
    
        

