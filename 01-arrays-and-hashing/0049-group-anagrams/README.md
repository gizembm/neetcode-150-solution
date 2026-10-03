# 49. Group Anagrams

> 📌 Problemin Türkçe açıklaması ve örnekleri için [`problem.md`](./problem.md) dosyasına bakabilirsiniz.

## Problemi Nasıl Düşündüm?

Bu problem, bir önceki **Valid Anagram** probleminin devamı gibi düşünülebilir.

Valid Anagram'da iki kelime veriliyor ve şu soruyu soruyorduk:

> Bu iki kelime aynı karakterleri aynı sayıda içeriyor mu?

Group Anagrams'ta ise elimizde iki kelime yerine bir kelime listesi bulunuyor:

```python
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
```

Bu kez amacımız anagram olup olmadıklarını sadece kontrol etmek değil, **birbirinin anagramı olan kelimeleri aynı grupta toplamak**.

Örneğin:

```text
act ──┐
      ├── aynı grup
cat ──┘


pots ──┐
tops ──┼── aynı grup
stop ──┘


hat ────── farklı grup
```

Burada çözmemiz gereken asıl problem şu hale geliyor:

> Bir kelimenin hangi anagram grubuna ait olduğunu nasıl temsil edebilirim?

Bunun için her anagram grubuna ortak olacak bir **key** oluşturmamız gerekiyor.

Anagram olan kelimeler aynı key'i üretirse, Hash Map kullanarak onları aynı key altında gruplayabiliriz.

---

# 1. Yaklaşım — Sorting

İlk yaklaşımda her kelimenin karakterlerini sıralayarak ortak bir key oluşturabiliriz.

Örneğin:

```text
"act" → "act"
"cat" → "act"
```

Her iki kelime de sıralandığında aynı sonucu verdi.

Dolayısıyla:

```text
key = "act"
```

değerini bu iki kelimenin ortak anagram kimliği olarak kullanabiliriz.

Başka bir örnek:

```text
"pots" → "opst"
"tops" → "opst"
"stop" → "opst"
```

Üç kelime de aynı key'i ürettiği için aynı gruba ait olduklarını anlayabiliriz.

---

## Hash Map Nasıl Kullanılıyor?

Başlangıçta boş bir dictionary oluşturuyoruz:

```python
groups = {}
```

Bu dictionary'nin yapısı:

```text
anagram key → o gruba ait kelimeler
```

şeklinde olacak.

Örneğin:

```python
{
    "act": ["act", "cat"],
    "opst": ["pots", "tops", "stop"],
    "aht": ["hat"]
}
```

Her kelime için key oluşturduktan sonra key daha önce görülmediyse yeni bir grup oluşturuyoruz:

```python
if key not in groups:
    groups[key] = []
```

Daha sonra kelimeyi ilgili gruba ekliyoruz:

```python
groups[key].append(word)
```

---

## Kod

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
```

---

## Neden `groups.values()` Kullanıyoruz?

Dictionary içerisinde key'leri yalnızca grupları oluşturmak için kullanıyoruz.

Problem bizden:

```python
{
    "act": ["act", "cat"],
    "opst": ["pots", "tops", "stop"]
}
```

şeklinde bir dictionary istemiyor.

Sadece grupları istiyor:

```python
[
    ["act", "cat"],
    ["pots", "tops", "stop"]
]
```

Bu nedenle:

```python
groups.values()
```

ile dictionary'nin değerlerini alıyoruz.

Sonucu liste olarak döndürmek için:

```python
return list(groups.values())
```

kullanıyoruz.

---

## Karmaşıklık

`n` kelime sayısını, `k` ise bir kelimenin ortalama uzunluğunu temsil etsin.

Her kelimeyi sıralamak:

```text
O(k log k)
```

zaman alır.

Bunu `n` kelime için yaptığımızdan:

```text
Time Complexity: O(n × k log k)
```

olur.

Sorting yaklaşımı oldukça anlaşılırdır. Ancak anagramları belirlemek için karakterleri gerçekten sıralamamız şart değildir.

Karakterlerin kaç kez tekrar ettiğini bilmemiz yeterlidir.

---

# 2. Yaklaşım — Frequency Array

Valid Anagram probleminde öğrendiğimiz **frequency counting** fikrini burada tekrar kullanabiliriz.

Problemde stringlerin yalnızca:

```text
a-z
```

arasındaki küçük İngilizce harflerden oluştuğu belirtiliyor.

Bu nedenle her kelime için 26 elemanlı bir sayaç oluşturabiliriz:

```python
count = [0] * 26
```

Listenin her indexi bir harfi temsil eder:

```text
index 0  → a
index 1  → b
index 2  → c
...
index 25 → z
```

---

## Bir Kelimenin Frekansını Oluşturmak

Örneğin:

```text
word = "act"
```

olsun.

Her karakter için:

```python
index = ord(char) - ord("a")
```

ile ilgili indexi buluyoruz.

Sonra:

```python
count[index] += 1
```

ile o karakterin sayısını artırıyoruz.

`"act"` için frequency array kabaca:

```text
a  b  c  d  ...  t  ...  z
↓  ↓  ↓          ↓

