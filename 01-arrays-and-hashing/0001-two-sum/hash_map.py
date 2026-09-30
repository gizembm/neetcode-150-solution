class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        One-Pass Hash Map yaklaşımı.

        Daha önce ziyaret edilen sayıları ve indekslerini
        bir dictionary içerisinde saklar.

        Her sayı için gerekli tamamlayıcı değer:
        complement = target - num

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


if __name__ == "__main__":
    nums = [3, 4, 5, 6]
    target = 7

    solution = Solution()
    result = solution.twoSum(nums, target)

    print(result)