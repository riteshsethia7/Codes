'''
Given two strings A and B, find the minimum number of characters that needs to be deleted from these 2 strings to make them anagrams of each other. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutation of string A must be same as string B.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains 2 space separated strings - A and B.

Constraints

1 <= T <= 1000
1 <= len(A), len(B) <= 1000
'a' <= A[i],B[i] <= 'z'

Output Format

For each test case, print the minimum number of deletions required, separated by new line.

Sample Input 0

2
smart interviews
data structures
Sample Output 0

9
12
'''
for _ in range(int(input())):
    ls = list(map(str,input().split()))
    A = ls[0]
    B = ls[1]
    a = [0]*27
    b = [0]*27
    ans=0
    for i in A:
        pop = ord(i) - 96
        a[pop] += 1
    for j in B:
        pop = ord(j) - 96
        b[pop] += 1
    for x in range(27):
        temp = a[x]-b[x]
        ans+=abs(temp)
    print (ans)
    
