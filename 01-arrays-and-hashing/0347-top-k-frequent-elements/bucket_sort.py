class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Her sayının frekansını hesapla
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # index = frekans
        # freq[index] = bu frekansta bulunan sayılar
        freq = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            freq[frequency].append(num)

        # En yüksek frekanstan başlayarak k eleman seç
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    k = 2

    solution = Solution()
    result = solution.topKFrequent(nums, k)

    print(result)