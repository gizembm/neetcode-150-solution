# 1. Two Sum

**Zorluk:** Easy  
**Konu:** Arrays & Hashing

## Problem

Bir `nums` tam sayı dizisi ve bir `target` değeri veriliyor.

Amacımız, toplamları `target` değerine eşit olan iki farklı elemanın indekslerini bulmaktır.

Matematiksel olarak:

```text
nums[i] + nums[j] = target
```

ve aynı elemanı iki kez kullanamayacağımız için:

```text
i != j
```

olmalıdır.

Her input için yalnızca bir geçerli çözüm olduğu garanti edilmektedir.

---

## Örnek

```text
Input:
nums = [3, 4, 5, 6]
target = 7

Output:
[0, 1]
```

Çünkü:

```text
nums[0] + nums[1]
= 3 + 4
= 7
```

Bu nedenle `[0, 1]` döndürülür.

---

# Çözüm 1 — Brute Force

## Yaklaşım

Problemi çözmenin en basit yolu bütün olası eleman çiftlerini kontrol etmektir.

Her `nums[i]` elemanı için kendisinden sonra gelen elemanları dolaşırız:

```text
nums = [2, 1, 5, 3]

2 → 1, 5, 3
1 → 5, 3
5 → 3
```

Bir çiftin toplamı `target` değerine eşitse indekslerini döndürürüz.

İkinci döngünün `i + 1` değerinden başlamasının iki nedeni vardır:

1. Aynı elemanı iki kez kullanmamak.
2. Daha önce kontrol edilmiş çiftleri tekrar kontrol etmemek.

Örneğin `2 + 1` kontrol edildiyse daha sonra tekrar `1 + 2` kontrol edilmesine gerek yoktur.

## Kod

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

## Zaman Karmaşıklığı

```text
O(n²)
```

İç içe iki döngü kullandığımız için en kötü durumda yaklaşık olarak bütün eleman çiftleri kontrol edilir.

## Alan Karmaşıklığı

```text
O(1)
```

Input büyüklüğüne bağlı ek bir veri yapısı kullanılmaz.

---

# Çözüm 2 — One-Pass Hash Map

Brute Force çözümünde problem, ihtiyacımız olan sayıyı bulabilmek için diğer elemanları tekrar tekrar kontrol etmemizdir.

Bunun yerine problemi farklı şekilde düşünebiliriz.

Elimizde şu denklem var:

```text
num + diğer_sayı = target
```

Buradan:

```text
diğer_sayı = target - num
```

elde edilir.

Aradığımız bu değere **complement (tamamlayıcı)** diyebiliriz.

Örneğin:

```text
target = 9
num = 2

complement = 9 - 2
           = 7
```

Yani `2` sayısını gördüğümüzde bütün diziyi tekrar aramak yerine şu soruyu sorabiliriz:

> Daha önce `7` sayısını gördüm mü?

Bu sorguyu hızlı yapabilmek için bir Hash Map kullanabiliriz.

Python'da bunu `dict` ile gerçekleştiriyoruz.

---

## Hash Map'te Ne Saklıyoruz?

Dictionary içerisinde:

```text
sayı → index
```

eşleşmesini saklıyoruz.

Örneğin:

```python
seen = {
    8: 0,
    2: 1
}
```

şu anlama gelir:

```text
8 sayısını index 0'da gördüm.
2 sayısını index 1'de gördüm.
```

İndeksi saklamamızın nedeni problemin bizden sayıların kendisini değil, indekslerini istemesidir.

---

## Algoritma

Her eleman için:

1. Mevcut sayıyı al.
2. `complement = target - num` hesapla.
3. `complement` daha önce görülmüş mü kontrol et.
4. Görülmüşse iki indeksi döndür.
5. Görülmemişse mevcut sayıyı ve indeksini Hash Map'e ekle.

Özet olarak:

```text
current number
      ↓
target - current number
      ↓
complement
      ↓
Hash Map'te var mı?
     / \
   Evet Hayır
    ↓     ↓
 return  Hash Map'e ekle
```

---

## Adım Adım Örnek

Şu input'u kullanalım:

```python
nums = [8, 2, 11, 7, 15]
target = 9
```

Başlangıç:

```python
seen = {}
```

### 1. Iterasyon

```text
i = 0
num = 8
```

Tamamlayıcı:

```text
complement = 9 - 8
           = 1
```

`1`, `seen` içerisinde bulunmuyor.

