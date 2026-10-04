# 347. Top K Frequent Elements

Bir tam sayı dizisi `nums` ve bir tam sayı `k` veriliyor.

Amaç, dizi içerisinde **en sık tekrar eden `k` farklı elemanı** bulup döndürmektir.

Sonuç herhangi bir sırada döndürülebilir.

Test durumları, cevabın her zaman benzersiz olacağı şekilde oluşturulmuştur.

---

## Örnek 1

**Input:**

```text
nums = [1, 2, 2, 3, 3, 3]
k = 2
```

Dizideki sayıların tekrar sayılarına baktığımızda:

```text
1 → 1 kez
2 → 2 kez
3 → 3 kez
```

`3` en sık tekrar eden elemandır.

`2` ise ikinci en sık tekrar eden elemandır.

`k = 2` olduğu için en sık tekrar eden iki farklı elemanı döndürmemiz gerekir.

**Output:**

```text
[2, 3]
```

Sonuç herhangi bir sırada döndürülebileceği için:

```text
[3, 2]
```

de geçerli bir cevaptır.

---

## Örnek 2

**Input:**

```text
nums = [7, 7]
k = 1
```

Dizide yalnızca `7` değeri bulunmaktadır ve iki kez tekrar etmektedir.

En sık tekrar eden `1` eleman istendiği için:

**Output:**

```text
[7]
```

---

## Elemanın Değeri Değil, Frekansı Önemlidir

Bu problemde sayıların büyüklüklerini karşılaştırmıyoruz.

Örneğin:

```text
nums = [100, 100, 5, 5, 5, 1]
k = 1
```

Frekanslar:

```text
100 → 2 kez
5   → 3 kez
1   → 1 kez
```

şeklindedir.

Dizideki en büyük sayı `100` olmasına rağmen en sık tekrar eden sayı `5` olduğu için cevap:

```text
[5]
```

olur.

Yani problem:

> En büyük `k` sayıyı bulmamızı değil, frekansı en yüksek `k` sayıyı bulmamızı istiyor.

---

## Önemli Noktalar

- Her farklı elemanın dizide kaç kez geçtiği önemlidir.
- Sonuç içerisinde `k` farklı eleman bulunmalıdır.
- Elemanların sayısal büyüklüğü önemli değildir.
- Sonuç herhangi bir sırada döndürülebilir.
- Aynı eleman sonuç içerisinde birden fazla kez bulunmaz.
- `k`, dizide bulunan farklı elemanların sayısından büyük olmayacaktır.
- Test durumları cevabın benzersiz olacağı şekilde oluşturulmuştur.

---

## Constraints

```text
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums
```

---

## Kısaca Bizden İstenen

Öncelikle dizideki farklı sayıların kaç kez tekrar ettiğini düşünmemiz gerekiyor.

Daha sonra bu frekanslara bakarak:

> **Dizi içerisinde en sık tekrar eden `k` farklı eleman hangileri?**

sorusunu cevaplamamız gerekiyor.