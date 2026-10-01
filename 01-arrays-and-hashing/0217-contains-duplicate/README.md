# 217. Contains Duplicate

**Zorluk:** Easy  
**Konu:** Arrays & Hashing

## Problem

Bir `nums` tam sayı listesi veriliyor.

Amacımız, listede herhangi bir değerin birden fazla kez bulunup bulunmadığını kontrol etmek.

Eğer en az bir değer tekrar ediyorsa:

```python
True
```

hiçbir değer tekrar etmiyorsa:

```python
False
```

döndürülür.

### Örnek 1

```text
Input:
nums = [1, 2, 3, 3]

Output:
True
```

Çünkü `3` değeri listede iki kez bulunmaktadır.

### Örnek 2

```text
Input:
nums = [1, 2, 3, 4]

Output:
False
```

Çünkü bütün değerler birbirinden farklıdır.

---

# Çözüm 1 — Brute Force

## Yaklaşım

Problemi çözmenin en basit yollarından biri her elemanı diğer elemanlarla karşılaştırmaktır.

Örneğin:

```text
nums = [1, 2, 3, 3]

1 → 2, 3, 3
2 → 3, 3
3 → 3
    ↑
 duplicate
```

Aynı değere sahip iki farklı eleman bulunduğu anda `True` döndürülür.

## Kod

```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
```

## Karmaşıklık

**Zaman:**

```text
O(n²)
```

Her eleman diğer elemanlarla karşılaştırılabileceği için büyük inputlarda verimsizdir.

**Alan:**

```text
O(1)
```

Input boyutuna bağlı ek bir veri yapısı kullanılmaz.

### Neden tercih etmiyoruz?

Problemde:

```text
nums.length <= 10^5
```

olabilir.

Yani liste 100.000 elemana kadar çıkabilir.

`O(n²)` çözüm büyük inputlarda çok fazla karşılaştırma yapabileceği için iyi ölçeklenmez.

Brute Force yine de problemin en temel çözümünü görmek ve optimizasyon ihtiyacını anlamak açısından faydalıdır.

---

# Çözüm 2 — Sorting

## Yaklaşım

Listeyi sıraladığımızda aynı değerler yan yana gelir.

Örneğin:

```text
[4, 2, 1, 3, 2]

        ↓ sorting

[1, 2, 2, 3, 4]
    ↑  ↑
```

Artık bütün eleman çiftlerini kontrol etmek yerine sadece komşu elemanları karşılaştırabiliriz.

## Kod

```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
```

## Karmaşıklık

**Zaman:**

```text
O(n log n)
```

Sıralama işlemi baskın olduğu için toplam zaman karmaşıklığı `O(n log n)` olur.

### Dikkat Edilmesi Gereken Nokta

```python
nums.sort()
```

orijinal listeyi değiştirir.

Örneğin:

```python
nums = [3, 1, 2]

nums.sort()

print(nums)
```

çıktısı:

```text
[1, 2, 3]
```

olacaktır.

Bu nedenle input'un değiştirilmemesi gereken problemlerde bu davranış dikkate alınmalıdır.

---

# Çözüm 3 — Hash Set

Bu problem için en önemli yaklaşım Hash Set kullanmaktır.

## Problemi Farklı Düşünmek

Aslında ihtiyacımız olan bilgi oldukça basit:

> Şu an baktığım sayıyı daha önce gördüm mü?

Bir değerin daha önce görülüp görülmediğini hızlı şekilde kontrol etmek için Hash Set kullanabiliriz.

Python'da:

```python
seen = set()
```

ile boş bir set oluşturabiliriz.

---

## Algoritma

Her sayı için:

1. Sayının `seen` içerisinde olup olmadığını kontrol et.
2. Varsa duplicate bulduk → `True`.
3. Yoksa sayıyı `seen` içerisine ekle.
4. Liste biterse duplicate yoktur → `False`.

```text
Mevcut sayı
     ↓
Daha önce görüldü mü?
    /       \
  Evet      Hayır
   ↓          ↓
 True      Set'e ekle
```

---

## Adım Adım Örnek

```python
nums = [7, 4, 9, 2, 4]
```

Başlangıç:

```python
seen = set()
```

### 1. Iterasyon

```text
num = 7

7 in seen → False
```

