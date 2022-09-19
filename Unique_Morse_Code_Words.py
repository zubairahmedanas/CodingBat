class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res = set()
        for word in words:
            # print(word)
            val = ""
            for i in word:
                val += morse[ord(i) - ord('a')]
            print('the val is', val, ord('a'))
            res.add(val)

        return len(res)

