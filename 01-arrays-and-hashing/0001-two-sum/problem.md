# 1. Two Sum

## Problem

Bu problemde bize `nums` adında bir tam sayı listesi ve `target` adında bir hedef değer veriliyor.

Bizden, listedeki **iki farklı sayının toplamı `target` değerine eşit olacak şekilde bu sayıların indexlerini bulmamız** isteniyor.

Aynı elemanı iki kez kullanamayız. Yani seçtiğimiz iki sayının indexleri birbirinden farklı olmalıdır.

Her input için yalnızca bir geçerli çözüm olduğu kabul edilebilir.

---

## Örnek 1

```text
Input:
nums = [3, 4, 5, 6]
target = 7

Output:
[0, 1]
```

Çünkü:

```text
nums[0] = 3
nums[1] = 4

3 + 4 = 7
```

Bu nedenle döndürmemiz gereken indexler:

```text
[0, 1]
```

olur.

---

## Örnek 2

```text
Input:
nums = [4, 5, 6]
target = 10

Output:
[0, 2]
```

Çünkü:

```text
nums[0] = 4
nums[2] = 6

4 + 6 = 10
```

---

## Örnek 3

```text
Input:
nums = [5, 5]
target = 10

Output:
[0, 1]
```

Burada iki sayının değerleri aynı olsa da indexleri farklıdır:

```text
nums[0] = 5
nums[1] = 5
```

Dolayısıyla:

```text
5 + 5 = 10
```

olduğu için `[0, 1]` geçerli bir cevaptır.

---

## Dikkat Edilmesi Gereken Nokta

Aynı elemanı iki kez kullanamayız.

Örneğin:

```text
nums = [3, 4]
target = 6
```

İlk eleman `3` olsa bile:

```text
3 + 3 = 6
```

diyerek aynı indexi iki kez kullanamayız.

Yani:

```text
[0, 0]
```

geçerli bir cevap değildir.

Aradığımız iki sayı **farklı indexlerde** bulunmalıdır.

---

## Kısaca Bizden İstenen

Bu problemi şu soruya indirgeyebiliriz:

> `nums` içerisinde toplamları `target` değerini veren iki farklı eleman var mı ve bunların indexleri nedir?

Örneğin:

```text
nums = [8, 2, 11, 7, 15]
target = 9
```

Burada:

```text
2 + 7 = 9
```

ve bu sayıların indexleri:

```text
1 ve 3
```

olduğu için cevap:

```text
[1, 3]
```

olmalıdır.