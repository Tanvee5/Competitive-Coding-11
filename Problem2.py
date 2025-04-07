# Problem 2 : Remove K Digits
# Time Complexity : O(n) where n is the size of the num
# Space Complexity : O(n) where n is the size of the num
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if the length of the num is less than k then resturn 0
        if k > len(num):
            return 0

        # define stack to store the number from the num string
        stack = []
        
        # loop through num string
        for d in num:
            # check if stack contain element and k greater than 0 and top element of stack greater than d
            while stack and k > 0 and stack[-1] > d:
                # pop the element from the stack since we need to get the smallest number
                stack.pop()
                # decrement the value of k
                k -= 1
            # push d to stack
            stack.append(d)
        
        # if still k greater than 0 then loop from 0 to k and pop the top element from stack
        for i in range(k):
            stack.pop()
        
        # define result to store result
        result = []
        # flag for leadingZero and set to True
        leadingZero = True
        # loop through digit in stack
        for digit in stack:
            # check the flag leadingZero and digit. If the flag is true and digit is 0 then continue
            if leadingZero and digit == '0':
                continue
            # set the leadingZero to flase
            leadingZero = False
            # append digit to result
            result.append(digit)
        # if result list is empty then return 0
        if not result:
            return '0'
        # convert result list to string and return the value
        return ''.join(result)
