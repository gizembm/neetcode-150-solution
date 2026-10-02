
# 217. Contains Duplicate

## Problem

Bu problemde bize `nums` adında bir tam sayı listesi veriliyor.

Bizden, listede **aynı değerin birden fazla kez bulunup bulunmadığını** kontrol etmemiz isteniyor.

Eğer herhangi bir değer en az iki kez bulunuyorsa:

```python
True
```

hiçbir değer tekrar etmiyorsa:

```python
False
```

döndürmeliyiz.

---

## Örnek 1

```text
Input:
nums = [1, 2, 3, 3]

Output:
True
```

Listede `3` değeri iki kez bulunmaktadır:

```text
[1, 2, 3, 3]
       ↑  ↑
```

Bu nedenle sonuç:

```python
True
```

olur.

---

## Örnek 2

```text
Input:
nums = [1, 2, 3, 4]

Output:
False
```

Listedeki bütün değerler birbirinden farklıdır.

```text
1 → 1 kez
2 → 1 kez
3 → 1 kez
4 → 1 kez
```

Tekrar eden herhangi bir değer olmadığı için sonuç:

```python
False
```

olur.

---

## Birkaç Farklı Durum

### Aynı değerin birden fazla kez tekrar etmesi

```text
nums = [5, 5, 5]
```

Bir değerin iki kez değil, üç veya daha fazla kez bulunması da duplicate olduğu anlamına gelir.

Sonuç:

```python
True
```

---

### Tek elemanlı liste

```text
nums = [7]
```

Bir değerin tekrar edebilmesi için en az iki elemanın bulunması gerekir.

Bu nedenle sonuç:

```python
False
```

olur.

---

### Boş liste

```text
nums = []
```

Listede hiçbir eleman bulunmadığı için tekrar eden bir değer de bulunamaz.

Sonuç:

```python
False
```

olur.

---

## Dikkat Edilmesi Gereken Nokta

Bizden:

> Hangi değer tekrar ediyor?

veya:

> Kaç kez tekrar ediyor?

bilgisi istenmiyor.

Sadece:

> En az bir duplicate var mı?

sorusuna cevap vermemiz gerekiyor.

Örneğin:

```text
nums = [7, 4, 9, 2, 4]
```

için `4` değerinin tekrar ettiğini fark ettiğimiz anda cevabın `True` olduğunu biliyoruz.

Listenin geri kalanını incelememiz gerekmez.

---

## Kısıtlar

```text
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```

Listenin uzunluğu `100.000` elemana kadar çıkabilir.

Bu nedenle küçük inputlarda çalışan bir çözümün büyük inputlarda ne kadar verimli olacağını da düşünmemiz gerekir.

---

## Kısaca Bizden İstenen

Bu problemi şu soruya indirgeyebiliriz:

> Liste içerisinde daha önce gördüğümüz bir değer tekrar karşımıza çıkıyor mu?

Örneğin:

```text
nums = [7, 4, 9, 2, 4]
```

için:

```text
7 → ilk kez görüldü
4 → ilk kez görüldü
9 → ilk kez görüldü
2 → ilk kez görüldü
4 → daha önce görülmüştü
```

Bu nedenle sonuç:

```python
True
```

olmalıdır.