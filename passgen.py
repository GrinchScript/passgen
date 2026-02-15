#!/usr/bin/env python3
import random
import string
import argparse
import sys

# Цвета для терминала
class C:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def generate_password(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    pwd = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return pwd

def check_strength(pwd):
    score = 0
    if len(pwd) >= 12: score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1
    
    if score == 5:
        return f"{C.GREEN}{C.BOLD}STRONG{C.END} 🔒"
    elif score >= 3:
        return f"{C.YELLOW}{C.BOLD}MEDIUM{C.END} ⚠️"
    else:
        return f"{C.RED}{C.BOLD}WEAK{C.END} ❌"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{C.BOLD}🔐 Smart Password Generator{C.END}")
    parser.add_argument("-l", "--length", type=int, default=16, help="Длина пароля (по умолчанию: 16)")
    parser.add_argument("-n", "--no-special", action="store_true", help="Без спецсимволов")
    
    args = parser.parse_args()
    
    pwd = generate_password(args.length, not args.no_special)
    strength = check_strength(pwd)
    
    print(f"\n{C.BOLD}✨ Сгенерирован пароль:{C.END}")
    print(f"{C.GREEN}{C.BOLD}{pwd}{C.END}")
    print(f"\n{C.BOLD}Оценка надёжности:{C.END} {strength}\n")
