# 242. Valid Anagram

## Problem

Bu problemde bize `s` ve `t` olmak üzere iki string veriliyor. Bizden bu iki stringin birbirinin **anagramı** olup olmadığını kontrol etmemiz isteniyor.

İki kelime, **aynı karakterleri aynı sayıda içeriyorsa** birbirinin anagramıdır. Karakterlerin hangi sırada bulunduğu önemli değildir.

Örneğin:

```text
s = "racecar"
t = "carrace"
```

İki kelimedeki harflerin sırası farklı olsa da içerdikleri karakterler ve bu karakterlerin tekrar sayıları aynıdır:

```text
a → 1 kez
c → 2 kez
e → 1 kez
r → 2 kez
```

Bu nedenle sonuç `True` olur.

---

## Örnek 1

```text
Input:
s = "racecar"
t = "carrace"

Output:
True
```

İki string de aynı karakterleri aynı sayıda içerdiği için birbirinin anagramıdır.

---

## Örnek 2

```text
Input:
s = "jar"
t = "jam"

Output:
False
```

Her iki kelimede de `j` ve `a` bulunuyor. Ancak ilk kelimede `r`, ikinci kelimede ise `m` bulunuyor.

Karakterler aynı olmadığı için bu iki string anagram değildir.

---

## Örnek 3

```text
Input:
s = "x"
t = "x"

Output:
True
```

İki string de yalnızca bir tane `x` karakteri içerdiği için sonuç `True` olur.

---

## Dikkat Edilmesi Gereken Nokta

Anagram kontrolünde sadece **hangi karakterlerin bulunduğuna** bakmak yeterli değildir. Her karakterin **kaç kez bulunduğu** da aynı olmalıdır.

Örneğin:

```text
s = "aab"
t = "abb"
```

İki string de `a` ve `b` karakterlerini içeriyor. Fakat karakter sayıları farklı:

```text
        s       t

a       2       1
b       1       2
```

Bu nedenle bu iki string anagram değildir.

---

## Kısıtlar

```text
1 <= s.length, t.length <= 5 * 10^4
```

`s` ve `t` yalnızca küçük İngilizce harflerden (`a-z`) oluşur.

---

## Kısaca Bizden İstenen

Bu problemi şu soruya indirgeyebiliriz:

> `s` ve `t` içerisindeki her karakter aynı sayıda mı bulunuyor?

Eğer cevap evetse `True`, değilse `False` döndürmeliyiz.