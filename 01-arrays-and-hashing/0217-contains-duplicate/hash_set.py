class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        Hash Set yaklaşımı.

        Daha önce gördüğümüz değerleri bir set içerisinde tutarız.

        Her yeni sayı için:
        1. Sayı daha önce görüldü mü kontrol ederiz.
        2. Görüldüyse duplicate vardır ve True döndürürüz.
        3. Görülmediyse sayıyı set içerisine ekleriz.

        Zaman Karmaşıklığı: O(n) - ortalama
        Alan Karmaşıklığı: O(n)
        """

        seen = set()

        for num in nums:
            # Sayı daha önce görüldüyse duplicate bulduk.
            if num in seen:
                return True

            # İlk kez gördüğümüz sayıyı kaydediyoruz.
            seen.add(num)

        # Bütün listeyi gezdik ve tekrar eden değer bulamadık.
        return False


if __name__ == "__main__":
    nums = [7, 4, 9, 2, 4]

    solution = Solution()
    result = solution.hasDuplicate(nums)

    print(result)