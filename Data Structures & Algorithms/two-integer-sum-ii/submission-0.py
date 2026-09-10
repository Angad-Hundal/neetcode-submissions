class Solution:
    # numbers: increasing order
    # indx1 < idx 2
    # idx != idx2

    # using two for loops
    # not the best solution

    # use pointers
    # 

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start_index = 0
        end_index = len(numbers) - 1

        while start_index < end_index:

            if numbers[start_index] + numbers[end_index] == target:
                return [start_index+1, end_index+1]
            elif numbers[start_index] + numbers[end_index] < target:
                start_index += 1
            else:
                end_index -= 1
        return [start_index+1, end_index+1]
        