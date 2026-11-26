class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in res:
                res[sortedWord] = []
           
            res[sortedWord].append(word)

        return list(res.values())

            