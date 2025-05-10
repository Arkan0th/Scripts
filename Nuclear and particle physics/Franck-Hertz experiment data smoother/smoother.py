import os
import numpy as np
import matplotlib.pyplot as plt

def aplikovat_vyhlazeni(data, iterace=3, koef_vyhlazeni=2):
    for _ in range(iterace):
        vyhlazena_data = []
        for i in range(0, len(data) - koef_vyhlazeni, koef_vyhlazeni):
            v_vyhlazene = round(np.mean([data[j][0] for j in range(i, i + koef_vyhlazeni)]), 3)
            c_vyhlazene = round(np.mean([data[j][1] for j in range(i, i + koef_vyhlazeni)]), 3)
            if v_vyhlazene >= 10:  # Odstranit hodnoty pod 10V
                vyhlazena_data.append((v_vyhlazene, c_vyhlazene))
        data = vyhlazena_data  # Aktualizovat data vyhlazenými výsledky
    return zip(*data)  # Vrátit oddělené seznamy napětí a proudu

def vyhladit_data(slozka, iterace=3):
    for nazev_souboru in os.listdir(slozka):
        if nazev_souboru.endswith("0"):  # Kontrola, zda název souboru odpovídá očekávanému vzoru
            cesta_souboru = os.path.join(slozka, nazev_souboru)
            
            with open(cesta_souboru, 'r') as soubor:
                radky = soubor.readlines()
            
            # Extrahovat data, přeskočit hlavičku
            data = []
            for radek in radky[2:]:  # Přeskočit první dva řádky
                casti = radek.strip().split('\t')
                if len(casti) == 2:  # Ujistit se, že jsou přesně dva sloupce
                    try:
                        napeti = float(casti[0].replace(',', '.'))
                        proud = float(casti[1].replace(',', '.'))
                        data.append((napeti, proud))
                    except ValueError:
                        continue  # Přeskočit řádky s nenumerickými hodnotami
            
            # Ujistit se, že je dostatek datových bodů
            if len(data) < 5:
                print(f"Přeskakuji {nazev_souboru}, nedostatek datových bodů.")
                continue
            
            # Aplikovat vyhlazení několikrát
            napeti_vyhlazene, proud_vyhlazeny = aplikovat_vyhlazeni(data, iterace=iterace)
            
            # Připravit nový název souboru
            novy_nazev = f"{nazev_souboru}_smooth"
            nova_cesta = os.path.join(slozka, novy_nazev)
            
            # Zapsat do nového souboru
            with open(nova_cesta, 'w') as novy_soubor:
                novy_soubor.write("Napětí U1\tProud IA\n")
                novy_soubor.write("U1/V\tIA/nA\n")
                for v, c in zip(napeti_vyhlazene, proud_vyhlazeny):
                    novy_soubor.write(f"{str(v).replace('.', ',')}\t{str(c).replace('.', ',')}\n")
            
            print(f"Zpracováno {nazev_souboru} -> {novy_nazev}")
            
            # Vykreslit vyhlazená data
            plt.figure()
            plt.plot(napeti_vyhlazene, proud_vyhlazeny, marker='o', linestyle='-', label=f"V-A charakteristika při {nazev_souboru}˚C")
            
            plt.xlabel("Napětí (V)")
            plt.ylabel("Proud (nA)")
            plt.title(f"Franck–Hertz experiment Hg výbojky při {nazev_souboru}˚C")
            plt.legend()
            plt.grid()
            plt.show()

if __name__ == "__main__":
    slozka = "./data"  # Změňte na vaši skutečnou složku
    vyhladit_data(slozka, iterace=3)

