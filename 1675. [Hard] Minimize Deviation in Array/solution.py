# the description of the problem is really confusing
class Solution:
    def deviation(self, nums: List[int]) -> int:
        'calculate deviation'
        minn = min(nums)
        maxn = max(nums)
        dev = maxn - minn
        return dev

    def double_all_odds(self, nums: List[int]) -> List[int]:
        'this applies the second operation to all'
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = nums[i] * 2
        return nums

    def halve_max(self, nums: List[int]) -> List[int]:
        'assumes max to be even, otherwise returns None'
        m = max(nums)
        if m % 2 == 1: # if max is not event
            return None
        idx = nums.index(m)
        nums[idx] = nums[idx] / 2
        return nums
    


    def minimumDeviation(self, nums: List[int]) -> int:
        'iterate and minimizes deviation'
        # doubling all odds can only be done once and solves all possible cases for odds
        nums = self.double_all_odds(nums)
        current_lower_deviation = self.deviation(nums)
        nums = self.halve_max(nums)
        while nums: # while makes sense to attemp reduction
            new_dev = self.deviation(nums)
            if new_dev < current_lower_deviation: # if it reduces uses the new value
                current_lower_deviation = new_dev
            nums = self.halve_max(nums)
        # return the lowest value obtained
        return int(current_lower_deviation)