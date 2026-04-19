# Hiyerarşik Düşünme: Taksonomi ve Meronimi

Ontoloji tasarlarken en sık yapılan hata, "tür" ilişkisi ile "parça" ilişkisini birbirine karıştırmaktır. Bu iki yapı hiyerarşiktir ancak mantıkları tamamen farklıdır.

---

## 1. Taksonomi (IS-A İlişkisi)
Taksonomi, kavramları "tür" ve "alt tür" olarak sınıflandırır. Burada her alt eleman, üst elemanın bir örneği veya türüdür.
- **Mantık:** "X, bir Y'dir."
- **Özellik:** Kalıtım (Inheritance) söz konusudur. Üst sınıfın tüm özellikleri alt sınıfa geçer.
- **Örnekler:**
    - Kedi bir **Hayvan**dır.
    - Elma bir **Meyve**dir.
    - Profesör bir **Akademisyen**dir.

## 2. Meronimi (PART-OF İlişkisi)
Meronimi, bir bütünü oluşturan bileşenleri tanımlar. Burada alt eleman, üst elemanın bir parçasıdır ama onun bir türü değildir.
- **Mantık:** "X, Y'nin bir parçasıdır."
- **Özellik:** Bütün-parça ilişkisidir. Parça, bütünün türü olmak zorunda değildir.
- **Örnekler:**
    - Tekerlek bir **Araba**nın parçasıdır. (Tekerlek bir araba değildir!)
    - Ekran bir **Bilgisayar**ın parçasıdır.
    - Bölüm bir **Fakülte**nin parçasıdır.

---

## Karşılaştırmalı Tablo

| Özellik | Taksonomi | Meronimi |
| :--- | :--- | :--- |
| **Soru** | X, ne tür bir şeydir? | X, neyin parçasıdır? |
| **Mantıksal Bağ** | IS-A (X bir Y'dir) | PART-OF (X, Y'nin parçasıdır) |
| **Örnek** | Kanarya -> Kuş | Kanat -> Kuş |
| **Hata Riski** | "Tekerlek bir arabadır" demek. | "Kanat bir kuştur" demek. |

---

## Ontolojide Neden Önemli?
Bir bilgi sisteminde veriyi doğru hiyerarşiye yerleştirmek, otomatik çıkarım (reasoning) için hayati önem taşır. Eğer tekerleği arabanın bir alt türü (Taksonomi) olarak tanımlarsanız, sistem tüm tekerleklerin araba olduğunu varsayar ki bu mantıksal bir hatadır.
