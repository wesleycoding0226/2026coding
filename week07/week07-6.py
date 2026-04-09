#week07-6.py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queue = deque(list(senate))
        counter = Counter(senate)
        R, D = counter['R'], counter['D']
        banR = banD = 0
        while queue:
            now = queue.popleft()
            if now == 'R':
                if banR>0:
                    banR -= 1
                    R -= 1
                    continue
                else:
                    banD += 1
                    queue.append(now)
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                    continue
                else:
                    banR += 1
                    queue.append(now)

            if R==0: return 'Dire'
            if D==0: return 'Radiant'
