class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0; 
        for j in J: 
            for s in S: 
                if j == s: 
                    counter += 1
        return counter

print(Solution.numJewelsInStones('self', 'aA', 'aAAAbbb'))
print(Solution.numJewelsInStones('self', 'zz', 'ZZ'))
