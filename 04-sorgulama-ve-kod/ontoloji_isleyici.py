import os
import sys
import logging
from typing import Optional, List
from rdflib import Graph, Namespace, RDF, OWL
from rdflib.query import ResultRow

# Windows terminal encoding fix
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Logging Yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ontoloji dosyalarının yolları
PROJE_DIZINI: str = os.path.dirname(os.path.abspath(__file__))
MIZAN_DIZINI: str = os.path.join(os.path.dirname(PROJE_DIZINI), "03-modelleme-projeleri")

AILE_OWL: str = os.path.join(MIZAN_DIZINI, "aile-agaci.owl")
ETICARET_OWL: str = os.path.join(MIZAN_DIZINI, "e-ticaret.owl")

class OntolojiAraci:
    """Ontoloji dosyalarını işlemek ve sorgulamak için geliştirilmiş araç sınıfı."""

    def __init__(self, dosya_yolu: str):
        self.dosya_yolu = dosya_yolu
        self.g = Graph()
        self._yukle()

    def _yukle(self) -> None:
        """Dosyayı yükler ve grafı oluşturur."""
        if not os.path.exists(self.dosya_yolu):
            logger.error(f"Dosya bulunamadı: {self.dosya_yolu}")
            raise FileNotFoundError(self.dosya_yolu)
        
        try:
            self.g.parse(self.dosya_yolu, format="xml")
            logger.info(f"Ontoloji başarıyla yüklendi: {os.path.basename(self.dosya_yolu)}")
        except Exception as e:
            logger.error(f"Yükleme hatası: {str(e)}")
            raise

    def ozet_cikar(self) -> None:
        """Ontoloji yapısının temel bir özetini konsola yazdırır."""
        print(f"\n--- {os.path.basename(self.dosya_yolu)} Özet Analizi ---")
        print(f"🔹 Toplam Üçlü (Triple) Sayısı: {len(self.g)}")
        
        # Sınıfları Listele
        siniflar = list(self.g.subjects(RDF.type, OWL.Class))
        print(f"🔹 Sınıf Sayısı: {len(siniflar)}")
        for i, s in enumerate(siniflar[:5]): # İlk 5'ini göster
             print(f"   {i+1}. {s}")
        if len(siniflar) > 5: print("   ...")
            
        # Bireyleri Listele
        bireyler = list(self.g.subjects(RDF.type, OWL.NamedIndividual))
        print(f"🔹 Birey Sayısı: {len(bireyler)}")
        for i, b in enumerate(bireyler[:5]):
             print(f"   {i+1}. {b}")
        if len(bireyler) > 5: print("   ...")

    def sparql_calistir(self, sorgu: str) -> List[ResultRow]:
        """SPARQL sorgusu çalıştırır ve sonuçları döner."""
        logger.info("SPARQL sorgusu çalıştırılıyor...")
        try:
            results = self.g.query(sorgu)
            return list(results)
        except Exception as e:
            logger.error(f"Sorgu hatası: {str(e)}")
            return []

if __name__ == "__main__":
    # Örnek Kullanım
    try:
        # Aile Ontolojisi Analizi
        aile_analiz = OntolojiAraci(AILE_OWL)
        aile_analiz.ozet_cikar()
        
        # SPARQL Sorgusu
        sorgu = """
        PREFIX aile: <http://www.example.org/ontologies/aile-agaci#>
        SELECT ?ebeveyn ?cocuk
        WHERE {
            ?ebeveyn aile:ebeveynidir ?cocuk .
        }
        """
        sonuclar = aile_analiz.sparql_calistir(sorgu)
        print(f"\n✅ Sorgu Sonuçları ({len(sonuclar)} eşleşme):")
        for row in sonuclar:
            print(f"   - {row.ebeveyn} -> {row.cocuk}")

    except Exception as e:
        logger.critical(f"Uygulama hatası: {str(e)}")
