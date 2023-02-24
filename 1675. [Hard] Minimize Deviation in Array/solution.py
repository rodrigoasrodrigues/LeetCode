class Solution:
    def deviation(self, nums: List[int]) -> int:
        if nums is None: return None
        if len(nums)==0:
            return None
        minn = min(nums)
        maxn = max(nums)
        dev = maxn - minn
        return dev

    def double_lower_odd(self, nums: List[int]) -> List[int]:
        # double lower odd approach
        odds = [x for x in nums if x % 2 != 0]
        if len(odds)>0:
            lower_odd = min(odds)
            lo_idx = nums.index(lower_odd)
            lo_nums = nums.copy()
            lo_nums[lo_idx] = lo_nums[lo_idx] * 2
            return lo_nums
        else:
            return None

    def halve_higher_even(self, nums: List[int]) -> List[int]:
        # divide higher even approach
        evens = [x for x in nums if x % 2 == 0]
        if len(evens)>0:
            higher_even = max(evens)
            he_idx = nums.index(higher_even)
            he_nums = nums.copy()
            he_nums[he_idx] = he_nums[he_idx] / 2
            return he_nums
        else:
            return None



    def minimumDeviation(self, nums: List[int]) -> int:
        # initial deviation
        init_dev = self.deviation(nums)
        # minumum possible value
        if init_dev == 0:
            return 0
        dlo = self.double_lower_odd(nums)
        dlo_dev = self.deviation(dlo)
        hhe = self.halve_higher_even(nums)
        hhe_dev = self.deviation(hhe)
        
        # used to ignore branch
        nope = init_dev *2

        if hhe_dev is None:
            hhe_dev = nope
        if dlo_dev is None:
            dlo_dev = nope

        # halving reduces deviation
        if hhe_dev <= init_dev and hhe_dev <= dlo_dev:
            return self.minimumDeviation(hhe)
        # doubling reduces deviation
        elif dlo_dev < init_dev and dlo_dev <= hhe_dev:
            return self.minimumDeviation(dlo)
        # no gain
        return int(init_dev)