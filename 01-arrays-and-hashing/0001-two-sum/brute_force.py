class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Brute Force yaklaşımı.

        Her elemanı kendisinden sonra gelen diğer elemanlarla
        karşılaştırır ve toplamları target değerine eşitse
        indekslerini döndürür.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    nums = [3, 4, 5, 6]
    target = 7

    solution = Solution()
    result = solution.twoSum(nums, target)

    print(result)