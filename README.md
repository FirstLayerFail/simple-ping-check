# Simple Ping Sweeper

Môj prvý skript v Pythone, ktorý slúži na rýchle overenie, či je zadaná IP adresa aktívna v sieti (Online).

## 🚀 Ako to funguje
Skript využíva zabudovanú knižnicu `os` na odoslanie dvoch ICMP paketov (príkaz `ping -c 2`) cez Linux terminál. Následne vyhodnotí návratový kód systému a vypíše prehľadný výsledok.

## 💻 Spustenie
Pre spustenie skriptu v systéme Linux použi príkaz:
```bash
python3 ping_check.py