class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for digit in s:
            if digit.isdigit() and int(digit) not in digits:
                digits.append(int(digit))
        if len(digits) <= 1:
            return -1
        else:  
            digits.sort() 
            return digits[-2]
        
                
        