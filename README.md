# VIZUALIZACE GRAFŮ TRŽEBTržby - Analýza a Vizualizace
Tento projekt umožňuje vizualizaci a analýzu tržeb za různé roky pomocí knihovny Matplotlib v Pythonu.

Obsah
Instalace
Použití
Funkce
Příspěvky
Licence
Instalace
Pro správnou funkci projektu je nutné mít nainstalován Python a knihovnu Matplotlib. Nainstalujte závislosti pomocí následujícího příkazu:

bash
Zkopírovat kód
pip install matplotlib
Poté klonujte tento repozitář a přejděte do složky projektu:

bash
Zkopírovat kód
git clone https://github.com/uzivatel/projekt.git
cd projekt
Použití
Spusťte hlavní skript:

bash
Zkopírovat kód
python main.py
Po spuštění programu budete vyzváni k výběru jedné z následujících operací:

Zobrazit graf tržeb
Odstranit daný rok
Přidat rok do tržeb
Vypsat maximální a minimální hodnotu za určitý rok
Porovnat 2 roky mezi sebou
KONEC
Přehled funkcí
Zobrazení grafu tržeb
Vyberte rok, pro který chcete zobrazit graf. Program vykreslí graf tržeb za zvolený rok.

Odstranění daného roku
Vyberte rok, který chcete odstranit ze záznamů.

Přidání roku do tržeb
Přidejte nový rok a zadejte tržby pro každý měsíc.

Vypsání maximální a minimální hodnoty za určitý rok
Vyberte rok a program vypíše maximální a minimální hodnotu tržeb pro daný rok.

Porovnání 2 roky mezi sebou
Vyberte dva roky, které chcete porovnat. Program vykreslí grafy tržeb obou roků pro porovnání.

Ukázkový vstup a výstup
Ukázkový vstup pro přidání nového roku:

bash
Zkopírovat kód
Jaké jsou tvé tržby za měsíc Leden? 12000
Jaké jsou tvé tržby za měsíc Únor? 11500
...
Jaké jsou tvé tržby za měsíc Prosinec? 14000
Ukázkový výstup pro zobrazení grafu tržeb:


Funkce
graf(odpoved): Zobrazení grafu tržeb pro zvolený rok.
max_min(odpoved): Zobrazení maximální a minimální hodnoty tržeb pro zvolený rok.
hodnoty_list(): Vstup tržeb pro každý měsíc v roce.
porovnani(odpoved): Porovnání tržeb dvou roků 
