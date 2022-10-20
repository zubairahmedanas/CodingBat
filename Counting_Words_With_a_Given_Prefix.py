class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        pref_1 = len(pref)
        for i in words:
            if pref == i[:pref_1]:
                count += 1
            # break
            # count = 0
        # print(count)
        return count
