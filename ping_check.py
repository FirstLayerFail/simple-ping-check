# použitie modulu pre prácu s operačným systémom
import os

# Zadanie IP adresy, ktorú chceme skontrolovať
ip = input("Zadaj IP na overenie: ")

# spustenie systémového príkazu ping
# -c 2 odošle 2 testovacie pakety
odpoved = os.system(f"ping -c 2 {ip}")

# vyhodnotenie  pingu
# ak je odpoveď 0 daná IP je na sieti
if odpoved == 0:
    print(f"[+] Zariadenie {ip} je Online.")
else:
    print(f"[-] Zariadenie {ip} neodpovedá.")