class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        count_rpt = 0
        
        if needle is "":
            return 0
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                
                j = len(needle) # Sol 1
                if haystack[i:i+j] == needle: # Sol 1
                    return i # Sol 1

                #j = 0 # Sol 2
                #while j in range(len(needle)): # Sol 2
                    #if (needle[j] != haystack[i+j]): # Sol 2
                        #break # Sol 2
                    #else: # Sol 2
                        #j = j+1 # Sol 2
                #if j == len(needle): # Sol 2
                    #return i # Sol 2
        return -1