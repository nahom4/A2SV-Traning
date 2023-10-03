class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(map(lambda s : 1 if s == "R" else 0,senate))
        count = Counter(senate)
        ban = {0: 0,1 : 0}
        queue = deque(senate)
        while queue:
            mark = queue.popleft() # 1 R 0 D
            if ban[mark] > 0:
                ban[mark] -= 1
                count[mark] -= 1
            else:
                ban[1 - mark] += 1
                queue.append(mark)
           
            if count[0] == 0 or count[1] == 0:
                break
        return "Dire" if count[0] > count[1] else  "Radiant"

                
            
            