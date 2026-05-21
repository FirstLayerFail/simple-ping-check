# Simple Ping Sweeper

🇸🇰 Slovenská verzia

Môj prvý skript v Pythone, ktorý slúži naoverenie, či je zadaná IP adresa aktívna v sieti (Online).

Ako to funguje

Skript využíva zabudovanú knižnicu os na odoslanie dvoch ICMP paketov (príkaz ping -c 2) cez Linux terminál. Následne vyhodnotí návratový kód systému a vypíše prehľadný výsledok.

Spustenie

Pre spustenie skriptu v systéme Linux použi príkaz:

python3 ping_check.py


🇬🇧 English version

My first Python script, designed to verify whether a specified IP address is active on the network (Online).

How it works

The script utilizes the built-in os library to send two ICMP packets (using the ping -c 2 command) via the Linux terminal. It then evaluates the system's return code and prints a clear result.

Running the script

To run this script on a Linux system, use the following command:

python3 ping_check.py
