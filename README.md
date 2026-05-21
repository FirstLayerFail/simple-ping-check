# Simple Ping check
Môj prvý skript v Pythone, ktorý slúži na overenie, či je zadaná IP adresa aktívna v sieti (Online).

*My first Python script, designed to quickly verify whether a specified IP address is active on the network (Online).*

## Ako to funguje
Skript využíva zabudovanú knižnicu `os` na odoslanie dvoch ICMP paketov (príkaz `ping -c 2`) cez Linux terminál. Následne vyhodnotí návratový kód systému a vypíše výsledok.
## *How it works*
*The script utilizes the built-in `os` library to send two ICMP packets (using the `ping -c 2` command) via the Linux terminal. It then evaluates the system's return code and prints a result.*

## Spustenie
Pre spustenie skriptu v systéme Linux použi príkaz:
## *Running the script*
*To run this script on a Linux system, use the following command:*
```bash
python3 ping_check.py