1  0  1  0  ...  1  ...  0
```

olur.

`"cat"` kelimesini saydığımızda karakterlerin geliş sırası farklı olsa bile aynı sonuç ortaya çıkar:

```text
act → [1, 0, 1, ..., 1, ...]
cat → [1, 0, 1, ..., 1, ...]
```

İşte bu frekans bilgisini kelimenin **anagram kimliği** olarak kullanabiliriz.

---

## Neden `tuple(count)` Kullanıyoruz?

Elimizde:

```python
count = [1, 0, 1, 0, ...]
```

şeklinde bir list bulunuyor.

Bunu doğrudan dictionary key'i olarak kullanamayız:

```python
groups[count]
```

çünkü Python'da `list` mutable, yani değiştirilebilir bir veri yapısıdır ve hashable değildir.

Dictionary key'lerinin ise hashable olması gerekir.

Bu nedenle listeyi tuple'a çeviriyoruz:

```python
key = tuple(count)
```

Artık:

```text
(1, 0, 1, 0, ...)
```

şeklindeki tuple dictionary key'i olarak kullanılabilir.

---

## Gruplama Nasıl Gerçekleşiyor?

Örneğin önce `"act"` geldiğinde:

```text
frequency(act)
      ↓
     key
      ↓
["act"]
```

oluşur.

Sonra `"cat"` geldiğinde aynı frequency key ortaya çıkar:

```text
frequency(cat)
      ↓
aynı key
      ↓
["act", "cat"]
```

Böylece Hash Map anagramları bizim için aynı grupta toplamış olur.

---

## Kod

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
```

---

## `count` Neden Her Kelimede Yeniden Oluşturuluyor?

Şu satır:

```python
count = [0] * 26
```

`for word in strs` döngüsünün içerisindedir.

Çünkü `count` sadece **o anda incelediğimiz kelimenin karakter frekansını** temsil etmelidir.

Örneğin:

```text
"act"
```

bittikten sonra `"cat"` için saymaya sıfırdan başlamalıyız.

Bu nedenle:

```text
word = "act"
count → sıfırdan oluştur
      → act'yi say

word = "cat"
count → tekrar sıfırdan oluştur
      → cat'i say
```

şeklinde ilerleriz.

Buna karşılık:

```python
groups = {}
```

döngünün dışında bulunur.

Çünkü `groups`, şimdiye kadar oluşturduğumuz **bütün anagram gruplarını** saklamalıdır.

Kısaca:

```text
count
→ mevcut kelimenin bilgisi
→ her kelimede sıfırlanır

groups
→ bütün kelimelerin grupları
→ algoritma boyunca korunur
```

---

## Karmaşıklık

Her kelimedeki her karakteri bir kez geziyoruz.

Bu nedenle:

```text
Time Complexity: O(n × k)
```

olur.

Burada:

```text
n → kelime sayısı
k → ortalama kelime uzunluğu
```

olarak düşünülebilir.

26 elemanlı frequency array'in boyutu input büyüklüğüne bağlı olarak değişmediği için her kelime için sabit büyüklükte bir sayaç kullanıyoruz.

Gruplarda ise sonuçta kelimeleri saklamamız gerektiğinden, çıktı için gereken alan inputla birlikte büyür.

---

# İki Yaklaşımın Karşılaştırılması

| Yaklaşım | Anagram Key | Zaman |
|---|---|---:|
| Sorting | Sıralanmış kelime | O(n × k log k) |
| Frequency Array | Karakter frekans tuple'ı | O(n × k) |

Sorting çözümü daha sezgisel ve okunması kolaydır.

Frequency Array çözümü ise problemde verilen `a-z` constraint'inden yararlanarak sorting işlemine ihtiyaç duymadan anagramları gruplamamızı sağlar.

---

# Bu Problemden Ne Öğrendim?

Bu problemde öğrendiğim en önemli fikirlerden biri, bir Hash Map kullanırken **doğru key'i tasarlamanın** çözümün merkezinde olabileceği.

Burada doğrudan kelimeyi key olarak kullanmak işimize yaramaz:

```text
"act" != "cat"
```

Ancak bu iki kelimenin ortak bir özelliğini key haline getirirsek:

```text
"act" ─┐
       ├─ aynı frequency signature
"cat" ─┘
```

Hash Map onları aynı grup altında toplayabilir.

Bu nedenle problemi şu şekilde düşünebiliriz:

```text
word
 ↓
anagramı temsil eden ortak bir özellik bul
 ↓
bu özelliği key yap
 ↓
aynı key'e sahip kelimeleri grupla
```

Bu, sadece anagram problemlerinde değil, elemanları ortak bir özelliğe göre gruplamamız gereken başka problemlerde de kullanılabilecek önemli bir pattern.

---

## Önceki Problemlerle Bağlantısı

Arrays & Hashing bölümünde Hash Map ve Hash Set'i farklı amaçlarla kullanmaya başladık:

```text
Two Sum
↓
value → index

Amaç:
İhtiyacım olan değeri daha önce gördüm mü?


Contains Duplicate
↓
seen values

Amaç:
Bu değer daha önce karşıma çıktı mı?


Valid Anagram
↓
character → frequency

Amaç:
Her karakter kaç kez tekrar ediyor?


Group Anagrams
↓
frequency signature → words

Amaç:
Aynı özelliğe sahip kelimeleri aynı grupta toplamak.
```

Özellikle **Valid Anagram → Group Anagrams** geçişi önemli.

Valid Anagram'da frequency counting kullanarak iki kelimeyi karşılaştırmıştık.

Group Anagrams'ta ise aynı bilgiyi bir adım ileri taşıyarak **Hash Map key'i** haline getirdik.

Bu problemden çıkardığım temel düşünce:

> Elemanları ortak bir özelliğe göre gruplamam gerekiyorsa, bu ortak özelliği temsil eden bir key oluşturup Hash Map kullanmayı düşünebilirim.