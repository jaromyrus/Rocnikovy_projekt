import matplotlib.pyplot as plt
mesice = ["Leden","Únor","Březen","Duben","Květen","Červen","Červenec","Srpen","Září","Říjen","Listopad","Prosinec"]
roky = {"2001":[10000,9500,8990,10500,11909,13010,15000,14400,13010,12500,12000,11200],
        "2002":[13000,11000,10500,9900,8800,15552,18090,20000,18600,16010,15000,14400],
        "2003":[14000,15000,18500,23200,25000,15500,12000,11500,16000,19000,26000,16500],
}
def graf(odpoved):
  plt.plot(mesice,roky[odpoved],color="#5a7d9a", marker="o")
  plt.title(f"Tržby za rok {odpoved}")
  plt.ylabel("Tržby v Kč")
  plt.xticks(rotation=45)
  plt.show()

def max_min(odpoved):
  maximum = max(roky[odpoved])
  minimum = min(roky[odpoved])
  print(f"V roce {odpoved} je maximální hodnota {maximum} a minimální hodnota {minimum}.")


def hodnoty_list():
  odpoved = []
  f = 12
  z =0

  while True:
    if z >= 12:
      break
    else:
      try:
        trzby = int(input(f"Jaké jsou tvé tržby za měsíc {mesice[z]}?"))
        z += 1
        odpoved.append(trzby)
      except:print("Piš pouze čísla!")
  return odpoved

def porovnani(odpoved):
  while True:
    porovnani_odpoved = input("S jakým rokem si ho přeješ porovnat?")
    if porovnani_odpoved in roky:
      plt.plot(mesice,roky[odpoved],color="#5a7d9a", marker="o", label = odpoved)
      plt.plot(mesice,roky[porovnani_odpoved],color="#52bd19", marker="o", label = porovnani_odpoved)
      plt.title(f"Porovnání roku {odpoved} a {porovnani_odpoved}")
      plt.ylabel("Tržby v Kč")
      plt.xticks(rotation=45)
      plt.legend()
      plt.show()
      break
    else:
      print("Rok který jsi vybral není ve slovníku!")

while True:
  rozcesti = input("Co chceš provést za operaci? \n 1. Zobrazit graf tržeb\n 2. Odstranit daný rok\n 3. Přidat rok do tržeb\n 4. Vypsat maximální a minimální hodnotu za určitý rok\n 5. Porovnat 2 roky mezi sebou \n 6. KONEC \n")
  if rozcesti == "STOP":
    break
  elif rozcesti == "1" or rozcesti == "2" or rozcesti == "3" or rozcesti == "4" or rozcesti == "5":
    while True:
      for keys, value in roky.items():
        print(keys)
      odpoved = input("Vyber si rok se kterým chceš manipulovat, nebo napiš KONEC\n")
      if odpoved in roky and rozcesti == "1":
        graf(odpoved)
        break
      elif odpoved in roky and rozcesti == "2":
        del roky[odpoved]
        break
      elif odpoved in roky and rozcesti == "3":
        print("Rok který jsis vybral už existuje!")
      elif odpoved not in roky and rozcesti =="3" and odpoved != "KONEC":
        roky[odpoved] = hodnoty_list()
        break
      elif odpoved in roky and rozcesti == "4":
        max_min(odpoved)
        break
      elif odpoved in roky and rozcesti == "5":
        porovnani(odpoved)
        break
      elif odpoved == "KONEC":
        break
      else:
        print("Rok který jsi vybral není ve slovníku!")
    else:
      print("Vyber si platnou možnost!")
  else:
    print("Neplatný znak!")