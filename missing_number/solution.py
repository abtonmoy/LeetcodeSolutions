class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        e_sum = size*(size+1)/2 #expected sum
        s = sum(nums)           #actual sum
        
            
        missing_num = e_sum -s  # difference between them is the missing number
        
        return missing_num