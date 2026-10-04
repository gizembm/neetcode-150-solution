# 347. Top K Frequent Elements

> 📌 Problemin Türkçe açıklaması, örnekleri ve önemli detayları için [`problem.md`](./problem.md) dosyasına bakabilirsiniz.

Bu problemde bir sayı dizisi içerisindeki **en sık tekrar eden `k` farklı elemanı** bulmamız gerekiyor.

Top K Frequent Elements, önceki Arrays & Hashing problemlerinde öğrendiğim **Hash Map** ve **frequency counting** mantığının devamı niteliğinde.

Özellikle Valid Anagram probleminde karakterlerin kaç kez tekrar ettiğini hesaplamıştım.

Bu problemde de benzer şekilde sayıların frekanslarını hesaplıyorum. Ancak bu kez yalnızca frekansları bulmak yeterli değil.

Frekansları bulduktan sonra:

> En yüksek frekansa sahip `k` elemanı nasıl seçebilirim?

sorusunu da çözmem gerekiyor.

Bu problem için iki farklı yaklaşım kullandım:

1. **Hash Map + Sorting**
2. **Hash Map + Bucket Sort**

---

# Problemi Nasıl Düşündüm?

Örneğin:

```text
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

verilmiş olsun.

İlk olarak her sayının kaç kez tekrar ettiğini bulabilirim.

```text
1 → 1 kez
2 → 2 kez
3 → 3 kez
```

Bunu bir Hash Map kullanarak temsil edebilirim:

```python
count = {
    1: 1,
    2: 2,
    3: 3
}
```

Burada:

```text
key   → sayı
value → sayının frekansı
```

anlamına geliyor.

Yani:

```text
count[1] = 1
count[2] = 2
count[3] = 3
```

`k = 2` olduğuna göre frekansı en yüksek iki farklı elemanı bulmam gerekiyor.

Bu örnekte:

```text
3 → 3 kez
2 → 2 kez
1 → 1 kez
```

olduğu için cevap:

```text
[3, 2]
```

olabilir.

Sonuç herhangi bir sırada döndürülebildiği için:

```text
[2, 3]
```

de geçerlidir.

---

# Frequency Counting

Problemin iki çözümünde de ilk adım aynıdır.

Her sayının kaç kez tekrar ettiğini hesaplamam gerekiyor.

Bunun için bir dictionary kullanabilirim:

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1
```

Örneğin:

```text
nums = [1, 2, 2, 3, 3, 3]
```

için dictionary'nin gelişimi şu şekilde olur:

```text
başlangıç:

{}

1 işlendi:

{1: 1}

2 işlendi:

{1: 1, 2: 1}

ikinci 2 işlendi:

{1: 1, 2: 2}

3 işlendi:

{1: 1, 2: 2, 3: 1}

ikinci 3 işlendi:

{1: 1, 2: 2, 3: 2}

üçüncü 3 işlendi:

{1: 1, 2: 2, 3: 3}
```

Sonuç:

```python
count = {
    1: 1,
    2: 2,
    3: 3
}
```

Bu noktadan sonra problem:

> Bu dictionary içerisinden value değeri en yüksek olan `k` key'i nasıl bulabilirim?

sorusuna dönüşüyor.

---

# Yaklaşım 1 — Sorting

İlk akla gelen yöntem, frekansları hesapladıktan sonra sayıları **frekanslarına göre sıralamak**.

Elimizde:

```python
count = {
    1: 1,
    2: 2,
    3: 3
}
```

olsun.

Frekansa göre büyükten küçüğe sıraladığımızda:

```text
3 → 3 kez
2 → 2 kez
1 → 1 kez
```

elde ederiz.

`k = 2` olduğuna göre sıralanmış yapıdan ilk iki elemanı almamız yeterlidir:

```text
[3, 2]
```

---

## Neden Normal Sorting Yeterli Değil?

Eğer doğrudan:

```python
sorted(count)
```

kullanırsam dictionary'nin key'leri kendi değerlerine göre sıralanır.

Ancak problemde sayıların büyüklüğü önemli değildir.

Örneğin:

```python
nums = [100, 100, 5, 5, 5, 1]
```

için frekanslar:

```python
count = {
    100: 2,
    5: 3,
    1: 1
}
```

şeklindedir.

Normal sıralama sayıların kendisine bakar.

Fakat bizim istediğimiz:

```text
5   → 3 kez
100 → 2 kez
1   → 1 kez
```

şeklinde **frekansa göre** sıralamaktır.

Bu nedenle sorting işleminin hangi değere göre yapılacağını belirtmem gerekiyor.

---

## `key=count.get` Ne İşe Yarıyor?

Python'da:

```python
sorted(count, key=count.get, reverse=True)
```

kullanabilirim.

