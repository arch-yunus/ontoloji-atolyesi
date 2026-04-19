# OWL (Web Ontology Language) Rehberi

OWL, RDFS'in sunduğu yetenekleri genişleten ve çok daha karmaşık mantıksal kısıtlamalar eklememizi sağlayan, Semantik Web'in en güçlü dilidir.

---

## 1. Neden OWL?
RDFS ile sadece hiyerarşi kurabilirken (Hamsi bir Balıktır), OWL ile şunları yapabiliriz:
- "İki sınıf aynıdır" veya "farklıdır."
- "Bir özelliğin sadece bir tane değeri olabilir" (Functional Property).
- "Bir özelliğin tersi şudur" (Inverse Property).
- "Eğer A, B'nin içindeyse ve B, C'nin içindeyse A da C'nin içindedir" (Transitivite).

---

## 2. Temel Bileşenler

### Sınıflar (Classes)
- **`owl:Class`:** Kavram şablonu.
- **`owl:equivalentClass`:** İki sınıfın mantıksal olarak aynı olduğunu belirtir.

### Özellikler (Properties)
1. **Object Properties:** İki bireyi (Individual) birbirine bağlar (Örn: `Ahmet evlidir Ayşe`).
2. **Data Properties:** Bir bireyi bir veri değerine bağlar (Örn: `Ahmet yaşı 30`).

### Özellik Kısıtlamaları (Restrictions)
- **`owl:someValuesFrom`:** "En az bir tane" kısıtlaması.
- **`owl:allValuesFrom`:** "Sadece ve sadece" kısıtlaması.
- **`owl:hasValue`:** "Tam olarak şu değere sahip" kısıtlaması.

---

## 3. Mantıksal Çıkarım (Reasoning)
OWL'in en büyük gücü, bir **Reasoner** (Akıl Yürütücü) ile kullanıldığında ortaya çıkar. Siz her şeyi tek tek elle yazmazsınız; kuralları tanımlarsınız ve sistem yeni bilgileri kendi "çıkarır".

> **Örnek:**
> 1. Tanım: "Amca, babanın erkek kardeşidir."
> 2. Veri: "Ali, Veli'nin babasıdır. Can, Ali'nin erkek kardeşidir."
> 3. Çıkarım: "Can, Veli'nin amcasıdır."

---

## OWL Türleri (Kısaca)
1. **OWL Lite:** Basit kısıtlamalar.
2. **OWL DL:** Belirlenebilir mantık (Description Logic). En yaygın ve dengeli türdür.
3. **OWL Full:** Maksimum esneklik ama otomatik çıkarım yapılması zordur.
