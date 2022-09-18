    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
       
        max_words =0
        for i in sentences:
            # print(i)
            max_words = max( len( i.split() ), max_words ) 
        return max_words