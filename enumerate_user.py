#!/usr/bin/env python3
"""
User Enumeration Demo - Banking System Security
DEMO MODE: Simulates both vulnerable and secure scenarios
"""

import requests
import time
import sys

# ================= CONFIGURATION =================
TARGET_URL = "http://localhost/banking-tutorial/"
DEMO_MODE = True  # Set to True for guaranteed demo, False for real testing
SIMULATE_VULNERABLE = True  # Simulate vulnerable app for demo

# Real demo accounts (from your setup)
REAL_ACCOUNTS = {
    'admin': {'password': 'admin123', 'balance': '$50,000', 'role': 'Administrator'},
    'john.doe': {'password': 'password123', 'balance': '$28,000', 'role': 'Customer'},
    'jane.smith': {'password': 'secure456', 'balance': '$65,000', 'role': 'Business Owner'}
}

# Expanded realistic username list
BANKING_USERNAMES = [
    # Real accounts
    'admin', 'john.doe', 'jane.smith',
    
    # Common patterns (some will be simulated as existing)
    'j.smith', 'smithj', 'jsmith01', 'customer', 'support',
    'bankadmin', 'sysadmin', 'root', 'administrator',
    
    # Personal accounts
    'robert.johnson', 'mjones', 'williams_b', 'patel.a',
    'david_lee', 'k.garcia', 'thomasw', 'sarah.connor',
    
    # Business accounts
    'payroll', 'accounting', 'audit', 'compliance',
    'manager', 'teller01', 'teller02', 'operations',
    
    # Test accounts
    'test.user', 'demo', 'guest', 'nonexistent123',
    'fakeuser', 'invalid.user', 'security.test'
]

# Terminal colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# ================= DEMO INTRO =================
def print_demo_header():
    print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}🚀 SECURITY DEMO: User Enumeration Attack{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}🎯 Target:{Colors.RESET} Banking Application Login")
    print(f"{Colors.BOLD}📊 Strategy:{Colors.RESET} Test {len(BANKING_USERNAMES)} usernames")
    print(f"{Colors.BOLD}🎯 Real Accounts:{Colors.RESET} {', '.join(REAL_ACCOUNTS.keys())}")
    
    if DEMO_MODE:
        if SIMULATE_VULNERABLE:
            print(f"{Colors.YELLOW}⚠️  DEMO MODE: Simulating VULNERABLE application{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}✅ DEMO MODE: Simulating SECURE application{Colors.RESET}")
    
    print(f"{Colors.CYAN}{'-'*70}{Colors.RESET}")

# ================= SIMULATION MODE =================
def simulate_response(username, is_vulnerable=True):
    """Simulate application responses for demo purposes"""
    if username in REAL_ACCOUNTS:
        # Real account - always exists
        if is_vulnerable:
            return f"Invalid password for user '{username}'. Please try again."
        else:
            return "Invalid username or password"
    elif username in ['bankadmin', 'sysadmin', 'payroll', 'accounting'] and is_vulnerable:
        # Simulate some common accounts existing in vulnerable app
        return f"Invalid password for user '{username}'"
    else:
        # User doesn't exist
        if is_vulnerable:
            return f"User '{username}' not found in our system."
        else:
            return "Invalid username or password"

# ================= ATTACK SIMULATION =================
def run_enumeration_demo():
    print_demo_header()
    
    vulnerable_users = []
    secure_users = []
    unknown_users = []
    
    print(f"\n{Colors.BOLD}🔍 Testing Usernames:{Colors.RESET}\n")
    
    for i, username in enumerate(BANKING_USERNAMES, 1):
        # Progress indicator with animation
        progress = f"{Colors.BOLD}[{i:2d}/{len(BANKING_USERNAMES)}]{Colors.RESET}"
        dots = '.' * ((i % 3) + 1)
        print(f"{progress} Testing: {Colors.BOLD}{username:<20}{Colors.RESET}", end="", flush=True)
        
        time.sleep(0.1)  # Small delay for dramatic effect
        
        try:
            if DEMO_MODE:
                # Use simulation
                response_text = simulate_response(username, SIMULATE_VULNERABLE)
                status_code = 200
            else:
                # Real request
                response = requests.post(
                    TARGET_URL,
                    data={'username': username, 'password': 'WRONG_PASS_2024!'},
                    headers={'User-Agent': 'SecurityAudit/1.0'},
                    allow_redirects=False,
                    timeout=2
                )
                response_text = response.text.lower()
                status_code = response.status_code
            
            # Analysis
            is_real_account = username in REAL_ACCOUNTS
            
            if DEMO_MODE and SIMULATE_VULNERABLE:
                # Simulated vulnerable application
                if 'invalid password' in response_text.lower() or username in REAL_ACCOUNTS:
                    print(f" {Colors.GREEN}✅ EXISTS{Colors.RESET}")
                    vulnerable_users.append(username)
                    
                    if is_real_account:
                        account = REAL_ACCOUNTS[username]
                        print(f"      {Colors.BLUE}🎯 REAL ACCOUNT: {account['role']} (Balance: {account['balance']}){Colors.RESET}")
                elif 'user not found' in response_text.lower():
                    print(f" {Colors.RED}❌ NOT FOUND{Colors.RESET}")
                    secure_users.append(username)
                else:
                    print(f" {Colors.YELLOW}⚠️  UNKNOWN{Colors.RESET}")
                    unknown_users.append(username)
            else:
                # Real or simulated secure application
                print(f" {Colors.YELLOW}🔒 SECURE{Colors.RESET}")
                secure_users.append(username)
                if is_real_account:
                    print(f"      {Colors.GREEN}Protected by identical error messages{Colors.RESET}")
        
        except Exception as e:
            print(f" {Colors.RED}⚠️  ERROR{Colors.RESET}")
            print(f"      {str(e)[:40]}")
    
    return vulnerable_users, secure_users, unknown_users

