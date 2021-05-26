class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        strs.sort(key=len)
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[0][i] == strs[j][i]:
                    continue
                else:
                    return strs[0][:i]
        return strs[0]