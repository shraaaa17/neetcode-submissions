class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True  # Found a duplicate, exit early
            seen.add(num)
        return False  # No duplicates found
