'''
You are playing a video-game in which your character has to cross N hurdles.
Initially, your character has N energies states corresponding to each hurdle.
All the hurdles have their respective heights.
Now, your character can only jump over a hurdle if its energy at that instant is greater than or equal to the hurdle's height.
When you cross a hurdle of height h, your current energy gets reduced by h. The remaining energy can rolled over for subsequent hurdles.
Also, after your character crosses a hurdle, it gets an energy boost that is equal to the position of that hurdle(1,2,3....).
So, given N, N energy states, and N hurdle heights; you need to find whether you can win the game or not. You can only win,
if your character can successfully cross all the hurdles.

Input:
The first line of the input contains a single integer T, denoting the number of test cases.
Then T test case follows. Each testcase contains three lines of input:-
The number N.
N energy states, separated by spaces.
N heights of hurdles, separated by spaces.

Output:
For each testcase, print "You Win!" space remaining energy if you cross all the hurdles, else print "Game Over".

Constraints:
1<=T<=110
1<=N<=2000
0<=A[i]<=1000

Example:

Input:
2
3
1 1 1
0 2 4
3
1 1 1
8 4 6

Output:
You Win! 3
Game Over

Explanation:
For testcase1: Your inital energy for 1st hurdle is 1. The hurdle height is 0. You can cross it.
The energy 1-0=1 get rolled over to the next state. Also, you gets a boost of 1 since you crossed the first hurdle.
The total energy of the next state becomes 1(rolled over)+1(boost)+1(2nd states energy)=3.
Now 3>= 2, so you can cross it. The energy 3-2=1 get rolled over. Also,
you get a boost of 2 since you crossed 2nd hurdle.
So, the next state's total energy becomes 1(rolled over)+2(boost)+1(state's energy)=4.
Now, 4>=4, so you can cross it. The remeining energy is 4-4=0 plus the boost of 3 since you crossed hurdle 3.
The energy at the end is 3.

For testcase2: 1 is not greater than or equal to 8. You can't cross the first hurdle.
'''
t = int(input())

for i in range(t):
    n = int(input())
    E = list(map(int , input().split()))
    H = list(map(int , input().split()))
    flag = 0
    energy = E[0]
    for i in range(1 , n+1):
        if energy >= H[i-1]:
            energy = energy - H[i-1] + (i)
            flag = 1
            if i!= n:
                energy += E[i] 
        else:
            flag = 0
            break
        
    if flag == 1:
        print("You Win!" , energy )
    else:
        print("Game Over")
            
            
            
    
    
    
    
    
