class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vs = dict()
        answer = False

        for save in s:
            if save in vs:
                vs[save] = vs.get(save) + 1
            else:
                vs[save] = 1

        for trex in t:
            if trex in vs:
                vs[trex] = vs.get(trex) - 1
            else:
                vs[trex] = 1

        for x,y in vs.items():
            if y == 0:
                answer = True
            else:
                return False

        return answer

        