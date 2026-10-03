# 49. Group Anagrams

## Problem

Bu problemde bize `strs` adında, birden fazla string içeren bir liste veriliyor.

Bizden **birbirinin anagramı olan kelimeleri aynı grup altında toplamamız** isteniyor.

İki kelime aynı karakterleri aynı sayıda içeriyorsa birbirinin anagramıdır. Karakterlerin hangi sırada bulunduğu önemli değildir.

Örneğin:

```text
"act" ve "cat"
```

kelimelerini inceleyelim.

Her ikisinde de:

```text
a → 1 kez
c → 1 kez
t → 1 kez
```

bulunur.

Karakterlerin sırası farklı olsa da karakterler ve tekrar sayıları aynı olduğu için bu iki kelime anagramdır ve aynı grupta bulunmalıdır.

---

## Örnek 1

```text
Input:
strs = ["act", "pots", "tops", "cat", "stop", "hat"]

Output:
[["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
```

Bu listedeki kelimeleri incelediğimizde üç farklı grup oluşur.

### 1. Grup

```text
"act"
"cat"
```

İki kelime de aynı karakterleri içerdiği için birbirinin anagramıdır.

```text
act → a, c, t
cat → c, a, t
```

Bu nedenle:

```text
["act", "cat"]
```

aynı grupta bulunur.

### 2. Grup

```text
"pots"
"tops"
"stop"
```

Bu kelimelerin tamamında:

```text
o → 1 kez
p → 1 kez
s → 1 kez
t → 1 kez
```

bulunur.

Dolayısıyla:

```text
["pots", "tops", "stop"]
```

aynı anagram grubunda yer alır.

### 3. Grup

```text
"hat"
```

`"hat"` ile anagram olan başka bir kelime olmadığı için tek başına bir grup oluşturur.

> Sonuçtaki grupların sırası önemli değildir.

---

## Örnek 2

```text
Input:
strs = ["x"]

Output:
[["x"]]
```

Listede yalnızca bir kelime bulunduğu için bu kelime kendi grubunu oluşturur.

---

## Örnek 3

```text
Input:
strs = [""]

Output:
[[""]]
```

Boş string de geçerli bir stringdir.

Listede yalnızca bir tane boş string bulunduğu için tek başına bir grup oluşturur.

---

## Dikkat Edilmesi Gereken Nokta

Sadece kelimelerin aynı karakterleri içerip içermediğine bakmak yeterli değildir.

Karakterlerin **tekrar sayılarının da aynı olması gerekir**.

Örneğin:

```text
"aab"
"abb"
```

iki kelimede de `a` ve `b` karakterleri vardır.

Ancak:

```text
        a       b

aab     2       1
abb     1       2
```

olduğu için bu kelimeler birbirinin anagramı değildir ve aynı gruba konulmamalıdır.

---

## Kısıtlar

```text
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
```

Her string yalnızca küçük İngilizce harflerden (`a-z`) oluşur.

Bir kelimenin boş string (`""`) olabileceğini de unutmamak gerekir.

---

## Kısaca Bizden İstenen

Bu problemi şu soruya indirgeyebiliriz:

> Hangi kelimeler aynı karakterleri aynı sayıda içeriyor?

Aynı karakter yapısına sahip kelimeleri bulup aynı listede toplamalıyız.

Örneğin:

```text
["eat", "tea", "car", "ate"]
```

için:

```text
eat ─┐
tea ─┼─ aynı karakterler → aynı grup
ate ─┘

car ─── farklı karakterler → farklı grup
```

dolayısıyla sonuç şu şekilde olabilir:

```text
[
    ["eat", "tea", "ate"],
    ["car"]
]
```