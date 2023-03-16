def twoSum(self, nums, target):
    # target - nums 값을 seen에서 찾고 없으면 seen에 추가        
    seen = {}

    for idx, val in enumerate(nums):
        another = target - val

        if another in seen:
            # seen에 넣었던 값이 먼저 return 돼야 한다.
            return [seen[another], idx]
        else:
            seen[val] = idx

    return [-1, 1]   