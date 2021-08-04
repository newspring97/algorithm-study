class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        res = []
        
        keyList = list(cnt.keys())
        tmp = 1
        for k in keyList:
            tmp *= cnt[k] + 1
            
        for i in range(tmp):
            subset = []
            ind = 0
            tmp = i
            while i > 0:
                for j in range(i % (cnt[keyList[ind]]+1)):
                    subset.append(keyList[ind])
                i -= i % (cnt[keyList[ind]]+1)
                i = int(i / (cnt[keyList[ind]]+1))
                ind += 1
            res.append(subset)
        return res