Buradaki:

```python
key=count.get
```

ifadesi sıralama sırasında dictionary key'inin kendisini değil, o key'e karşılık gelen value değerini kullanmamızı sağlar.

Örneğin:

```python
count = {
    100: 2,
    5: 3,
    1: 1
}
```

için Python karşılaştırma sırasında şunlara bakar:

```text
count.get(100) → 2
count.get(5)   → 3
count.get(1)   → 1
```

`reverse=True` kullandığım için büyük frekanstan küçük frekansa doğru sıralama yapılır.

Sonuç:

```text
[5, 100, 1]
```

olur.

Daha sonra:

```python
frequent[:k]
```

ile ilk `k` elemanı alabilirim.

---

## Sorting Çözümü

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequent = sorted(count, key=count.get, reverse=True)

        return frequent[:k]
```

---

## Sorting Çözümünün Adımları

Algoritmanın genel akışı:

```text
nums
 ↓
Her elemanın frekansını hesapla
 ↓
sayı → frekans
 ↓
Elemanları frekanslarına göre sırala
 ↓
En yüksek frekanstan en düşüğe
 ↓
İlk k elemanı al
```

Örneğin:

```text
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

için:

```text
nums
 ↓
{1: 1, 2: 2, 3: 3}
 ↓
[3, 2, 1]
 ↓
ilk 2 eleman
 ↓
[3, 2]
```

---

## Sorting Çözümünün Karmaşıklığı

`n` dizideki toplam eleman sayısı, `m` ise farklı eleman sayısı olsun.

Frekansları hesaplamak:

```text
O(n)
```

zaman alır.

Farklı elemanları frekanslarına göre sıralamak:

```text
O(m log m)
```

zaman alır.

Bu nedenle toplam zaman karmaşıklığı:

```text
O(n + m log m)
```

olur.

En kötü durumda bütün elemanlar birbirinden farklı olabilir.

Bu durumda:

```text
m = n
```

olacağından en kötü durum:

```text
O(n log n)
```

olarak düşünülebilir.

---

# Yaklaşım 2 — Bucket Sort

Sorting çözümü problemi çözüyor.

Ancak burada şu soruyu sorabiliriz:

> Frekansları gerçekten sıralamak zorunda mıyım?

Bu noktada problemdeki önemli bir özellik kullanılabilir.

Bir elemanın frekansı sınırsız değildir.

Eğer dizide `n` tane eleman varsa herhangi bir sayının maksimum frekansı `n` olabilir.

Örneğin:

```text
nums = [7, 7, 7, 7, 7]
```

için:

```text
n = 5
```

ve:

```text
7 → 5 kez
```

olur.

Dolayısıyla bir sayının frekansı:

```text
1 ... n
```

aralığındadır.

Bu bilgi sayesinde frekansı doğrudan bir **array index'i** olarak kullanabiliriz.

Bucket Sort yaklaşımının temel fikri buradan geliyor.

---

# Bucket Yapısını Oluşturmak

Şöyle bir liste oluşturuyorum:

```python
freq = [[] for _ in range(len(nums) + 1)]
```

Örneğin:

```text
len(nums) = 6
```

ise:

```text
freq = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
```

oluşur.

Neden `len(nums) + 1`?

Çünkü index değerlerini doğrudan frekans olarak kullanmak istiyorum.

Index `0` kullanılmayacak olsa bile:

```text
freq[1]
freq[2]
freq[3]
...
freq[n]
```

şeklinde frekans değerlerine doğrudan erişebilmek istiyorum.

---

# Bucket Index'i Ne Anlama Geliyor?

Bu yapıda:

```text
freq[1] → 1 kez görülen sayılar
freq[2] → 2 kez görülen sayılar
freq[3] → 3 kez görülen sayılar
...
freq[n] → n kez görülen sayılar
```

anlamına geliyor.

Örneğin:

```python
nums = [1, 2, 2, 3, 3, 3]
```

için:

```python
count = {
    1: 1,
    2: 2,
    3: 3
}
```

elde etmiştim.

Şimdi her sayıyı kendi frekansına karşılık gelen bucket'a yerleştirebilirim.

```python
for num, frequency in count.items():
    freq[frequency].append(num)
```

Adım adım:

```text
1 sayısının frekansı = 1
↓
freq[1].append(1)

2 sayısının frekansı = 2
↓
freq[2].append(2)

3 sayısının frekansı = 3
↓
freq[3].append(3)
```

Sonuç:

```text
index      bucket

0       →  []
1       →  [1]
2       →  [2]
3       →  [3]
4       →  []
5       →  []
6       →  []
```

Burada aslında ilk Hash Map'teki ilişkiyi tersine çevirmiş oldum.

Başlangıçta:

```text
sayı → frekans
```

