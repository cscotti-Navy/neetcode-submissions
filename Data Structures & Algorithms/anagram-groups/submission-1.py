class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))

            if key in ana_dict:
                ana_dict[key].append(word)

            else:
                ana_dict[key] = [word]
        return list(ana_dict.values()) 
