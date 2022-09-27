class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        arr = []
        arr1 = []

        for i in image:
            i = i[::-1]
            arr.append(i)

        for j in arr:
            for char in range(len(j)):
                # print(type(char))
                if j[char] == 1:
                    j[char] = 0
                else:
                    j[char] = 1

            arr1.append(j)

        return arr1