vardı.

Bucket yapısında ise:

```text
frekans → sayılar
```

haline geldi.

---

# Neden Her Bucket Bir Liste?

Aynı frekansa sahip birden fazla sayı olabilir.

Örneğin:

```text
nums = [1, 1, 2, 2, 3]
```

için:

```text
1 → 2 kez
2 → 2 kez
3 → 1 kez
```

olur.

Burada hem `1` hem de `2` aynı frekansa sahiptir.

Bu nedenle:

```text
freq[1] → [3]
freq[2] → [1, 2]
```

şeklinde bir yapı oluşmalıdır.

Bu yüzden:

```python
freq
```

içerisindeki her eleman tek bir sayı değil, bir **liste** olmak zorundadır.

---

# Bucket'ları Neden Tersten Geziyoruz?

Bucket index'i doğrudan frekansı temsil ediyor.

Örneğin:

```text
freq[1] → düşük frekans
freq[2]
freq[3]
...
freq[n] → yüksek frekans
```

Biz en yüksek frekanslı elemanları istediğimiz için `freq` listesini sondan başa doğru gezmemiz gerekir.

Bunu:

```python
for i in range(len(freq) - 1, 0, -1):
```

ile yapabiliriz.

Buradaki:

```python
range(start, stop, step)
```

mantığına göre:

```text
start → len(freq) - 1
stop  → 0
step  → -1
```

olur.

Örneğin `freq` uzunluğu `7` ise:

```python
range(6, 0, -1)
```

şu değerleri üretir:

```text
6, 5, 4, 3, 2, 1
```

Böylece en yüksek frekanstan en düşük frekansa doğru ilerleriz.

---

# Sonuçları Toplamak

Her bucket içerisinde birden fazla sayı bulunabileceği için iki döngü kullanıyorum:

```python
for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
```

Bulduğum sayıları:

```python
result.append(num)
```

ile sonuç listesine ekliyorum.

Problem yalnızca `k` tane eleman istediği için:

```python
if len(result) == k:
    return result
```

kontrolünü yapıyorum.

Böylece gerekli sayıda elemanı bulduğum anda algoritmayı sonlandırabiliyorum.

---

# Bucket Sort Çözümü

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            freq[frequency].append(num)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
```

---

# Bucket Sort Adım Adım

Şu örneği kullanalım:

```text
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

### 1. Frekansları hesapla

```text
count = {
    1: 1,
    2: 2,
    3: 3
}
```

### 2. Bucket'ları oluştur

```text
freq[0] → []
freq[1] → [1]
freq[2] → [2]
freq[3] → [3]
freq[4] → []
freq[5] → []
freq[6] → []
```

### 3. En yüksek frekanstan başla

```text
freq[6] → []
freq[5] → []
freq[4] → []
```

Henüz eleman bulamadık.

Sonra:

```text
freq[3] → [3]
```

olduğu için:

```text
result = [3]
```

olur.

Devam ederiz:

```text
freq[2] → [2]
```

ve:

```text
result = [3, 2]
```

olur.

### 4. `k` kontrolü

```text
len(result) = 2
k = 2
```

olduğu için:

```python
return result
```

çalışır.

Sonuç:

```text
[3, 2]
```

olur.

---

# Bucket Sort Karmaşıklığı

Frekansları hesaplamak için `nums` dizisini bir kez geziyorum:

```text
O(n)
```

Bucket listesini oluşturmak:

```text
O(n)
```

Elemanları frekanslarına göre bucket'lara yerleştirmek:

```text
O(m)
```

zaman alır.

Burada `m`, farklı eleman sayısıdır ve:

```text
m <= n
```

olduğu için bu işlem de en fazla `O(n)` olur.

Bucket'ları sondan başa doğru taramak da:

```text
O(n)
```

zaman alır.

Dolayısıyla toplam zaman karmaşıklığı:

```text
O(n)
```

olur.

Bucket listesi ve Hash Map için ek alan kullandığımızdan:

```text
Space Complexity: O(n)
```

olur.

---

# Sorting ve Bucket Sort Karşılaştırması

| Yaklaşım | Time Complexity | Space Complexity | Temel Fikir |
|---|---|---|---|
| Sorting | `O(n + m log m)` | Ek alan gerekir | Frekansları hesapla ve frekansa göre sırala |
| Bucket Sort | `O(n)` | `O(n)` | Frekansı doğrudan array index'i olarak kullan |

Burada:

```text
n → nums içerisindeki toplam eleman sayısı
m → farklı eleman sayısı
```

anlamına gelir.

Sorting yaklaşımı daha sezgisel ve kısa bir çözümdür.

Bucket Sort ise problemin frekanslarının sınırlı bir aralıkta olması özelliğinden yararlanarak sorting işlemini tamamen ortadan kaldırır.

