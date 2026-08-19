class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Width between the two pointers
            width = right - left
            
            # Height is limited by the shorter bar
            current_height = min(height[left], height[right])
            
            # Calculate current container area
            current_water = width * current_height
            
            # Update maximum water found so far
            max_water = max(max_water, current_water)
            
            # Move the pointer with the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
