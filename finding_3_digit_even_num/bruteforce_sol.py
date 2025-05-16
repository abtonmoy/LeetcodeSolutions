class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or k==i:
                        continue

                    h=digits[i]
                    t=digits[j]
                    u=digits[k]

                    # if h==0:
                    #     continue
                        
                    num = h*100+t*10+u

                    if num>=100 and num%2==0:
                        result.add(num)
        return sorted(result)
        