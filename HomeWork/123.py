class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        for i in operations:
            if "+" in i:
                result += 1
            else:
                result -= 1
        return result