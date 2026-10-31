class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            length = str(len(s))
            for i in range(3-len(length)):
                length = '0' + length
            encoded_s += length + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded_l = []
        i = 0
        while i < len(s):
            strlen = int(s[i:i+3])
            decoded_l.append(s[i+3:i+3+strlen])
            i += 3 + strlen
        return decoded_l