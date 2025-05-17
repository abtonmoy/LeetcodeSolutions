import math
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max = 0.0
        for i in range(len(points)):
            x1,y1= points[i]
            for j in range(i+1, len(points)):
                x2,y2=points[j]
                for k in range(j+1, len(points)):
                    x3,y3 = points[k]

                    a = self.dist(x1,y1,x2,y2)
                    b = self.dist(x2,y2,x3,y3)
                    c = self.dist(x3,y3,x1,y1)
                    
                    A = self.area(a,b,c)
                    if A > max:
                        max = A
        return max

    def area(self, a, b, c):
        if (a+b)<=c or (b+c)<=a or (c+a)<=b:
            return 0.0
        s = (a+b+c)/2.0
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
        

    def dist(self,x1, y1, x2, y2):
        return (math.sqrt((x1-x2)**2+(y1-y2)**2))