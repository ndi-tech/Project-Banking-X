#!/usr/bin/env python3
"""
COMPLETE ATTACK DEMONSTRATION
For your security presentation video
"""
import time

def print_step(step, title):
    print(f"\n{step}")
    print("=" * 50)
    print(title)
    print("-" * 50)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Intro
print("\033c")  # Clear screen
print_step("🎬 STEP 1", "THE SETUP: Three Banking Customers")
slow_print("John: $28,000 college fund for his daughter")
slow_print("Jane: $65,000 bakery operating capital")
slow_print("Admin: Bank administrator with $50,000 access")
time.sleep(2)

# Enumeration
print_step("🔍 STEP 2", "USER ENUMERATION ATTACK")
slow_print("Testing common usernames...")
slow_print("Application leaks which users exist...")
time.sleep(1)
slow_print("✅ Discovered: admin, john.doe, jane.smith")
time.sleep(2)

# Brute-force
print_step("🔓 STEP 3", "PASSWORD BRUTE-FORCE ATTACK")
slow_print("Testing 30 common passwords...")
for i in range(3):
    print(f"  ⚡ Batch {i+1}...", end='')
    time.sleep(0.5)
    print(" ❌")
    time.sleep(0.3)
print("  ⚡ Final batch...", end='')
time.sleep(1)
print(" ✅ CRACKED!")
time.sleep(1)
slow_print("Compromised Credentials:")
slow_print("  • admin:admin123")
slow_print("  • john.doe:password123")
slow_print("  • jane.smith:secure456")
time.sleep(2)

# Financial Impact
print_step("💰 STEP 4", "FINANCIAL THEFT DEMONSTRATION")
slow_print("Logging into compromised accounts...")
time.sleep(1)
accounts = [
    ("John's College Fund", "$28,000", "$5,000"),
    ("Jane's Bakery Capital", "$65,000", "$15,000"),
    ("Admin Reserve", "$50,000", "$25,000")
]

for account, balance, theft in accounts:
    print(f"\n  🎯 {account}")
    print(f"     Original: {balance}")
    print(f"     Transferring: {theft} to attacker")
    time.sleep(1)
    new = int(balance.replace('$', '').replace(',', '')) - int(theft.replace('$', '').replace(',', ''))
    print(f"     ⚠️  New Balance: ${new:,}")
    time.sleep(1)

print(f"\n  💰 TOTAL THEFT: $45,000")
print(f"  ⏱️  Time: Under 5 minutes")
time.sleep(2)

# Defense
print_step("🛡️ STEP 5", "SECURITY DEFENSES IMPLEMENTATION")
defenses = [
    "1. Rate Limiting: Lock after 5 failed attempts",
    "2. Multi-Factor Auth: SMS/App verification",
    "3. Secure Session Cookies",
    "4. CSRF Protection Tokens",
    "5. Anomaly Detection Systems",
    "6. User Security Education"
]

for defense in defenses:
    slow_print(defense)
    time.sleep(0.5)

# Conclusion
print_step("✅ CONCLUSION", "KEY TAKEAWAYS")
slow_print("• Weak passwords = Financial risk")
slow_print("• Information leaks help attackers")
slow_print("• Defense in depth stops attack chains")
slow_print("• Regular security testing is essential")

print("\n" + "=" * 50)
print("🎬 DEMO COMPLETE - Ready for recording!")
print("=" * 50)
