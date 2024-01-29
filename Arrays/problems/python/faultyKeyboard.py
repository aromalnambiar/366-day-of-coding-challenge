class Solution:
    def finalString(self, s):
        new_array = []
        for i in range(len(s)):
            
            if "i" in s:
                if "i" == s[i]:
                    new_array = new_array[i::-1]
                else:
                    new_array.append(s[i])
            else:
                new_array.append(s[i])        
        return ''.join(new_array)   
    
    
result = Solution()
print(result.finalString("string"))
