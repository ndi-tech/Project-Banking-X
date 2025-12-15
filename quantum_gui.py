#!/usr/bin/env python3
"""
🚀 QUANTUM BRUTE-FORCE SIMULATOR - GUI Edition
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import time
import random
import threading

class QuantumBruteForceGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("⚡ Brute-Force Simulator")
        self.window.geometry("800x600")
        
        # User database
        self.users = {
            'admin': {'password': 'admin123', 'balance': '$50,000'},
            'john.doe': {'password': 'password123', 'balance': '$28,000'},
            'jane.smith': {'password': 'secure456', 'balance': '$65,000'},
            'bankadmin': {'password': 'BankSecure@2024', 'balance': '$100,000'},
            'sysadmin': {'password': 'Sys@dmin!789', 'balance': '$75,000'},
            'payroll': {'password': 'Payroll#2024', 'balance': '$200,000'},
        }
        
        # 30 passwords
        self.passwords = [
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
        
        self.attempts = 0
        self.cracked = []
        self.running = False
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        tk.Label(self.window, text="⚡ QUANTUM BRUTE-FORCE SIMULATOR",
                font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Label(self.window, text="Testing 30 passwords against 6 accounts",
                font=("Arial", 10)).pack()
        
        # Stats frame
        stats_frame = tk.Frame(self.window)
        stats_frame.pack(pady=10)
        
        self.attempts_label = tk.Label(stats_frame, text="Attempts: 0",
                                      font=("Arial", 11, "bold"))
        self.attempts_label.pack(side='left', padx=20)
        
        self.cracked_label = tk.Label(stats_frame, text="Cracked: 0/0",
                                     font=("Arial", 11, "bold"))
        self.cracked_label.pack(side='left', padx=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.window, length=400, mode='determinate')
        self.progress.pack(pady=5)
        
        # Stream display
        tk.Label(self.window, text="Live Attack Stream:",
                font=("Arial", 11, "bold")).pack(anchor='w', padx=20, pady=(10, 0))
        
        self.stream_text = scrolledtext.ScrolledText(self.window, height=10,
                                                    font=("Courier", 9))
        self.stream_text.pack(fill='both', expand=True, padx=20, pady=5)
        
        # Results display
        tk.Label(self.window, text="Cracked Accounts:",
                font=("Arial", 11, "bold")).pack(anchor='w', padx=20, pady=(10, 0))
        
        self.results_text = scrolledtext.ScrolledText(self.window, height=6,
                                                     font=("Courier", 9))
        self.results_text.pack(fill='both', expand=True, padx=20, pady=5)
        
        # Control buttons
        control_frame = tk.Frame(self.window)
        control_frame.pack(pady=10)
        
        self.start_btn = tk.Button(control_frame, text="🚀 Start Attack",
                                  command=self.start_attack, width=15)
        self.start_btn.pack(side='left', padx=5)
        
        self.stop_btn = tk.Button(control_frame, text="⏹️ Stop",
                                 command=self.stop_attack, width=15,
                                 state='disabled')
        self.stop_btn.pack(side='left', padx=5)
        
        tk.Button(control_frame, text="🔄 Reset",
                 command=self.reset_simulation, width=15).pack(side='left', padx=5)
    
    def start_attack(self):
        if not self.running:
            self.running = True
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')
            
            attack_thread = threading.Thread(target=self.run_simulation, daemon=True)
            attack_thread.start()
    
    def stop_attack(self):
        self.running = False
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
    
    def reset_simulation(self):
        self.stop_attack()
        self.attempts = 0
        self.cracked = []
        self.stream_text.delete(1.0, tk.END)
        self.results_text.delete(1.0, tk.END)
        self.progress['value'] = 0
        self.attempts_label.config(text="Attempts: 0")
        self.cracked_label.config(text="Cracked: 0/0")
    
    def run_simulation(self):
        user_list = list(self.users.keys())
        random.shuffle(user_list)
        random.shuffle(self.passwords)
        
        total = len(user_list) * len(self.passwords)
        
        for i, user in enumerate(user_list):
            for j, password in enumerate(self.passwords):
                if not self.running:
                    return
                
                self.attempts += 1
                
                # Update GUI
                self.window.after(0, self.update_counters)
                self.window.after(0, lambda p=(i*len(self.passwords)+j)/total*100: 
                                 self.progress.config(value=p))
                
                # Check password
                real_pw = self.users[user]['password']
                if password == real_pw:
                    self.cracked.append((user, password))
                    self.window.after(0, self.add_cracked, user, password)
                    self.window.after(0, self.add_to_stream, user, password, True)
                else:
                    if random.random() < 0.3:
                        self.window.after(0, self.add_to_stream, user, password, False)
                
                time.sleep(0.05)
        
        self.stop_attack()
        self.window.after(0, self.show_summary)
    
    def update_counters(self):
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.cracked_label.config(text=f"Cracked: {len(self.cracked)}/{len(self.users)}")
    
    def add_to_stream(self, user, password, success):
        timestamp = time.strftime("%H:%M:%S")
        if success:
            entry = f"[{timestamp}] ✅ CRACKED: {user} → {password}\n"
            self.stream_text.insert(1.0, entry, 'success')
            self.stream_text.tag_config('success', foreground='green')
        else:
            entry = f"[{timestamp}] ❌ FAILED: {user} → {password}\n"
            self.stream_text.insert(1.0, entry, 'failure')
            self.stream_text.tag_config('failure', foreground='red')
        
        # Limit lines
        lines = int(self.stream_text.index('end-1c').split('.')[0])
        if lines > 50:
            self.stream_text.delete('50.0', 'end')
    
    def add_cracked(self, user, password):
        info = self.users[user]
        entry = f"🔓 {user}\n🔐 {password}\n💰 {info['balance']}\n{'='*30}\n"
        self.results_text.insert(1.0, entry)
    
    def show_summary(self):
        summary = f"\n{'='*60}\nAttack Complete!\nAttempts: {self.attempts}\nCracked: {len(self.cracked)}/{len(self.users)}\n{'='*60}"
        messagebox.showinfo("Attack Complete", summary)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = QuantumBruteForceGUI()
    app.run()
