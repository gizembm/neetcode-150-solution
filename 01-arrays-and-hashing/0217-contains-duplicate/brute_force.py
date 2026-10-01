class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        Brute Force yaklaşımı.

        Listedeki her elemanı kendisinden sonra gelen diğer
        elemanlarla karşılaştırırız.

        Eğer aynı değere sahip iki farklı eleman bulursak
        listede tekrar eden bir değer olduğunu anlarız.

        Zaman Karmaşıklığı: O(n^2)
        Alan Karmaşıklığı: O(1)
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 3]

    solution = Solution()
    result = solution.hasDuplicate(nums)

    print(result)