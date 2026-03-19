#week04-2.py
        N = len(gain)
        ans = H = 0
        for i in range(N):
            H += gain[i]
            ans = max(ans, H)
        return ans
