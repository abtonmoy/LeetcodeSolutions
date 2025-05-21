class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        a = len(nums)
        sol = []

        for i in range(a):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = a-1

            while l<r:
                total = nums[l] + nums[r] + nums[i]

                if total == 0:
                    res=[nums[l], nums[r], nums[i]]
                    sol.append(res)
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l <r and nums[r] == nums[r+1]:
                        r-=1

                elif total < 0:
                    l+=1
                else:
                    r-=1
        
        return sol


        