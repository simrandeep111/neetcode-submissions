class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        arr = []

        for j in range(len(nums)):
            hashmap[nums[j]] = j

        for i in range (len(nums)):
            diff=target-nums[i]
            if diff in hashmap and hashmap[diff] != i:
                arr.append(i)
                arr.append(hashmap[diff])
                return arr

