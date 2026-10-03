# NeetCode 150 — Türkçe Çözümler 🧠

Bu repository, **NeetCode 150 roadmap'ini takip ederek veri yapıları ve algoritmalar konusunda kendimi geliştirmek** için oluşturduğum çalışma alanı.

Buradaki amacım sadece soruları çözüp geçmek veya mümkün olduğunca hızlı şekilde 150 problemi tamamlamak değil. Her problemde kullanılan yaklaşımın **neden çalıştığını**, farklı çözümler arasındaki farkları ve bir problemi gördüğümde hangi veri yapısını veya algoritmayı neden düşünmem gerektiğini anlamaya çalışıyorum.

Öğrendiklerimi kalıcı hale getirmek için çözümlerimi ve çalışma notlarımı burada düzenli olarak paylaşacağım.

Aynı zamanda algoritma problemleri konusunda İngilizce çok fazla kaynak bulunmasına rağmen Türkçe açıklamalı kaynakların daha sınırlı olduğunu düşünüyorum. Bu nedenle notlarımı mümkün olduğunca **Türkçe, anlaşılır ve öğretici** bir şekilde hazırlamaya çalışıyorum.

---

## 🗺️ Nasıl İlerliyorum?

Problemleri **NeetCode 150 roadmap'indeki konu sırasına göre** çözüyorum.

Her konu ayrı bir klasör altında bulunuyor:

```text
01-arrays-and-hashing/
02-two-pointers/
03-sliding-window/
04-stack/
05-binary-search/
...
```

Problem klasörlerini ise LeetCode problem numaralarıyla isimlendiriyorum.

Örneğin:

```text
01-arrays-and-hashing/
│
├── README.md
│
└── 0001-two-sum/
    ├── README.md
    ├── brute_force.py
    └── hash_map.py
```

Bir problemin birden fazla anlamlı çözüm yöntemi varsa bunları ayrı ayrı incelemeye çalışıyorum.

Örneğin **Two Sum** için:

```text
Brute Force
O(n²)
   ↓
Hash Map
O(n)
```

Böylece yalnızca en iyi çözümü görmek yerine, **ilk yaklaşımdan daha verimli çözüme nasıl ulaşıldığını** da anlamaya çalışıyorum.

---

## 📚 Problem Notlarında Neler Var?

Her problem için hazırladığım `README.md` dosyasında mümkün olduğunca şu konulara yer veriyorum:

- Problemin sade bir açıklaması
- Problemi nasıl düşünmeye başlayabileceğimiz
- Farklı çözüm yaklaşımları
- Çözümlerin adım adım çalışma mantığı
- Python implementasyonları
- Time Complexity
- Space Complexity
- Yaklaşımlar arasındaki farklar
- Problemden çıkarılabilecek temel algoritmik pattern

Buradaki temel düşüncem şu:

> Bir çözümün kodunu hatırlamaktan daha önemli olan şey, o çözüme neden ihtiyaç duyduğumuzu anlayabilmek.

---

## 🧩 Konular

NeetCode 150 boyunca çalışacağım ana konular:

- Arrays & Hashing
- Two Pointers
- Sliding Window
- Stack
- Binary Search
- Linked List
- Trees
- Tries
- Heap / Priority Queue
- Backtracking
- Graphs
- Advanced Graphs
- 1-D Dynamic Programming
- 2-D Dynamic Programming
- Greedy
- Intervals
- Math & Geometry
- Bit Manipulation

Her bölüm ilerledikçe ilgili klasör ve çalışma notları da repository'ye eklenecek.

---

## 🐍 Dil

Çözümleri ağırlıklı olarak **Python** ile yazıyorum.

Python'ın sade sözdizimi sayesinde algoritma problemlerinde dil detaylarından çok problem çözme mantığına ve kullanılan veri yapılarına odaklanmayı hedefliyorum.

---

## 🔍 Kodları Adım Adım İncelemek

Algoritmaların nasıl çalıştığını anlamanın en iyi yollarından biri, kodun her iterasyonda nasıl ilerlediğini gözlemlemek.

Bu repository'deki Python çözümlerini adım adım incelemek için **Python Tutor** kullanılabilir.

Python Tutor sayesinde:

- Değişkenlerin her adımda aldığı değerleri,
- `list`, `set` ve `dict` gibi veri yapılarının nasıl değiştiğini,
- Döngülerin her iterasyonunu,
- Fonksiyonların çalışma sırasını

görsel olarak takip edebilirsiniz.

👉 [Python Tutor ile kodu görselleştir](https://pythontutor.com/visualize.html#mode=edit)

Özellikle yeni bir algoritma veya veri yapısını öğrenirken kodu sadece okumak yerine adım adım çalıştırmak, çözümün mantığını anlamayı oldukça kolaylaştırıyor.


## 📈 İlerleme

**Tamamlanan problem: 1 / 150**

### Arrays & Hashing

- [x] 0001 — Two Sum
- [x] 0217 — Contains Duplicate
- [x] 0242 — Valid Anagram
- [x] 0049 — Group Anagrams
- [ ] 0347 — Top K Frequent Elements
- [ ] Encode and Decode Strings
- [ ] 0238 — Product of Array Except Self
- [ ] 0036 — Valid Sudoku
- [ ] 0128 — Longest Consecutive Sequence

---

## 🌱 Bu Repository'nin Amacı

Bu repo benim için aynı anda hem bir **çalışma günlüğü**, hem bir **algoritma not defteri**, hem de zaman içinde gelişimimi görebileceğim bir arşiv.

150 problemin sonunda yalnızca:

> “150 LeetCode problemi çözdüm.”

diyebilmek yerine;

> “Bir problem gördüğümde hangi veri yapısını veya algoritmik pattern'i düşünmem gerektiğini daha iyi anlayabiliyorum.”

noktasına ulaşmak istiyorum.

Repository de ben öğrendikçe ve yeni problemler çözdükçe gelişmeye devam edecek. 🚀
