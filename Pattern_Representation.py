'''
Given a pattern consisting only of 'I' and 'S', where I represents descending and S represents ascending, you need to display a sequence
of numbers describing the ascending or descending order. Each character should be represented by 2 digits (between 1-9) - denoting the 
character's ascending or descending nature.
The second character in the pattern takes the last digit from the first character to build the sequence. The third character in the 
pattern takes the last digit from the second character to build the sequence and so on. The sequence cannot have repeated digits. 
Find the smallest such sequence which represents the given pattern.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a pattern, consisting only of 'S' and 'I'.

Constraints

1 <= T <= 500
1 <= len(str) <= 8

Output Format

For each test case, print the smallest sequence which represents the given pattern, separated by newline.

Sample Input 0

4
S
I
SIS
IISS
Sample Output 0

12
21
1324
32145
Explanation 0

Test Case 1
The given pattern has a single character 'S', which denotes ascending nature. There are multiple ways
to represent it - 12, 47, 28, 34 etc. However, "12" is the smallest of them.


Test Case 2
The given pattern has a single character 'I', which denotes descending nature. There are multiple ways 
to represent it - 21, 41, 75, 96 etc. However, "21" is the smallest of them.


Test Case 3
The given pattern has 3 characters 'S' (ascending), 'I' (descending) and 'S' (ascending). There are multiple ways 
to represent it - 1324, 1634, 1435, 4812, 3748 etc. However, "1324" is the smallest of them.
'''
for _ in range(int(input())):
    pattern = str(input())
    ans = []
    for i in range(1,len(pattern)+2):
        ans.append(i)
    flag=0
    por=0
    while por<len(pattern):
        te=0
        for x in pattern:
            if x=="I":
                if ans[te]<ans[te+1]:
                    ans[te],ans[te+1]=ans[te+1],ans[te]
                te+=1    
            if x=="S":
                if ans[te]>ans[te+1]:
                    ans[te],ans[te+1]=ans[te+1],ans[te]
                te+=1    
        por+=1
    for pr in ans:
        print(pr,end="")
    print("")
