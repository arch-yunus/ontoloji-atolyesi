import os
from rdflib import Graph, Namespace, RDF, OWL

# Ontoloji dosyalarının yolları
PROJE_DIZINI = os.path.dirname(os.path.abspath(__file__))
MIZAN_DIZINI = os.path.join(os.path.dirname(PROJE_DIZINI), "03-modelleme-projeleri")

AILE_OWL = os.path.join(MIZAN_DIZINI, "aile-agaci.owl")
ETICARET_OWL = os.path.join(MIZAN_DIZINI, "e-ticaret.owl")

def ontoloji_ozeti(dosya_yolu):
    """Ontoloji dosyasını yükler ve temel bir özet çıkarır."""
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı.")
        return

    g = Graph()
    g.parse(dosya_yolu, format="xml")
    
    print(f"\n--- {os.path.basename(dosya_yolu)} Özet Bilgileri ---")
    print(f"Toplam Üçlü (Triple) Sayısı: {len(g)}")
    
    # Sınıfları Listele
    print("\nSınıflar (Classes):")
    for s in g.subjects(RDF.type, OWL.Class):
        print(f" - {s}")
        
    # Bireyleri Listele
    print("\nBireyler (Individuals):")
    for s in g.subjects(RDF.type, OWL.NamedIndividual):
        print(f" - {s}")

def sparql_sorgusu_calistir(dosya_yolu, sorgu):
    """Belirli bir ontoloji üzerinde SPARQL sorgusu çalıştırır."""
    g = Graph()
    g.parse(dosya_yolu, format="xml")
    
    results = g.query(sorgu)
    print(f"\nSorgu Sonuçları ({os.path.basename(dosya_yolu)}):")
    for row in results:
        print(row)

if __name__ == "__main__":
    # 1. Özetleri Göster
    ontoloji_ozeti(AILE_OWL)
    ontoloji_ozeti(ETICARET_OWL)
    
    # 2. Örnek SPARQL Sorgusu
    aile_sorgusu = """
    PREFIX aile: <http://www.example.org/ontologies/aile-agaci#>
    SELECT ?ebeveyn ?cocuk
    WHERE {
      ?ebeveyn aile:ebeveynidir ?cocuk .
    }
    """
    sparql_sorgusu_calistir(AILE_OWL, aile_sorgusu)
