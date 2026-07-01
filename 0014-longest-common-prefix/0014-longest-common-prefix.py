class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Assume the first string is the common prefix
        prefix = strs[0]

        # Compare the prefix with each remaining string
        for s in strs[1:]:
            
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                
                if prefix == "":
                    return ""

        # Return the longest common prefix
        return prefix