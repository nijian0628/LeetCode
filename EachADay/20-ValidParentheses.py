class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        temp = []
        
        if s[0] in ['(','[','{']:
            temp.append(s[0])
        else:
            return False
        
        for i in range(1,len(s)):
            if s[i] in ['(','[','{']:
                temp.append(s[i])
            elif len(temp) != 0:
                if s[i] == ')' and temp[len(temp)-1] == '(':
                    temp.pop()
                elif s[i] == ']' and temp[len(temp)-1] == '[':
                    temp.pop()
                elif s[i] == '}' and temp[len(temp)-1] == '{':
                    temp.pop()
                else:
                    return False
            else:
                return False
        if len(temp) == 0:
            return True
        else:
            return False