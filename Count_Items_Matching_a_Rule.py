lass Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        dic = {"type": 0, "color":1, "name":2}
        
        count = 0
        for item in items:
            if item[dic[ruleKey]]== ruleValue:
                count += 1
            
        return count