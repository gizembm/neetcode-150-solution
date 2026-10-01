class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        Sorting yaklaşımı.

        Listeyi sıraladığımızda aynı değerler yan yana gelir.
        Böylece sadece komşu elemanları karşılaştırmamız yeterlidir.

        Zaman Karmaşıklığı: O(n log n)

        Not:
        nums.sort() verilen listeyi yerinde (in-place) değiştirir.
        """

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


if __name__ == "__main__":
    nums = [4, 2, 1, 3, 2]

    solution = Solution()
    result = solution.hasDuplicate(nums)

    print(result)