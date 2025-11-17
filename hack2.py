#!/usr/bin/env python3
import time, random, os, json, subprocess

R, G, Y, C, W, D = '\033[91m','\033[92m','\033[93m','\033[96m','\033[0m','\033[90m'

def beep(n=1, d=0.04):
    for _ in range(n): print('\a', end=''); time.sleep(d)

os.system('clear')
print(f"{R}╔{'═'*58}╗")
print(f"║{W}                QUANTUM BREACH v47 – 4 STRIKES                {R}║")
print(f"║{W}                       8×RTX 5090 // 499 M/s                  {R}║")
print(f"╚{'═'*58}╝{W}\n")
beep(12)

# REAL SCAN
print(f"{D}» Deploying stealth scanner...{W}")
try:
    data = json.loads(subprocess.check_output(['termux-wifi-scaninfo'], text=True))
except:
    print(f"{R}✘ Termux-API required → pkg install termux-api{W}"); exit()

nets = {}
for n in data:
    ssid = n.get('ssid','<Hidden>').strip() or '<Hidden>'
    rssi = n.get('rssi',-100)
    ch = n.get('channel','?')
    if ssid not in nets or rssi > nets[ssid][0]: nets[ssid] = (rssi,ch)

sorted_nets = sorted(nets.items(), key=lambda x: x[1][0], reverse=True)

print(f"{G}» {len(data)} targets acquired{W}\n")
for i, (s, (r,c)) in enumerate(sorted_nets[:12],1):
    bar = "▰▰▰▰" if r>=-50 else "▰▰▰░" if r>=-65 else "▰▰░░"
    col = G if r>=-65 else Y if r>=-80 else R
    print(f"{D}[{i:02}] {col}{bar}{W} {s:<28} {Y}Ch {c}{W}")

choice = input(f"\n{R}TARGET → {W}") or "1"
target_ssid = sorted_nets[int(choice)-1 if choice.isdigit() and 1<=int(choice)<=len(sorted_nets) else 0][0]
os.system('clear')
print(f"{R}LOCKED → {target_ssid}{W}\n")
beep(20)

# ONLY 4 EPIC ATTACKS – EACH ONE IS PURE FIRE
epic_attacks = [
    ("ZERO-DAY INJECT",       "PAYLOAD DELIVERED",        "\n{R}⚡ INJECTION SUCCESSFUL ⚡{W}"),
    ("NEURAL COLLAPSE",       "ENCRYPTION MELTDOWN",      "\n{R}☢️ QUANTUM COLLAPSE DETONATED ☢️{W}"),
    ("OMEGA PROTOCOL",        "SYSTEM OVERRIDE",          "\n{G}✔ ROOT SHELL ACQUIRED{W}"),
    ("FINAL STRIKE",          "TOTAL DOMINATION",         "\n{R}💀 BREACH COMPLETE – TARGET OWNED{W}")
]

for name, phrase, finish in epic_attacks:
    os.system('clear')
    print(f"{R}╔{'═'*58}╗")
    print(f"║{W}                EXECUTING {name:<28} {R}║")
    print(f"╚{'═'*58}╝{W}\n")
    for i in range(3):
        print(f"{Y}      [{'█'*(i+1)}{'░'*(2-i)}] {phrase}{W}")
        beep(10,0.05); time.sleep(1)
    print(f"{finish}\n")
    beep(15)

# Final cracking + self-destruct + savage roast
os.system('clear')
print(f"{G}╔{'═'*58}╗")
print(f"║{W}                  FINAL DECRYPTION – 499 M/s                  {G}║")
print(f"╚{'═'*58}╝{W}\n")
tried = 0
for _ in range(25):
    tried += random.randint(15000000,35000000)
    print(f"{Y}► {tried:,} keys tested  •  499 M/s{W}", end="\r")
    time.sleep(0.1); beep(2)

# SELF-DESTRUCT FIRST
os.system('clear')
print(f"{R}╔{'═'*58}╗")
print(f"║{W}               UNAUTHORIZED BREACH DETECTED                  {R}║")
print(f"║{W}                  using some advance tool to hack                      {R}║")
print(f"╚{'═'*58}╝{W}\n")
for i in range(10,0,-1):
    print(f"{R}                        {i:02}                            {W}")
    beep(6,0.1); time.sleep(1)

os.system('clear')
print(f"{R}                         💀 BOOM 💀                          {W}")
for _ in range(80): print('\a', end=''); time.sleep(0.03)

# THEN THE SAVAGE ROAST
os.system('clear')
print(f"""
{R}╔{'═'*58}╗
║{W}                        BREACH FAILED                         {R}║
║                                                             ║
║  TARGET → {W}{target_ssid:<44}{R}║
║                                                             ║
║{R}    ██╗    ██╗██╗███████╗██╗    ███████╗███████╗          {R}║
║{R}    ██║    ██║██║██╔════╝██║    ██╔════╝██╔════╝          {R}║
║{R}    ██║ █╗ ██║██║█████╗  ██║    ███████╗█████╗            {R}║
║{R}    ██║███╗██║██║██╔══╝  ██║    ╚════██║██╔══╝            {R}║
║{R}    ╚███╔███╔╝██║██║     ██║    ███████║███████╗          {R}║
║{R}     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝╚══════╝          {R}║
║                                                             ║
║  {Y}           WIFI IS TOO STRONG BRO !                     {R}║
║  {Y}           YOU HAVE TO LEARN REAL HACKING 😂😂😂         {R}║
╚{'═'*58}╝{W}
""")
beep(300,0.02)
time.sleep(6)
os.system('clear')
print(f"{G}Just kidding bro 😂 WiFi safe.\nGo learn real hacking on Kali.{W}")
