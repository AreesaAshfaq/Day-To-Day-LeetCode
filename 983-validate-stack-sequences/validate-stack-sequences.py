class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        popInd = 0

        for p in pushed:
            stack.append(p)
            while stack and  stack[-1]== popped[popInd]: 
                popInd += 1
                stack.pop()   

        return True if len(stack) == 0 else False