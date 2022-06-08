nums = [10,9,2,5,3,7,101,18]
def lis(nums):
    res = []
    def backtracking(nums, i, curr, prev):
        if i == len(nums):
            print(res)
            if not res:
                res.append(curr.copy())
            elif len(curr) > len(res[0]):
                res[0] = curr.copy()

        for i in range(i, len(nums)):
            if nums[i] > prev:
                curr.append(nums[i])
                backtracking(nums, i+1, curr, nums[i])
                curr.pop()
        return
    curr = []
    backtracking(nums, 0, curr, -float('inf'))
    return res
    

x = lis(nums)
print(x)