class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol=set()
        count = 0
        sorted_ = sorted(nums)
        a=len(sorted_)
        
        for i in range(a):
            for j in range(i+1, a):
                for k in range(j+1, a):
                    if sorted_[i]+sorted_[j]+sorted_[k]==0:
                        t=tuple(sorted([sorted_[i],sorted_[j],sorted_[k]]))
                        sol.add(t)
        sol=list(sol)       
        print(sol)
        return sol


        '''
        will run into Time Limit Exceeded (TLE) for this solution
        '''