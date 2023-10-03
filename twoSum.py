from typing import List
import copy 
class Solution:
    nums = [2,7,11,15] 
    target = 9
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in nums:
            copia=copy.deepcopy(nums)
            copia[nums.index(i)]=nums.index(i)*-1
            if target - i in copia:
                    return [nums.index(i), copia.index(target - i)]
            else:
                continue
    print(twoSum(nums,target))