        dic={"I":1,
            "V":5,
            "X":10,
            "L":50,	
            "C":100,
            "D":500,
            "M":1000}
        
        r=dic[s[len(s)-1]]

        for i in range(1,len(s)):
            if dic[s[i]]<=dic[s[i-1]]:
                r=r+dic[s[i-1]]
            else:
                r=r-dic[s[i-1]]
        return r