# Problem 1 : Evaluate Reverse Polish Notation
# Time Complexity : O(n) where n is the size of the tokens
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # get the length of tokens list
        length = len(tokens)
        # if the length is 0 then return 0
        if length == 0:
            return 0
        # define stack to store the numbers from the token or result of the operations
        stack = []
        # loop through tokens list
        for i in range(length):
            # if the element is '+' then pop two number from stack, add those number and push the result of the operation to stack
            if tokens[i] == '+':
                popFirst = stack.pop()
                popSecond = stack.pop()
                result = popSecond + popFirst
                stack.append(result)
            # if the element is '-' then pop two number from stack, subtract second from first number and push the result of the operation to stack
            elif tokens[i] == '-':
                popFirst = stack.pop()
                popSecond = stack.pop()
                result = popSecond - popFirst
                stack.append(result)
            # if the element is '*' then pop two number from stack, muliply those number and push the result of the operation to stack
            elif tokens[i] == '*':
                popFirst = stack.pop()
                popSecond = stack.pop()
                result = popSecond * popFirst
                stack.append(result)
            # if the element is '/' then pop two number from stack, divide second by first and push the integer part of result of the operation to stack
            elif tokens[i] == '/':
                popFirst = stack.pop()
                popSecond = stack.pop()
                result = int(popSecond / popFirst)
                stack.append(result)
            # if the element is number then convert string to int and push to stack
            else:
                number = int(tokens[i])
                stack.append(number)
        # return top element of the stack as a result
        return stack[-1]
