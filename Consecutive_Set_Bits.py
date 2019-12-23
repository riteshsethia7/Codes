'''
Given a number N, find the max number of consecutive set bits in the number.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single number N.

Constraints

1 <= T <= 10000
0 <= N <= 1018

Output Format

For each test case, print the max number of consecutive set bits, separated by newline.

Sample Input 0

3
5
15
13
Sample Output 0

1
4
2
Explanation 0

Test Case 1
Binary Representation of 5: 101
Maximum Consecutive Set Bits: 1

Test Case 2
Binary Representation of 15: 1111
Maximum Consecutive Set Bits: 4

Test Case 3
Binary Representation of 13: 1101
Maximum Consecutive Set Bits: 2
'''
for _ in range(int(input())):
    number = int(input())
    st = str(format(number,"0b"))
    count = 0
    maxi=0
    for i in range(len(st)):
        if st[i]=="1":
            count+=1
        else:            
            count=0
        if count>maxi:
                maxi=count
    print(maxi)
        