Bu nedenle `8` ve indeksi eklenir:

```python
seen = {
    8: 0
}
```

### 2. Iterasyon

```text
i = 1
num = 2

complement = 9 - 2
           = 7
```

`7` henüz `seen` içerisinde bulunmuyor.

```python
seen = {
    8: 0,
    2: 1
}
```

### 3. Iterasyon

```text
i = 2
num = 11

complement = 9 - 11
           = -2
```

`-2` bulunmuyor.

```python
seen = {
    8: 0,
    2: 1,
    11: 2
}
```

### 4. Iterasyon

```text
i = 3
num = 7

complement = 9 - 7
           = 2
```

Bu sefer:

```text
2 in seen → True
```

Dictionary içerisinde:

```text
2 → 1
```

bulunuyor.

Dolayısıyla:

```python
seen[2] = 1
```

ve mevcut indeks:

```text
i = 3
```

olduğu için:

```python
return [1, 3]
```

sonucunu elde ederiz.

---

## Kod

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
```

---

## Neden Önce Kontrol Edip Sonra Ekliyoruz?

Şu sıralama önemlidir:

```python
if complement in seen:
    return [seen[complement], i]

seen[num] = i
```

Mevcut elemanı kontrol işleminden **sonra** Hash Map'e ekliyoruz.

Böylece aynı array elemanını iki kere kullanma problemini önlüyoruz.

Örneğin:

```text
nums = [5, 5]
target = 10
```

İlk `5`:

```text
complement = 5
seen = {}
```

Bulunamaz ve kaydedilir:

```python
seen = {5: 0}
```

İkinci `5` geldiğinde:

```text
complement = 5
```

ve artık:

```text
5 in seen → True
```

olduğu için:

```text
[0, 1]
```

döndürülür.

Yani iki farklı indeks kullanılmış olur.

---

## `enumerate()` Neden Kullanılıyor?

Python'daki:

```python
for i, num in enumerate(nums):
```

ifadesi bize aynı anda hem index'i hem de değeri verir.

Örneğin:

```python
nums = [8, 2, 11]
```

için:

```text
i    num
---------
0     8
1     2
2    11
```

elde edilir.

Bu nedenle:

```python
for i in range(len(nums)):
    num = nums[i]
```

yazmak yerine daha okunabilir olan `enumerate()` kullanılabilir.

---

# Karmaşıklık Analizi

## Brute Force

**Time Complexity**

```text
O(n²)
```

**Space Complexity**

```text
O(1)
```

## Hash Map

**Time Complexity**

```text
O(n)
```

Array yalnızca bir kez dolaşılır.

Hash Map üzerinde arama ve ekleme işlemleri ortalama durumda `O(1)` zamanda gerçekleştirilir.

**Space Complexity**

```text
O(n)
```

En kötü durumda array içerisindeki elemanların büyük kısmı Hash Map içerisinde saklanabilir.

---

# Çözümlerin Karşılaştırılması

| Yaklaşım | Zaman | Ek Alan |
|---|---:|---:|
| Brute Force | O(n²) | O(1) |
| One-Pass Hash Map | O(n) | O(n) |

Hash Map çözümünde ek bellek kullanarak çalışma süresini `O(n²)` seviyesinden `O(n)` seviyesine düşürüyoruz.

Bu durum bir **time-space trade-off** örneğidir.

---

# Bu Problemden Ne Öğrendim?

Two Sum problemindeki en önemli nokta kodu ezberlemek değil, probleme bakış şeklini değiştirmektir.

İlk yaklaşım:

> Hangi iki sayının toplamı target'a eşit?

Optimize yaklaşım:

> Şu anki sayının target'a ulaşması için hangi sayıya ihtiyacım var ve bu sayıyı daha önce gördüm mü?

Bu düşünce:

```text
target - current = complement
```

şeklinde ifade edilebilir.

Ardından Hash Map sayesinde:

```text
"complement daha önce görüldü mü?"
```

sorusunu ortalama `O(1)` zamanda cevaplayabiliriz.

## Öğrenilen Pattern

```text
Mevcut elemanı al
        ↓
İhtiyaç duyulan değeri hesapla
        ↓
Daha önce görülüp görülmediğini kontrol et
        ↓
Hash Map'i güncelle
```

Bu problem özellikle **Hash Map ile hızlı lookup yapma** düşüncesini öğrenmek için temel bir örnektir.