import os
import sys
import logging
from typing import Optional, List
from rdflib import Graph, Namespace, RDF, OWL
from rdflib.query import ResultRow
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

# Windows terminal encoding fix
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

console = Console()

# Logging Yapılandırması (Hidden for cleaner TUI)
logging.basicConfig(level=logging.CRITICAL)

# Ontoloji dosyalarının yolları
PROJE_DIZINI: str = os.path.dirname(os.path.abspath(__file__))
MIZAN_DIZINI: str = os.path.join(os.path.dirname(PROJE_DIZINI), "03-modelleme-projeleri")

AILE_OWL: str = os.path.join(MIZAN_DIZINI, "aile-agaci.owl")
ETICARET_OWL: str = os.path.join(MIZAN_DIZINI, "e-ticaret.owl")

class MetaOntolojiZehni:
    """Varlığın dijital izdüşümlerini (ontolojileri) işleyen üst-akıl aracı."""

    def __init__(self, dosya_yolu: str):
        self.dosya_yolu = dosya_yolu
        self.g = Graph()
        self._tezahur_ettir()

    def _tezahur_ettir(self) -> None:
        """Dosyayı sisteme dahil eder ve ontolojik grafı oluşturur."""
        if not os.path.exists(self.dosya_yolu):
            console.print(f"[bold red]Hata:[/bold red] Varlık dosyası bulunamadı: {self.dosya_yolu}")
            raise FileNotFoundError(self.dosya_yolu)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description=f"Ontoloji yükleniyor: {os.path.basename(self.dosya_yolu)}...", total=None)
            try:
                self.g.parse(self.dosya_yolu, format="xml")
            except Exception as e:
                console.print(f"[bold red]Yükleme hatası:[/bold red] {str(e)}")
                raise

    def hakikat_ozeti(self) -> None:
        """Ontolojinin özünü (summary) görsel bir tablo ile sunar."""
        
        table = Table(title=f"📜 {os.path.basename(self.dosya_yolu)} Analiz Raporu", show_header=True, header_style="bold magenta")
        table.add_column("Metrik", style="cyan")
        table.add_column("Değer", style="green")

        table.add_row("Toplam Üçlü (Triple)", str(len(self.g)))
        
        siniflar = list(self.g.subjects(RDF.type, OWL.Class))
        table.add_row("Sınıf Sayısı", str(len(siniflar)))
            
        bireyler = list(self.g.subjects(RDF.type, OWL.NamedIndividual))
        table.add_row("Birey Sayısı", str(len(bireyler)))

        console.print(Panel(table, expand=False, border_style="bright_blue"))

        if siniflar:
            console.print("\n[bold yellow]🔹 Öne Çıkan Sınıflar:[/bold yellow]")
            for i, s in enumerate(siniflar[:5]):
                 console.print(f"  {i+1}. [italic]{s}[/italic]")
        
        if bireyler:
            console.print("\n[bold yellow]🔹 Öne Çıkan Bireyler:[/bold yellow]")
            for i, b in enumerate(bireyler[:5]):
                 console.print(f"  {i+1}. [italic]{b}[/italic]")

    def derin_sorgu(self, sorgu: str) -> List[ResultRow]:
        """SPARQL ile varlığın derinliklerine iner."""
        console.print("\n[bold cyan]🔍 Hakikat aranıyor (SPARQL)...[/bold cyan]")
        try:
            results = self.g.query(sorgu)
            return list(results)
        except Exception as e:
            console.print(f"[bold red]Sorgu hatası:[/bold red] {str(e)}")
            return []

if __name__ == "__main__":
    console.print(Panel.fit("🌌 [bold white]META-ONTOLOJİ İŞLEYİCİ[/bold white] 🌌\n[dim]Varlığın Dijital Temsili Üzerine Bir Araştırma[/dim]", border_style="purple"))
    
    try:
        # Aile Ontolojisi Analizi
        if os.path.exists(AILE_OWL):
            akil = MetaOntolojiZehni(AILE_OWL)
            akil.hakikat_ozeti()
            
            # SPARQL Sorgusu
            sorgu = """
            PREFIX aile: <http://www.example.org/ontologies/aile-agaci#>
            SELECT ?ebeveyn ?cocuk
            WHERE {
                ?ebeveyn aile:ebeveynidir ?cocuk .
            }
            """
            sonuclar = akil.derin_sorgu(sorgu)
            
            if sonuclar:
                res_table = Table(title="✅ Sorgu Sonuçları", show_header=True, header_style="bold green")
                res_table.add_column("Ebeveyn", style="blue")
                res_table.add_column("Çocuk", style="yellow")
                
                for row in sonuclar:
                    res_table.add_row(str(row.ebeveyn).split('#')[-1], str(row.cocuk).split('#')[-1])
                
                console.print(res_table)
            else:
                console.print("[yellow]Sonuç bulunamadı.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Kritik Hata:[/bold red] {str(e)}")
        sys.exit(1)