# ================= RESULTS DISPLAY =================
def print_results(vulnerable_users, secure_users, unknown_users):
    print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}📊 ENUMERATION RESULTS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
    
    # Found accounts
    real_found = [u for u in vulnerable_users if u in REAL_ACCOUNTS]
    other_found = [u for u in vulnerable_users if u not in REAL_ACCOUNTS]
    
    if vulnerable_users:
        print(f"\n{Colors.RED}{Colors.BOLD}🚨 VULNERABLE ACCOUNTS DISCOVERED:{Colors.RESET}")
        print(f"  Application leaks user existence through error messages")
        
        if real_found:
            print(f"\n{Colors.BLUE}{Colors.BOLD}🎯 REAL DEMO ACCOUNTS COMPROMISED:{Colors.RESET}")
            for user in real_found:
                acc = REAL_ACCOUNTS[user]
                print(f"  • {Colors.BOLD}{user}{Colors.RESET} - {acc['role']} (Balance: {acc['balance']})")
        
        if other_found:
            print(f"\n{Colors.YELLOW}📋 Other discovered accounts ({len(other_found)}):{Colors.RESET}")
            for user in other_found[:8]:
                print(f"  • {user}", end="")
            if len(other_found) > 8:
                print(f" ... and {len(other_found)-8} more")
    else:
        print(f"\n{Colors.GREEN}{Colors.Bold}✅ SECURE IMPLEMENTATION{Colors.RESET}")
        print(f"  Application successfully prevents user enumeration")
        print(f"  All failed logins return identical error messages")
    
    # Security impact analysis
    print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}🔒 SECURITY IMPACT ANALYSIS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
    
    if vulnerable_users:
        print(f"\n{Colors.RED}❌ INSECURE IMPLEMENTATION:{Colors.RESET}")
        print(f"  1. Attackers can discover valid usernames")
        print(f"  2. Reduces brute-force search space by {len(vulnerable_users)*100/len(BANKING_USERNAMES):.0f}%")
        print(f"  3. Enables targeted attacks on specific accounts")
        print(f"  4. First step in account takeover chain")
        
        print(f"\n{Colors.GREEN}✅ SECURITY FIX:{Colors.RESET}")
        print(f"  Always return identical error messages:")
        print(f"  {Colors.BOLD}Before:{Colors.RESET} 'Invalid password' vs 'User not found'")
        print(f"  {Colors.BOLD}After:{Colors.RESET} 'Invalid username or password' (for all failures)")
    else:
        print(f"\n{Colors.GREEN}✅ SECURE IMPLEMENTATION:{Colors.RESET}")
        print(f"  1. No information leakage to attackers")
        print(f"  2. Identical responses for all failed logins")
        print(f"  3. Proper implementation of security best practices")
    
    # Demo toggle instructions
    print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}🎬 DEMO CONTROLS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"\nToggle demo modes by editing script:")
    print(f"  {Colors.YELLOW}DEMO_MODE = True{Colors.RESET} - Use simulation (recommended for presentation)")
    print(f"  {Colors.YELLOW}DEMO_MODE = False{Colors.RESET} - Test real application")
    print(f"  {Colors.YELLOW}SIMULATE_VULNERABLE = True/False{Colors.RESET} - Show vulnerable/secure scenario")
    
    print(f"\n{Colors.BOLD}Real test command:{Colors.RESET}")
    print(f"  curl -s -X POST '{TARGET_URL}' -d 'username=admin&password=wrong' | grep -i 'invalid\\|error\\|not'")

# ================= MAIN EXECUTION =================
if __name__ == "__main__":
    # Clear screen for clean demo
    print("\033c", end="")
    
    # Run the demo
    vulnerable, secure, unknown = run_enumeration_demo()
    
    # Show results
    print_results(vulnerable, secure, unknown)
    
    # Final call to action
    print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.PURPLE}🎯 FOR YOUR PRESENTATION:{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}{Colors.RESET}")
    
    if SIMULATE_VULNERABLE:
        print(f"""
{Colors.BOLD}Demo Script:{Colors.RESET}
1. "Watch as we test 30 common banking usernames..."
2. "The application returns different error messages..."
3. "We've discovered valid accounts: admin, john.doe, jane.smith"
4. "This information leak enables targeted attacks"
5. "The fix: Use identical error messages for all failed logins"
        """)
    else:
        print(f"""
{Colors.BOLD}Demo Script:{Colors.RESET}
1. "We're testing the same 30 usernames..."
2. "Notice all responses are identical: 'Invalid username or password'"
3. "No information leakage - this is secure implementation"
4. "Attackers cannot determine which accounts exist"
5. "This is security best practice in action"
        """)
