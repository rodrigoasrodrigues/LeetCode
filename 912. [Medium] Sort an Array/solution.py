class Solution:
    def merge(self, arr1, arr2):
        'Merges sorted arrays' 
        i = j = 0
        l1 = len(arr1)
        l2 = len(arr2)
        res = []
        arr1.append(0) # just to avoid index error
        while (i < l1) or (j<l2):
            if (j >= l2) :
                res.append(arr1[i])
                i += 1
            elif arr1[i]<arr2[j] and (i < l1):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        return res
    
        
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort approach
        if len(nums) <= 1:
            return nums
        else:
            l = len(nums)
            l2 = int(l/2)
            left = nums[0:l2]
            right = nums[l2:l]
            left = self.sortArray(left)
            right = self.sortArray(right)
            res = self.merge(left,right)
            return res