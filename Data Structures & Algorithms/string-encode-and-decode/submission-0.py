class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            for char in string:
                res.append(str(ord(char)))
                res.append("!")
            res.append("@")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        words_encoded = s.split("@")
        words_encoded.pop()
        for word in words_encoded:
            chars_encoded = word.split("!")
            chars_encoded.pop()
            chars = []
            for char in chars_encoded:
                chars.append(chr(int(char)))
            res.append("".join(chars))
        return res

            