---

# Bucket Sort Neden Runtime Testinde Her Zaman Daha Hızlı Görünmeyebilir?

Teorik olarak:

```text
Sorting    → O(n log n) worst case
Bucket     → O(n)
```

olmasına rağmen bazı online judge testlerinde Sorting çözümü daha hızlı görünebilir.

Bunun nedenlerinden biri Python'ın:

```python
sorted()
```

fonksiyonunun oldukça optimize edilmiş olmasıdır.

Bucket Sort çözümünde ise Python seviyesinde:

- `n + 1` tane bucket oluşturulur,
- dictionary üzerinde dolaşılır,
- bucket'lar doldurulur,
- bucket listesi tersten taranır,
- iç içe döngüler çalıştırılır.

Bu işlemlerin sabit maliyetleri vardır.

Bu nedenle özellikle küçük veya orta büyüklükteki inputlarda gerçek runtime değerleri teorik karmaşıklıkla birebir aynı sıralamayı göstermeyebilir.

Online judge üzerindeki `Beats %` değerleri de çalışma ortamına ve ölçümlere göre değişebilir.

Bu nedenle algoritmaları değerlendirirken yalnızca tek bir runtime sonucuna değil, **time ve space complexity'ye ve kullanılan algoritmik fikre** bakmak daha doğru olur.

---

# Bu Problemden Ne Öğrendim?

Bu problemde ilk olarak daha önce kullandığım frequency counting yaklaşımını tekrar kullandım:

```text
sayı → frekans
```

Bunun için:

```python
count[num] = count.get(num, 0) + 1
```

pattern'ini kullandım.

Ancak bu kez frequency counting problemin yalnızca ilk kısmıydı.

Asıl yeni öğrendiğim fikir:

> Frekans gibi sınırlı bir integer değerini doğrudan bir array index'i olarak kullanabilmek.

Bucket Sort yaklaşımında:

```text
sayı → frekans
```

ilişkisini:

```text
frekans → sayılar
```

şeklinde yeniden düzenledim.

Böylece frekansları ayrıca sıralamaya gerek kalmadan en yüksek frekanslı elemanlara doğrudan ulaşabildim.

---

# Önceki Problemlerle Bağlantısı

Arrays & Hashing bölümünde Hash Map ve Set'i farklı amaçlarla kullandım.

### Two Sum

```text
sayı → index
```

Bir sayının ihtiyaç duyduğum complement'ini daha önce görüp görmediğimi kontrol ettim.

### Contains Duplicate

```text
daha önce gördüm mü?
```

sorusunu çözmek için Hash Set kullandım.

### Valid Anagram

```text
karakter → frekans
```

ilişkisini kullanarak iki kelimenin aynı karakterlerden aynı sayıda içerip içermediğini kontrol ettim.

### Group Anagrams

```text
frekans imzası → kelimeler
```

ilişkisini kullanarak aynı karakter frekansına sahip kelimeleri aynı grupta topladım.

### Top K Frequent Elements

Bu kez iki farklı ilişki kullandım:

```text
sayı → frekans
```

ve ardından:

```text
frekans → sayılar
```

Özellikle Valid Anagram'da öğrendiğim **frequency counting** mantığını burada daha ileri bir seviyede kullanmış oldum.

---

# Öğrendiğim Pattern

Bu problemden çıkarabileceğim ilk genel pattern:

> Bir problem elemanların kaç kez tekrar ettiğini soruyorsa Hash Map ile **frequency counting** düşün.

Örneğin:

```python
count[num] = count.get(num, 0) + 1
```

İkinci önemli pattern ise:

> Eğer kullandığım değer belirli ve küçük/sınırlı bir integer aralığındaysa, bu değeri bir array index'i olarak kullanıp kullanamayacağımı kontrol et.

Bu problemde:

```text
frequency
    ↓
bucket index
```

olarak kullandım.

Bu sayede:

```text
frequency counting
        ↓
bucket oluşturma
        ↓
yüksek frekanstan düşük frekansa tarama
        ↓
top k eleman
```

şeklinde `O(n)` bir çözüm elde ettim.

---

# Kısa Özet

Bu problemde öğrendiğim temel akış:

```text
nums
 ↓
Hash Map ile frekansları hesapla
 ↓
sayı → frekans
 ↓
frekansı bucket index'i olarak kullan
 ↓
frekans → sayılar
 ↓
bucket'ları sondan başa tara
 ↓
ilk k elemanı döndür
```

En önemli kazanımım yalnızca Top K Frequent Elements problemini çözmek değil, **frequency counting sonucunu başka bir veri yapısına dönüştürerek sorting ihtiyacını ortadan kaldırabileceğimi görmek** oldu.