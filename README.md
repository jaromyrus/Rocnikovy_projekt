# Tržby - Analýza a Vizualizace

Tento projekt umožňuje vizualizaci a analýzu tržeb za různé roky pomocí knihovny Matplotlib v Pythonu.

## Obsah

- [Instalace](#instalace)
- [Použití](#použití)
- [Funkce](#funkce)
- [Vlastní poznatky](#poznatky)

## Instalace

Pro správnou funkci projektu je nutné mít nainstalován Python a knihovnu Matplotlib. Nainstalujte závislosti pomocí následujícího příkazu:

```bash
pip install matplotlib
```
Nebo můžete projekt spustit pomocí Google colab.
## Použití

Spusťte hlavní skrypt:
```bash
python main.py
```
Po spuštění programu budete vyzváni k výběru jedné z následujících operací:

1. Zobrazit graf tržeb
2. Odstranit daný rok
3. Přidat rok do tržeb
4. Vypsat maximální a minimální hodnotu za určitý rok
5. Porovnat 2 roky mezi sebou
6. KONEC

### Přehled funkcí
Zobrazení grafu tržeb
Vyberte rok, pro který chcete zobrazit graf. Program vykreslí graf tržeb za zvolený rok.

### Odstranění daného roku
Vyberte rok, který chcete odstranit ze záznamů.

### Přidání roku do tržeb
Přidejte nový rok a zadejte tržby pro každý měsíc.

### Vypsání maximální a minimální hodnoty za určitý rok
Vyberte rok a program vypíše maximální a minimální hodnotu tržeb pro daný rok.

### Porovnání 2 roky mezi sebou
Vyberte dva roky, které chcete porovnat. Program vykreslí grafy tržeb obou roků pro porovnání.

### Ukázkový vstup a výstup
Ukázkový vstup pro přidání nového roku:
```bash
Jaké jsou tvé tržby za měsíc Leden? 12000
Jaké jsou tvé tržby za měsíc Únor? 11500
...
Jaké jsou tvé tržby za měsíc Prosinec? 14000

```
## Funkce
1. graf(odpoved): Zobrazení grafu tržeb pro zvolený rok.
2. max_min(odpoved): Zobrazení maximální a minimální hodnoty tržeb pro zvolený rok.
3. hodnoty_list(): Vstup tržeb pro každý měsíc v roce.
4. porovnani(odpoved): Porovnání tržeb dvou roků mezi sebou.

## Poznatky
V projektu jsem využil všechny znalosti co jsem získal ve třetím ročníku v programování.
Projekt jsem celý vytvořil přes Google Colab.
