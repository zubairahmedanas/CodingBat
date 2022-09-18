class Solution(object):
    def sortSentence(self, s):

        arr = s.split()
        arr = sorted(arr, key=lambda word: word[-1])

        res = ""
        n = len(arr)
        for i in range(n):

            res += arr[i][:-1]
            if i < n - 1:
                res += ' '

        return res

