class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        Set uzunluklarını karşılaştırma yaklaşımı.

        Set veri yapısı tekrar eden değerleri yalnızca bir kez tutar.

        Eğer orijinal listenin uzunluğu ile set'e dönüştürülmüş
        listenin uzunluğu farklıysa listede duplicate vardır.

        Zaman Karmaşıklığı: O(n) - ortalama
        Alan Karmaşıklığı: O(n)
        """

        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 3]

    solution = Solution()
    result = solution.hasDuplicate(nums)

    print(result)