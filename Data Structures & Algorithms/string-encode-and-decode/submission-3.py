class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            piece = str(len(s)) + "#" + s
            encoded_string = encoded_string + piece
        return encoded_string 

    
    def decode(self, s: str) -> List[str]:
        i = 0 # Sets index to the start of our string 
        result = []
        while i < len(s):
            delim_index = s.find('#', i)
            length = int(s[i:delim_index])
            decode_string = s[delim_index + 1 : delim_index + 1 + length]
            result.append(decode_string) 
            i = delim_index + 1 + length
        return result
