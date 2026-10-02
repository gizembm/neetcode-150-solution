# 242. Valid Anagram

> 📌 Problemin Türkçe açıklaması ve örnekleri için [`problem.md`](./problem.md) dosyasına bakabilirsiniz.

## Problemi Nasıl Düşündüm?

İki stringin anagram olup olmadığını anlamak için aslında iki şeyi kontrol etmemiz gerekiyor:

1. Aynı karakterleri içeriyorlar mı?
2. Bu karakterler aynı sayıda mı tekrar ediyor?

Örneğin:

```text
s = "aabc"
t = "abca"
```

Karakterleri saydığımızda:

```text
        s       t

a       2       2
b       1       1
c       1       1
```

olduğunu görüyoruz.

Karakterlerin sırası farklı olsa da frekansları aynı olduğu için bu iki string anagramdır.

Buradan problemin temel fikrine ulaşabiliriz:

> Her karakterin kaç kez geçtiğini bulabilirsek iki stringi karşılaştırabiliriz.

Fakat bunu yapmanın birden fazla yolu var.

---

# 1. Yaklaşım — Sorting

İlk akla gelebilecek çözümlerden biri iki stringin karakterlerini sıralamaktır.

Anagram olan iki string aynı karakterleri aynı sayıda içerdiği için sıralandıktan sonra aynı hale gelmelidir.

Örneğin:

```text
racecar → aaccerr
carrace → aaccerr
```

İki sonuç aynı olduğu için stringler anagramdır.

## Kod

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
```

## Neden Çalışıyor?

Karakterlerin başlangıçtaki sırası bizim için önemli değil.

Sorting işlemi iki stringde bulunan karakterleri belirli bir sıraya sokar. Eğer karakterler ve tekrar sayıları gerçekten aynıysa sıralama sonucunda aynı diziyi elde ederiz.

Örneğin:

```text
"jar" → ['a', 'j', 'r']
"jam" → ['a', 'j', 'm']
```

Sonuçlar farklı olduğu için anagram olmadıklarını anlayabiliriz.

## Karmaşıklık

```text
Time Complexity: O(n log n)
```

Çünkü karakterleri sıralamamız gerekir.

Bu çözüm kısa ve anlaşılırdır. Ancak problemi çözmek için aslında karakterleri sıralamaya ihtiyacımız yoktur. İhtiyacımız olan bilgi her karakterin kaç kez geçtiğidir.

Bu nedenle daha verimli bir çözüm arayabiliriz.

---

# 2. Yaklaşım — Hash Map ile Frekans Sayma

Bu problemde öğrenmek istediğim temel yaklaşım **frequency counting**.

Her karakter için şu bilgiyi saklayabiliriz:

```text
karakter → görülme sayısı
```

Örneğin:

```text
s = "aabc"
```

için oluşturacağımız dictionary:

```python
{
    "a": 2,
    "b": 1,
    "c": 1
}
```

olur.

Aynı işlemi `t` için de yapıp iki dictionary'yi karşılaştırabiliriz.

---

## Karakterleri Nasıl Sayıyoruz?

Python'da şu yapı oldukça kullanışlı:

```python
count_s[char] = count_s.get(char, 0) + 1
```

Buradaki:

```python
count_s.get(char, 0)
```

ifadesi şu anlama gelir:

> Eğer `char` dictionary içerisinde varsa mevcut değerini getir, yoksa `0` kabul et.

Örneğin ilk `a` geldiğinde:

```text
count_s = {}

"a" henüz yok.

get("a", 0) → 0
0 + 1 → 1
```

Sonuç:

```python
{"a": 1}
```

İkinci `a` geldiğinde ise:

```text
get("a", 0) → 1
1 + 1 → 2
```

Sonuç:

```python
{"a": 2}
```

Yeni karakterler geldikçe dictionary büyümeye devam eder:

```text
{}
↓
{"a": 1}
↓
{"a": 2}
↓
{"a": 2, "b": 1}
↓
{"a": 2, "b": 1, "c": 1}
```

---

## Kod

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
```

---

## Neden Önce Uzunlukları Kontrol Ediyoruz?

Kodun başında:

```python
if len(s) != len(t):
    return False
```

kontrolü bulunuyor.

Çünkü iki stringin uzunlukları farklıysa aynı karakterleri aynı sayıda içermeleri zaten mümkün değildir.

Örneğin:

```text
s = "cat"   → 3 karakter
t = "cats"  → 4 karakter
```

Bu durumda diğer işlemleri yapmadan doğrudan `False` dönebiliriz.

Bu tür kontrollere **early return** denir.

---

## Karmaşıklık

Her iki stringi de bir kez dolaşıyoruz.

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

Hash Map üzerinde arama ve ekleme işlemleri ortalama durumda `O(1)` zamanda gerçekleşir.

Sorting çözümündeki `O(n log n)` yerine bu yaklaşım ile ortalama `O(n)` zamanda çözüm elde etmiş oluruz.

---

# 3. Yaklaşım — Counter

Python'daki `collections.Counter`, elemanların kaç kez tekrar ettiğini hesaplamak için hazır olarak kullanılabilir.

Bizim elle oluşturduğumuz:

```python
{
    "a": 2,
    "b": 1,
    "c": 1
}
```

gibi frekans bilgisini `Counter` bizim için oluşturabilir.

