class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            piece = str(len(s)) + "#" + s
            encoded_string = encoded_string + piece
        return encoded_string 

    
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
'''            
This function works by having a starting variable i set to 0 and creating an empty list at result
we create a while loop of i being less than length of the s string because I 
will eventually be as long as the decoded string 
first we create a vairable delim_index which will search through the string starting
from i until it finds a # 
then we will create this length funtion which will turn the slice from i to delim_index into 0
then we have decode string which takes the charchters from the str s between
delim_index + 1 and delim_index + 1 + length then we have result.append which
appends the decode string onto result 
finally to complete i to end the while loop we have i - delim_index +1 + length
and we return the resulting decoded string
'''
