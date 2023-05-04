'''Question Number: 1. 2Sum[Easy]
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target. 
    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice. You can return the answer in any order.

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
'''

'''思路
Solution1. 窮舉，遍歷每個組合 
Solution2. a,b 與 b,a 是一樣的，所以每一個數字只要跟後面的數字配在一起就可以，不需要回頭找配對
Solution3. 對一個陣列裡的數字 a 而言，我們其實是在找另一個數字 (target – a)
'''

from typing import List

# 這個寫法可以過濾掉重複出現的問題
# 但會重複去計算組合, e.g. [2,7] 與 [7,2]
class Solution1:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        for idx1,ele1 in enumerate(nums):
            for idx2,ele2 in enumerate(nums):
                if ele1 != ele2 and ele1 + ele2 == target:
                    return [idx1, idx2]

# 這個寫法可以過濾掉重複出現的問題 & 重複計算的組合
# 但時間複雜度太高
class Solution2:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        for idx1,ele1 in enumerate(nums):
            for idx2 in range(idx1+1,len(nums)):
                ele2 = nums[idx2]
                if ele1 + ele2 == target:
                    return [idx1, idx2]

# TODO: 有問題
class Solution3:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        for idx1,ele1 in enumerate(nums):
            expected_ele2 = target-ele1
            if expected_ele2 in nums :
                idx2 = nums.index(expected_ele2) #x有問題
                return [idx1, idx2]

class Solution4:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        temp_dict = {}
        for idx1,ele1 in enumerate(nums):
            temp_dict[ele1] = idx1
        for idx, ele in enumerate(nums):
            expected_ele2 = target - ele
            if expected_ele2 in temp_dict and temp_dict[expected_ele2] != idx:
                return [idx, temp_dict[expected_ele2]]

# Regina 目前可以想到的
class Solution5:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        temp_dict = {}
        for idx1,ele1 in enumerate(nums):
            expected_ele2 = target - ele1
            if expected_ele2 in temp_dict:
                return [temp_dict[expected_ele2], idx1]
            else:
                temp_dict[ele1] = idx1

class Solution(object):
    def two_sum(self, nums, target):
        d = {} # 用一個迴圈且把資訊與index暫存起來
        for idx1,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in d:
                return [d[num2], idx1]
            d[num1] = idx1
            print(d)

# nums = [2,7,11,15]
# target = 9

nums = [3,3]
target = 6

# nums = [3,1,3,6]
# target = 6
sol = Solution5()
print(sol.two_sum(nums, target))