## Kod

```python
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

Bu çözüm oldukça kısa ve Pythonic'tir.

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

Ancak algoritmayı öğrenirken Hash Map çözümünü ayrıca anlamak önemli. Çünkü birçok problemde hazır `Counter` kullanmak yerine frekans bilgisini kendimiz yönetmemiz gerekebilir.

---

# 4. Yaklaşım — 26 Elemanlı Frequency Array

Problemde önemli bir constraint bulunuyor:

> `s` ve `t` yalnızca küçük İngilizce harflerden (`a-z`) oluşur.

İngilizce alfabede 26 harf olduğu için Hash Map yerine doğrudan 26 elemanlı bir sayaç oluşturabiliriz.

```python
count = [0] * 26
```

Bu listenin her indexini bir harfe karşılık gelecek şekilde düşünebiliriz:

```text
index 0  → a
index 1  → b
index 2  → c
...
index 25 → z
```

---

## Harfi Index'e Nasıl Çeviriyoruz?

Bunun için `ord()` fonksiyonunu kullanabiliriz.

```python
ord("a")  # 97
ord("b")  # 98
ord("c")  # 99
```

Bir karakterden `ord("a")` değerini çıkardığımızda `0-25` arasında bir index elde ederiz.

```text
a → 97 - 97 = 0
b → 98 - 97 = 1
c → 99 - 97 = 2
```

Kodda:

```python
index = ord(char) - ord("a")
```

şeklinde kullanabiliriz.

---

## +1 ve -1 Mantığı

`s` içerisindeki karakterleri gördüğümüzde ilgili sayacı artırıyoruz:

```python
count[index] += 1
```

`t` içerisindeki karakterleri gördüğümüzde ise azaltıyoruz:

```python
count[index] -= 1
```

Örneğin:

```text
s = "aabc"
t = "abca"
```

`s` tamamlandıktan sonra listenin başlangıcı:

```text
a  b  c
↓  ↓  ↓

2  1  1
```

olur.

Daha sonra `t` içerisindeki karakterleri çıkarırız:

```text
a → -1
b → -1
c → -1
a → -1
```

Sonuç:

```text
a  b  c
↓  ↓  ↓

0  0  0
```

Eğer iki string anagramsa bütün karakterlerin sayıları birbirini götürmelidir.

---

## Kod

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            count[index] += 1

        for char in t:
            index = ord(char) - ord("a")
            count[index] -= 1

        return all(value == 0 for value in count)
```

Buradaki:

```python
all(value == 0 for value in count)
```

ifadesi `count` içerisindeki bütün değerlerin `0` olup olmadığını kontrol eder.

Bir değer bile `0` değilse karakter frekanslarından biri eşleşmiyor demektir.

---

## Karmaşıklık

```text
Time Complexity: O(n)
Space Complexity: O(1)
```

Neden `O(1)`?

Çünkü `count` listesi input büyüdükçe büyümez.

String ister 10 karakter ister 50.000 karakter olsun:

```python
count = [0] * 26
```

her zaman yalnızca 26 eleman içerir.

Bu çözüm problemde verilen `a-z` constraint'inden doğrudan yararlanır.

---

# Çözümleri Karşılaştıralım

| Yaklaşım | Zaman | Ek Alan | Özellik |
|---|---:|---:|---|
| Sorting | O(n log n) | Uygulamaya bağlı | Basit ve anlaşılır |
| Hash Map | O(n) | O(n) | Frequency counting mantığını açıkça gösterir |
| Counter | O(n) | O(n) | Kısa ve Pythonic |
| Frequency Array | O(n) | O(1) | `a-z` constraint'inden yararlanır |

Bu problemde özellikle **Hash Map çözümü**, ileride başka problemlerde de kullanabileceğimiz frequency counting pattern'ini öğrettiği için önemli.

Frequency Array çözümü ise bize başka bir önemli noktayı gösteriyor:

> Problemde verilen constraint'ler bazen daha özel ve daha verimli bir çözüm geliştirmemizi sağlayabilir.

---

# Bu Problemden Ne Öğrendim?

Bu problemde benim için en önemli yeni kavram **frequency counting** oldu.

Bir problemde:

> Her eleman veya karakter kaç kez tekrar ediyor?

sorusunu soruyorsam bir frequency map oluşturmayı düşünebilirim.

Örneğin:

```python
count[char] = count.get(char, 0) + 1
```

ile:

```text
karakter → frekans
```

bilgisini tutabiliyorum.

Önceki problemlerle birlikte düşününce Hashing'in farklı kullanım alanları daha net hale geliyor:

```text
Two Sum
"Bu değerle ilişkili hangi index'i saklamalıyım?"
→ Hash Map
→ value : index


Contains Duplicate
"Bu değeri daha önce gördüm mü?"
→ Hash Set


Valid Anagram
"Bu karakteri kaç kez gördüm?"
→ Hash Map
→ character : frequency
```

Yani önemli olan sadece `dict` veya `set` kullanmayı bilmek değil; **problemde hangi bilgiyi saklamaya ihtiyacım olduğunu fark etmek**.

Bu problemden çıkardığım temel pattern:

> Bir problemin çözümü elemanların kaç kez tekrar ettiğine bağlıysa frequency counting / Hash Map düşün.