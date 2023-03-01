class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #quick sort approach
        if len(nums) <= 1:
            return nums
        else:
            pivo = nums[0]
            maior = []
            menor = []
            iguais = [] # there may be more than one
            for x in nums:
                if x > pivo:
                    maior.append(x)
                elif x < pivo:
                    menor.append(x)
                else:
                    iguais.append(x)
            result = self.sortArray(menor)
            result.extend(iguais)
            result.extend(self.sortArray(maior))
            return result