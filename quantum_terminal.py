#!/usr/bin/env python3
"""
🚀 QUANTUM BRUTE-FORCE SIMULATOR - Terminal Matrix Edition
"""

import sys
import time
import random
from colorama import init, Fore

init(autoreset=True)

# User database (real + fake)
USERS_DB = {
    'admin': {'real_password': 'admin123', 'balance': '$50,000', 'role': 'Administrator'},
    'john.doe': {'real_password': 'password123', 'balance': '$28,000', 'role': 'Customer'},
    'jane.smith': {'real_password': 'secure456', 'balance': '$65,000', 'role': 'Business Owner'},
    'bankadmin': {'real_password': 'BankSecure@2024', 'balance': '$100,000', 'role': 'Bank Admin'},
    'sysadmin': {'real_password': 'Sys@dmin!789', 'balance': '$75,000', 'role': 'System Admin'},
    'payroll': {'real_password': 'Payroll#2024', 'balance': '$200,000', 'role': 'Payroll Manager'},
}

# 30 passwords
PASSWORD_LIST = [
    'admin123', 'password123', 'secure456', '123456', 'password',
    '123456789', 'qwerty', 'abc123', 'password1', '12345',
    '12345678', 'admin', 'welcome', 'login', 'letmein',
    'Admin@2024', 'P@ssw0rd', 'Secure!2024', 'Winter2023',
    'Banking123', 'Corporate2024', 'Finance#1', 'Business@123',
    'Summer2024', 'Spring2023', 'Autumn2024', 'Q1@2024',
    '2024Secure!', '2023Password', 'Jan2024!', 'Dec2023#',
    'P@$$w0rd2024', 'S3cur3P@ss!', 'B@nk1ng#Sec',
    'Adm1n!str@tor', 'J@neSmith789', 'J0hnDoe!456',
]

class FuturisticBruteForcer:
    def __init__(self):
        self.compromised = []
        self.attempts = 0
        self.successes = 0
    
    def clear_screen(self):
        print('\033c', end='')
    
    def print_header(self):
        self.clear_screen()
        print(f"{Fore.CYAN}{'='*70}")
        print(f"{Fore.GREEN}    ⚡ QUANTUM BRUTE-FORCE SIMULATOR ⚡")
        print(f"{Fore.CYAN}{'='*70}")
        print(f"{Fore.YELLOW}    PASSWORDS: {len(PASSWORD_LIST)} | USERS: {len(USERS_DB)}")
        print(f"{Fore.CYAN}{'='*70}\n")
    
    def run_attack(self):
        self.print_header()
        users = list(USERS_DB.keys())
        random.shuffle(users)
        random.shuffle(PASSWORD_LIST)
        
        print(f"{Fore.YELLOW}Initializing attack...\n")
        time.sleep(1)
        
        total = len(users) * len(PASSWORD_LIST)
        
        for i, user in enumerate(users):
            for j, password in enumerate(PASSWORD_LIST):
                self.attempts += 1
                
                # Check password
                real_pw = USERS_DB[user]['real_password']
                if password == real_pw:
                    print(f"{Fore.GREEN}✅ CRACKED: {user:15} → {password}")
                    self.successes += 1
                    self.compromised.append((user, password))
                elif random.random() < 0.3:  # Show some failures
                    print(f"{Fore.RED}❌ FAILED:  {user:15} → {password:20}")
                
                # Progress
                progress = (self.attempts / total) * 100
                if self.attempts % 10 == 0:
                    print(f"{Fore.CYAN}   Progress: {progress:5.1f}% ({self.attempts}/{total})")
                
                time.sleep(0.05)
        
        # Show results
        self.show_results()
    
    def show_results(self):
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.GREEN}    ATTACK COMPLETE")
        print(f"{Fore.CYAN}{'='*70}")
        print(f"{Fore.YELLOW}📊 STATISTICS:")
        print(f"  Total Attempts: {self.attempts}")
        print(f"  Successful Cracks: {self.successes}")
        
        if self.compromised:
            print(f"\n{Fore.RED}🚨 COMPROMISED ACCOUNTS:")
            for user, password in self.compromised:
                info = USERS_DB[user]
                print(f"  🔓 {user:15} | {info['role']:20} | {info['balance']:10}")
        
        print(f"\n{Fore.CYAN}{'='*70}")
        input(f"{Fore.YELLOW}Press Enter to exit...")

def main():
    forcer = FuturisticBruteForcer()
    try:
        forcer.run_attack()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Attack interrupted")

if __name__ == "__main__":
    main()
