class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a set
        # keep on adding the value in set if not there
        # if already there return true

        seen_values = set()

        for value in nums:
            if value in seen_values:
                return True
            seen_values.add(value)
        return False