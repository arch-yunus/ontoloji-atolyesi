# RDF ve RDFS'e Giriş

Semantik Web'in temelini oluşturan bu iki standart, verinin birbiriyle ilişkilendirilmesini ve anlamlandırılmasını sağlar.

---

## 1. RDF (Resource Description Framework)
RDF, veriyi bir "nesne" ve o nesnenin "özellikleri" arasındaki ilişki olarak tanımlayan standarttır.

### Üçlü Yapı (Triple)
Her bilgi bir **Triple (Üçlü)** olarak ifade edilir:
1. **Subject (Özne):** Tanımlanan kaynak (Örn: `Ahmet`).
2. **Predicate (Yüklem):** Öznenin bir özelliği veya ilişkisi (Örn: `arkadaşıdır`).
3. **Object (Nesne):** Özelliğin değeri veya ilişkinin hedefi (Örn: `Mehmet`).

> **Örnek:** `Ahmet` (Subject) -> `yaşı` (Predicate) -> `25` (Object).

---

## 2. RDFS (RDF Schema)
RDF veriyi tanımlarken, RDFS bu verilerin hiyerarşisini ve sınıflarını tanımlar. RDFS, temel bir "sınıflandırma dili"dir.

### Temel Kavramlar:
- **`rdfs:Class`:** Bir sınıf tanımlar (Örn: "İnsan").
- **`rdfs:subClassOf`:** Bir sınıfın başka bir sınıfın alt sınıfı olduğunu belirtir.
- **`rdf:Property`:** Bir özellik tanımlar (Örn: "ad").
- **`rdfs:domain`:** Özelliğin hangi sınıflara uygulanabileceğini belirler.
- **`rdfs:range`:** Özelliğin alabileceği değer türünü belirler.

---

## RDF Neden Önemli?
Geleneksel veritabanlarının (SQL) aksine RDF, **esnektir**. Şemayı önceden tanımlamak zorunda değilsinizdir; yeni ilişkiler eklemek için sadece yeni üçlüler yazmanız yeterlidir. Bu da "Açık Dünya Varsayımı" (Open World Assumption) için temel oluşturur.