Eklenir:

```text
seen = {7}
```

### 2. Iterasyon

```text
num = 4

4 in seen → False
```

Eklenir:

```text
seen = {7, 4}
```

### 3. Iterasyon

```text
num = 9

9 in seen → False
```

Eklenir:

```text
seen = {7, 4, 9}
```

### 4. Iterasyon

```text
num = 2

2 in seen → False
```

Eklenir:

```text
seen = {7, 4, 9, 2}
```

### 5. Iterasyon

```text
num = 4

4 in seen → True
```

`4` daha önce görüldüğü için:

```python
return True
```

çalışır.

---

## Kod

```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

## Karmaşıklık

**Zaman:**

```text
O(n)
```

Liste bir kez dolaşılır.

Hash Set üzerinde arama ve ekleme işlemleri ortalama durumda `O(1)` zamanda gerçekleştirilir.

**Alan:**

```text
O(n)
```

Duplicate bulunmadığı durumda bütün değerlerin `seen` içerisinde saklanması gerekebilir.

---

# Çözüm 4 — Set Uzunluklarını Karşılaştırmak

Python'da `set` tekrar eden değerleri yalnızca bir kez saklar.

Örneğin:

```python
nums = [1, 2, 3, 3]
```

için:

```python
set(nums)
```

sonucu:

```text
{1, 2, 3}
```

olur.

Dolayısıyla:

```text
len(nums)      = 4
len(set(nums)) = 3
```

Uzunluklar farklıysa duplicate olduğunu anlayabiliriz.

## Kod

```python
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
```

## Karmaşıklık

**Zaman:**

```text
O(n)
```

**Alan:**

```text
O(n)
```

Bu çözüm kısa ve Python'a özgü oldukça temiz bir çözümdür.

Ancak algoritmayı öğrenme açısından Hash Set'i açık şekilde kullanan çözüm, arkasındaki düşünceyi daha iyi göstermektedir.

---

# Çözümlerin Karşılaştırılması

| Yaklaşım | Zaman | Ek Alan | Not |
|---|---:|---:|---|
| Brute Force | O(n²) | O(1) | Basit ancak büyük inputlarda yavaş |
| Sorting | O(n log n) | Uygulamaya bağlı | Duplicate değerleri yan yana getirir |
| Hash Set | O(n) ortalama | O(n) | Problemin temel hashing yaklaşımı |
| Set Length | O(n) ortalama | O(n) | Kısa ve Pythonic |

---

# Neden Hash Set?

Bu problemde herhangi bir değerle ilgili ek bilgi saklamamız gerekmiyor.

Sadece:

> Bu değer daha önce görüldü mü?

sorusunun cevabına ihtiyacımız var.

Bu nedenle `dict` yerine `set` kullanmak yeterlidir.

Two Sum probleminde ise:

```text
sayı → index
```

bilgisine ihtiyacımız olduğu için `dict` kullanmıştık.

Karşılaştırırsak:

```text
Contains Duplicate
        ↓
"Sayı daha önce görüldü mü?"
        ↓
       set
```

```text
Two Sum
        ↓
"Complement daha önce görüldü mü
ve index'i neydi?"
        ↓
       dict
```

---

# Bu Problemden Ne Öğrendim?

Bu problemden çıkardığım en önemli pattern:

> Bir değeri daha önce görüp görmediğimi hızlı bir şekilde kontrol etmem gerekiyorsa Hash Set düşünebilirim.

Brute Force çözümünde tekrar tekrar liste içerisinde arama yaparken, Hash Set sayesinde üyelik kontrolünü ortalama `O(1)` zamanda gerçekleştirebiliyoruz.

Temel düşünce:

```text
Değeri al
    ↓
Daha önce gördüm mü?
    ↓
  Hash Set
   /    \
 Evet   Hayır
  ↓       ↓
True    Kaydet
```

Bu problem aynı zamanda algoritmalarda sık karşılaşılan bir **time-space trade-off** örneğidir.

Brute Force:

```text
O(n²) zaman
O(1) ek alan
```

Hash Set:

```text
O(n) zaman
O(n) ek alan
```

Yani ek bellek kullanarak algoritmanın çalışma süresini önemli ölçüde iyileştirmiş oluyoruz.