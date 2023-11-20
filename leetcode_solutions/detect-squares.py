class DetectSquares:

    def __init__(self):
        self.yAxis = defaultdict(list)
        self.ct = Counter()
    def add(self, point: List[int]) -> None:
        x,y = point
        self.yAxis[y].append(point)
        self.ct[(x,y)] += 1
        
    def count(self, point: List[int]) -> int:
        x,y = point
        #find all point that are on the same y level
        count = 0
        for point in self.yAxis[y]:
            currX,currY = point
            xDiff = abs(x - currX)
            if xDiff == 0:
                continue
            count += self.ct[(currX,y - xDiff)] * self.ct[(x,y - xDiff)]
            count += self.ct[(currX,y + xDiff)] * self.ct[(x,y + xDiff)]

        return count

        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)