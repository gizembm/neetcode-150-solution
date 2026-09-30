# Arrays & Hashing

Bu bölümde array yapıları ve hashing kullanılarak çözülebilen problemler üzerinde çalışılmaktadır.

## Temel Kavramlar

### Array

Array, elemanların belirli bir sırada tutulduğu veri yapısıdır.

Python'da bu problemlerde çoğunlukla `list` kullanılır.

```python
nums = [3, 4, 5, 6]
```

Elemanlara indeks kullanarak erişilebilir:

```python
nums[0]  # 3
nums[2]  # 5
```

Index ile erişim:

```text
O(1)
```

zaman karmaşıklığına sahiptir.

---

## Hashing

Hashing, bir değeri hızlı bir şekilde saklamak ve daha sonra hızlı bir şekilde bulmak için kullanılan bir tekniktir.

Python'da NeetCode problemlerinde en sık karşılaşacağımız iki yapı:

```python
dict
set
```

olacaktır.

### Dictionary

Key-value ilişkisi saklar.

```python
seen = {
    8: 0,
    2: 1
}
```

Burada:

```text
key   → value
8     → 0
2     → 1
```

şeklinde bir ilişki vardır.

### Set

Sadece benzersiz değerleri saklamak istediğimiz durumlarda kullanılabilir.

```python
seen = {2, 5, 8}
```

Hash tabanlı `dict` ve `set` yapılarında lookup ve insertion işlemleri ortalama durumda `O(1)` zamanda gerçekleştirilebilir.

---

## Neden Hashing Kullanıyoruz?

Bazı problemlerde tekrar tekrar:

> Bu elemanı daha önce gördüm mü?

veya:

> Bu değer mevcut mu?

sorularını cevaplamamız gerekir.

Array içerisinde bunu tekrar tekrar aramak `O(n)` maliyet oluşturabilir.

Hash Map veya Hash Set kullanmak ise bu sorguları ortalama durumda `O(1)` seviyesine indirebilir.

---

# Problemler

| # | Problem | Temel Yaklaşımlar |
|---|---|---|
| 1 | Two Sum | Brute Force, Hash Map |

Bu tablo bölüm ilerledikçe güncellenecektir.