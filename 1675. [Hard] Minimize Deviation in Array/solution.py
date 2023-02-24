import heapq


class Solution:
    def deviation(self, nums, minn) -> int:
        'calculate deviation'
        maxn = nums[0]
        dev = abs(maxn - minn)
        return dev

    def double_all_odds(self, nums: list[int]) -> list[int]:
        'this applies the second operation to all'
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = nums[i] * 2
        return nums

    def halve_max(self, nums, minn):
        'assumes max to be even, otherwise returns None'
        m = heapq.heappop(nums)
        if m % 2 != 0:  # if max is not even
            return None
        m = m / 2
        if minn < m: # note that numbers are negative due to heapq
            minn = m
        heapq.heappush(nums, m)
        return nums, minn

    def minimumDeviation(self, nums) -> int:
        'iterate and minimizes deviation'
        # doubling all odds can only be done once and solves all possible cases for odds
        nums = self.double_all_odds(nums)
        nums = [x * -1 for x in nums]
        min_num = max(nums) # the list is negative for heap optimization so we use max
        heapq.heapify(nums)
        current_lower_deviation = self.deviation(nums, min_num)
        nums, min_num = self.halve_max(nums, min_num)
        while nums:  # while makes sense to attemp reduction
            new_dev = self.deviation(nums, min_num)
            if new_dev < current_lower_deviation:  # if it reduces uses the new value
                current_lower_deviation = new_dev
            halve = self.halve_max(nums, min_num)
            if halve:
                nums, min_num = halve
            else:
                break
        # return the lowest value obtained
        return int(current_lower_deviation)