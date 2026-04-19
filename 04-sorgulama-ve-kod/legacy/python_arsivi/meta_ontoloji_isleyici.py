import os
import sys
import logging
import random
from typing import Optional, List, Dict
from rdflib import Graph, Namespace, RDF, OWL
from rdflib.query import ResultRow
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.align import Align

# Windows terminal encoding fix
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

console = Console()

# Exotic Mode Flag
EGZOTIK_MOD: bool = "--egzotik" in sys.argv


# Logging Yapılandırması
logging.basicConfig(level=logging.CRITICAL)

# Ontoloji dosyalarının yolları
PROJE_DIZINI: str = os.path.dirname(os.path.abspath(__file__))
MIZAN_DIZINI: str = os.path.join(os.path.dirname(PROJE_DIZINI), "03-modelleme-projeleri")

AILE_OWL: str = os.path.join(MIZAN_DIZINI, "aile-agaci.owl")
ETICARET_OWL: str = os.path.join(MIZAN_DIZINI, "e-ticaret.owl")
EGZOTIK_DIZIN: str = os.path.join(PROJE_DIZINI, "egzotik")


class NoesOntologike:
    """Varlığın (On) dijital izdüşümlerini işleyen üst-akıl (Noes) aracı."""

    def __init__(self, dosya_yolu: str):
        self.dosya_yolu = dosya_yolu
        self.g = Graph()
        self._tezahur_ettir()

    def _ekstasis_ettir(self) -> None:
        """Kodu sisteme dahil eder ve ontolojik grafı (Graph) oluşturur."""
        if not os.path.exists(self.dosya_yolu):
            console.print(f"[bold red]Hata:[/bold red] Varlık dosyası bulunamadı: {self.dosya_yolu}")
            raise FileNotFoundError(self.dosya_yolu)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description=f"🌌 Ontologikos Plain yükleniyor: {os.path.basename(self.dosya_yolu)}...", total=None)
            try:
                self.g.parse(self.dosya_yolu, format="xml")
            except Exception as e:
                console.print(f"[bold red]Tezahür hatası:[/bold red] {str(e)}")
                raise

    def alitheia_synopsis(self) -> Panel:
        """Ontolojinin özünü (Alitheia) görsel bir tablo ile sunar."""
        
        table = Table(show_header=True, header_style="bold cyan", box=None)
        table.add_column("Metrikon", style="dim")
        table.add_column("Monas", style="bold green")

        table.add_row("TripleCount", str(len(self.g)))
        
        classes = list(self.g.subjects(RDF.type, OWL.Class))
        table.add_row("Classis", str(len(classes)))
            
        individuals = list(self.g.subjects(RDF.type, OWL.NamedIndividual))
        table.add_row("Individuum", str(len(individuals)))

        return Panel(table, title=f"📜 {os.path.basename(self.dosya_yolu)} Synopsis", border_style="bright_blue")

    def sophia_poiesis(self) -> Panel:
        """Ontolojik veriden rastgele felsefi çıkarımlar (Sophia) üretir."""
        classes = [str(s).split('#')[-1] for s in self.g.subjects(RDF.type, OWL.Class) if '#' in str(s)]
        if not classes:
             classes = ["On", "Logos", "Ousia"]
        
        paradigms = [
            "İncelediğimiz [bold yellow]{0}[/bold yellow] kavramı, Logos'un temel direğidir.",
            "Eğer [bold yellow]{0}[/bold yellow] olmasaydı, ontolojik bütünlük (Hen) bozulurdu.",
            "Sistemdeki [bold yellow]{0}[/bold yellow] varlığı (On), hiyerarşinin üst basamaklarını işaret eder.",
            "Dijital evrende [bold yellow]{0}[/bold yellow], Ousia'nın bir yansımasıdır.",
            "[bold yellow]{0}[/bold yellow] ve diğer symbebekoslar, varlığın tezahür biçimleridir."
        ]
        
        insight = random.choice(paradigms).format(random.choice(classes))
        return Panel(Align.center(insight), title="🧠 Ontologikos Sophia", border_style="magenta")

    def bathys_ereuna(self, query: str) -> List[ResultRow]:
        """SPARQL ile varlığın (On) derinliklerine iner."""
        try:
            results = self.g.query(query)
            return list(results)
        except Exception as e:
            console.print(f"[bold red]Sorgu hatası:[/bold red] {str(e)}")
            return []

    def egzotik_laboratuvar_ozeti(self) -> None:
        """Egzotik dillerdeki ontolojik deneyleri listeler."""
        if not os.path.exists(EGZOTIK_DIZIN):
            return

        table = Table(title="🧪 Egzotik Ontoloji Laboratuvarı", show_header=True, header_style="bold yellow")
        table.add_column("Dil / Uzantı", style="magenta")
        table.add_column("Dosya Adı", style="cyan")

        dosyalar = [f for f in os.listdir(EGZOTIK_DIZIN) if os.path.isfile(os.path.join(EGZOTIK_DIZIN, f)) and f != "README.md"]
        for dosya in sorted(dosyalar):
             uzanti = dosya.split('.')[-1].upper()
             table.add_row(uzanti, dosya)

        console.print(Panel(table, title="[bold red]KRİTİK VERİ[/bold red]", subtitle="Alternatif Gerçeklikler", border_style="red"))


def protos():
    console.clear()
    console.print(Panel.fit("🌌 [bold white]NOES-ONTOLOGIKE ISLEYICI v1.0 [ARCHIVE][/bold white] 🌌\n[dim]On, Logos ve Alitheia Üzerine Bir Algoritmikos Kinema[/dim]", border_style="purple"))
    
    try:
        # Aile Ontolojisi Analizi
        if os.path.exists(AILE_OWL):
            mind = NoesOntologike(AILE_OWL)
            
            # TUI Layout
            layout = Layout()
            layout.split_column(
                Layout(name="upper"),
                Layout(name="lower")
            )
            layout["upper"].split_row(
                Layout(name="synopsis"),
                Layout(name="sophia")
            )
            
            layout["synopsis"].update(mind.alitheia_synopsis())
            layout["sophia"].update(mind.sophia_poiesis())
            
            console.print(layout)
            
            # SPARQL Sorgusu
            query = """
            PREFIX aile: <http://www.example.org/ontologies/aile-agaci#>
            SELECT ?ebeveyn ?cocuk
            WHERE {
                ?ebeveyn aile:ebeveynidir ?cocuk .
            }
            """
            results = mind.bathys_ereuna(query)
            
            if results:
                res_table = Table(title="🔍 Alitheia Ereuna: Ebeveyn-Çocuk İlişkileri", show_header=True, header_style="bold green")
                res_table.add_column("Ebeveyn", style="blue")
                res_table.add_column("Çocuk", style="yellow")
                
                for row in results[:10]: # Limit for display
                    res_table.add_row(str(row.ebeveyn).split('#')[-1], str(row.cocuk).split('#')[-1])
                
                console.print(res_table)
            else:
                console.print("[yellow]⚠️ Bu ontolojik katmanda henüz veri bulunamadı.[/yellow]")

            if EGZOTIK_MOD:
                mind.exotikos_ergasterion_synopsis()


    except Exception as e:
        console.print(f"[bold red]Kritikon Hata:[/bold red] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    protos()
