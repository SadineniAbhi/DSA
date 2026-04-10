class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            new_prefix = ""

            for i in range(len(prefix)):
                if i >= len(word) or prefix[i] != word[i]:
                    break
                new_prefix = new_prefix + prefix[i]

            prefix = new_prefix

        return prefix